# Matplotlib 模擬快速參考

## 🚀 快速開始

### 最簡單的方式（無需額外代碼）

```python
def test_my_function():
    plt.plot([1, 2, 3])
    plt.show()  # ✅ 自動被模擬，不會彈出視窗
```

> **為什麼有效？** `conftest.py` 中的 `mock_matplotlib_show` 自動應用到所有測試。

---

## 📌 常用場景

### 場景 1: 測試繪圖函數（不關心細節）

```python
def test_plotting_function(no_display):
    my_plotting_function()  # 完成即可
```

### 場景 2: 驗證特定方法被調用

```python
def test_plot_called(capture_plot_calls):
    with capture_plot_calls:
        my_plotting_function()
    
    assert capture_plot_calls.plot_called      # ✅ 驗證 plot()
    assert capture_plot_calls.show_called      # ✅ 驗證 show()
```

### 場景 3: 檢查調用次數和參數

```python
def test_plot_details(capture_plot_calls):
    with capture_plot_calls:
        plt.plot([1, 2, 3])
        plt.plot([4, 5, 6])
    
    # 檢查調用歷史
    plot_calls = [c for c in capture_plot_calls.calls if c[0] == 'plot']
    assert len(plot_calls) == 2  # 兩次 plot() 調用
```

---

## 🎯 Fixtures 速查表

| Fixture | 何時使用 | 需要 `with`？ |
|---------|----------|--------------|
| `mock_matplotlib_show` | 自動應用 | ❌ |
| `no_display` | 簡單測試，不需驗證 | ❌ |
| `capture_plot_calls` | 需要驗證調用 | ✅ |
| `mock_figure` | 需要模擬 Figure 物件 | ✅ (with patch) |
| `mock_plt` | 需要完全控制 pyplot | ✅ (with patch) |

---

## 🔍 capture_plot_calls 屬性

```python
capture_plot_calls.plot_called      # bool: plot() 被調用？
capture_plot_calls.show_called      # bool: show() 被調用？
capture_plot_calls.figure_called    # bool: figure() 被調用？
capture_plot_calls.imshow_called    # bool: imshow() 被調用？
capture_plot_calls.scatter_called   # bool: scatter() 被調用？
capture_plot_calls.savefig_called   # bool: savefig() 被調用？
capture_plot_calls.calls            # list: 所有調用 [(name, args, kwargs), ...]
```

---

## ⚡ 實用範例

### 測試熱圖

```python
def test_heatmap(capture_plot_calls):
    with capture_plot_calls:
        plt.imshow([[1, 2], [3, 4]])
        plt.show()
    
    assert capture_plot_calls.imshow_called
```

### 測試多個子圖

```python
def test_subplots():
    fig, (ax1, ax2) = plt.subplots(1, 2)
    ax1.plot([1, 2, 3])
    ax2.scatter([1, 2, 3], [3, 2, 1])
    plt.close()  # ✅ 良好習慣
```

### 測試 3D 繪圖

```python
def test_3d_plot():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(X, Y, Z)
    plt.close()
```

---

## 🛠️ 運行測試

```bash
# 運行所有測試
pytest tests/

# 運行特定檔案
pytest tests/test_mock_figures.py

# 詳細輸出
pytest tests/test_mock_figures.py -v

# 運行單一測試
pytest tests/test_mock_figures.py::test_capture_plot_calls
```

---

## 💡 提示和技巧

### ✅ 最佳實踐

- 使用 `plt.close()` 或 `plt.close('all')` 清理資源
- 每個測試應該獨立，不依賴其他測試
- 優先使用 `no_display` 除非需要驗證

### ⚠️ 常見陷阱

```python
# ❌ 錯誤：忘記使用 with
def test_bad(capture_plot_calls):
    plt.plot([1, 2, 3])  # 不會被捕獲！

# ✅ 正確：使用 with
def test_good(capture_plot_calls):
    with capture_plot_calls:
        plt.plot([1, 2, 3])  # 會被捕獲
```

### 🔧 調試技巧

```python
# 查看所有調用
def test_debug(capture_plot_calls):
    with capture_plot_calls:
        my_complex_function()
    
    for name, args, kwargs in capture_plot_calls.calls:
        print(f"{name}() 被調用，參數: {args}")
```

---

## 📚 更多資訊

- **詳細文檔**: `tests/MOCK_FIGURES_README.md`
- **範例測試**: `tests/test_mock_figures.py`
- **驗證腳本**: `tests/verify_mock.py`
- **設置說明**: `MOCK_FIGURES_SETUP.md`

---

## 🆘 疑難排解

### 問題：測試時仍然彈出視窗

**解決**:
```python
# 在測試檔案頂部添加
import matplotlib
matplotlib.use('Agg')
```

### 問題：capture_plot_calls 沒有捕獲

**解決**: 確保使用 `with` 語句:
```python
with capture_plot_calls:
    # 所有繪圖代碼放在這裡
    plt.plot([1, 2, 3])
```

### 問題：找不到 conftest.py

**解決**: 確保 `conftest.py` 在 `tests/` 目錄中。

---

**記住**: 大多數情況下，您不需要做任何特殊處理！測試會自動使用 Agg 後端並模擬 `plt.show()`。


