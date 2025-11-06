# 🗺️ Matplotlib 模擬系統 - 使用流程圖

## 📋 決策樹：選擇正確的方法

```
開始寫測試
    │
    ├─→ 測試包含 plt.show()？
    │   │
    │   ├─→ 是 → 什麼都不用做！✅
    │   │        自動模擬會處理
    │   │
    │   └─→ 否 → 繼續寫測試
    │
    ├─→ 需要驗證繪圖方法被調用？
    │   │
    │   ├─→ 是 → 使用 capture_plot_calls
    │   │        │
    │   │        └─→ with capture_plot_calls:
    │   │                your_code()
    │   │            assert capture_plot_calls.xxx_called
    │   │
    │   └─→ 否 → 繼續
    │
    ├─→ 測試複雜的繪圖邏輯？
    │   │
    │   ├─→ 是 → 使用 no_display
    │   │        │
    │   │        └─→ def test(no_display):
    │   │                your_function()
    │   │
    │   └─→ 否 → 繼續
    │
    └─→ 需要完全控制 pyplot？
        │
        ├─→ 是 → 使用 mock_plt 或 mock_figure
        │        (進階用法)
        │
        └─→ 否 → 使用自動模擬即可
```

---

## 🎯 場景導航

### 場景 A: 簡單測試（90% 情況）

```
您的測試
    ↓
   [無需額外代碼]
    ↓
自動模擬處理一切
    ↓
  ✅ 完成
```

**代碼範例**:
```python
def test_simple():
    plt.plot([1, 2, 3])
    plt.show()  # 自動模擬
```

---

### 場景 B: 需要驗證（8% 情況）

```
您的測試
    ↓
使用 capture_plot_calls
    ↓
執行繪圖代碼
    ↓
驗證調用
    ↓
  ✅ 完成
```

**代碼範例**:
```python
def test_verify(capture_plot_calls):
    with capture_plot_calls:
        my_plot_function()
    
    assert capture_plot_calls.plot_called
```

---

### 場景 C: 測試現有函數（2% 情況）

```
導入模組
    ↓
使用 no_display
    ↓
調用函數
    ↓
  ✅ 完成
```

**代碼範例**:
```python
def test_existing(no_display):
    from notebook import plot_NQueens
    plot_NQueens([0, 4, 7, 5, 2, 6, 1, 3])
```

---

## 🔄 工作流程

### 新功能開發流程

```
┌─────────────────┐
│  1. 寫功能代碼   │
│  (包含繪圖)     │
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│  2. 寫測試       │
│  (自動模擬)     │
└────────┬────────┘
         │
         ↓
┌─────────────────┐
│  3. 運行測試     │
│  pytest ...     │
└────────┬────────┘
         │
    ┌────┴────┐
    │         │
    ↓         ↓
  通過       失敗
    │         │
    │         ↓
    │    ┌─────────┐
    │    │ 4. 調試  │
    │    │ (查看調用)│
    │    └────┬────┘
    │         │
    │         ↓
    │    使用 capture_plot_calls
    │    查看實際調用
    │         │
    └────┬────┘
         │
         ↓
     ✅ 完成
```

---

## 📊 Fixture 選擇流程圖

```
需要測試繪圖代碼？
         │
         ↓
      ┌──┴──┐
      是    否 → 不需要模擬
      │
      ↓
需要驗證具體的繪圖調用？
      │
   ┌──┴──┐
   是    否
   │     │
   │     ↓
   │  只需要防止視窗彈出？
   │     │
   │  ┌──┴──┐
   │  是    否
   │  │     │
   │  │     ↓
   │  │  需要模擬 Figure 物件？
   │  │     │
   │  │  ┌──┴──┐
   │  │  是    否
   │  │  │     │
   │  │  │     ↓
   │  │  │  需要完全控制？
   │  │  │     │
   │  │  │  ┌──┴──┐
   │  │  │  是    否
   │  │  │  │     │
   │  ↓  ↓  ↓     ↓
   │  │  │  │   自動模擬
   │  │  │  │   (什麼都不用)
   │  │  │  │
   │  │  │  └─→ mock_plt
   │  │  │
   │  │  └─────→ mock_figure
   │  │
   │  └─────────→ no_display
   │
   └────────────→ capture_plot_calls
```

---

## 🎓 學習路徑流程

### 初學者路徑

```
START
  │
  ↓
閱讀 QUICK_REFERENCE.md (5 min)
  │
  ↓
查看 test_mock_figures.py
測試 1-3 (10 min)
  │
  ↓
寫第一個測試 (5 min)
  │
  ↓
運行測試 (1 min)
  │
  ↓
✅ 可以開始工作了！
  │
  ↓
遇到問題？
  │
  ↓
查閱 MOCK_FIGURES_README.md
```

### 進階使用者路徑

```
START
  │
  ↓
閱讀 README_MOCKING.md (10 min)
  │
  ↓
完整閱讀 MOCK_FIGURES_README.md (20 min)
  │
  ↓
研究所有測試範例 (30 min)
  │
  ├─→ test_mock_figures.py
  └─→ test_notebook_plotting.py
  │
  ↓
實踐所有 fixtures
  │
  ↓
✅ 精通模擬系統！
  │
  ↓
需要更多？
  │
  ↓
研究 conftest.py 實作
  │
  ↓
自定義 fixtures
```

---

## 🔍 問題排查流程

```
遇到問題
  │
  ↓
查看錯誤訊息
  │
  ├─→ "視窗彈出"
  │   │
  │   ↓
  │   檢查 conftest.py 是否在 tests/ 目錄
  │   │
  │   ├─→ 是 → 在測試開頭添加:
  │   │        import matplotlib
  │   │        matplotlib.use('Agg')
  │   │
  │   └─→ 否 → 創建或移動 conftest.py
  │
  ├─→ "沒有捕獲到調用"
  │   │
  │   ↓
  │   確認使用了 with 語句
  │   │
  │   └─→ with capture_plot_calls:
  │           your_code()
  │
  ├─→ "找不到 fixture"
  │   │
  │   ↓
  │   確認 conftest.py 位置正確
  │   │
  │   └─→ tests/conftest.py
  │
  └─→ "其他問題"
      │
      ↓
      運行 verify_mock.py
      │
      ↓
      查看 MOCK_FIGURES_README.md
      故障排除部分
```

---

## 📈 複雜度升級路徑

```
Level 1: 基礎使用
├─ 什麼都不做
├─ 自動模擬處理
└─ ✅ 90% 的測試
    │
    ↓
Level 2: 簡單驗證
├─ 使用 no_display
├─ 測試不彈出視窗
└─ ✅ 95% 的測試
    │
    ↓
Level 3: 進階驗證
├─ 使用 capture_plot_calls
├─ 驗證特定調用
└─ ✅ 99% 的測試
    │
    ↓
Level 4: 完全控制
├─ 使用 mock_figure
├─ 使用 mock_plt
├─ 自定義 fixtures
└─ ✅ 100% 的測試
```

---

## 🎯 快速決策表

| 我需要... | 使用 | 難度 | 示例 |
|-----------|------|------|------|
| 防止視窗彈出 | 自動模擬 | ⭐ | 無需代碼 |
| 測試簡單函數 | no_display | ⭐ | `def test(no_display):` |
| 驗證 plot() | capture_plot_calls | ⭐⭐ | `with capture_plot_calls:` |
| 驗證多個調用 | capture_plot_calls | ⭐⭐ | 查看 `.calls` |
| 模擬 Figure | mock_figure | ⭐⭐⭐ | `with patch(...)` |
| 完全控制 | mock_plt | ⭐⭐⭐ | 自定義模擬 |

---

## 🚀 快速開始流程

```
1. 安裝
   pip install -r requirements.txt
   
         ↓
         
2. 寫測試
   def test_my_plot():
       plt.plot([1, 2, 3])
       plt.show()
   
         ↓
         
3. 運行
   pytest tests/test_my_plot.py
   
         ↓
         
4. ✅ 成功！
```

---

## 💡 記憶技巧

### 使用頻率記憶法

```
自動模擬         ████████████████████ 90%
no_display      ████                  8%
capture_calls   █                     2%
mock_figure     ·                    <1%
mock_plt        ·                    <1%
```

### 三層記憶法

```
初級: 讓它自動處理
      ↓
中級: 使用 no_display 和 capture_plot_calls
      ↓
高級: 自定義模擬
```

---

## 🎨 視覺速查

### ✅ 正確的模式

```python
# 模式 A: 自動（最簡單）
def test():
    plt.plot([1, 2, 3])
    plt.show()  # ✅

# 模式 B: 驗證
def test(capture_plot_calls):
    with capture_plot_calls:  # ✅
        plt.plot([1, 2, 3])
    assert capture_plot_calls.plot_called

# 模式 C: 簡單
def test(no_display):  # ✅
    my_function()
```

### ❌ 錯誤的模式

```python
# 錯誤 A: 不需要的模擬
def test():
    with patch('plt.show'):  # ❌ 不需要，自動處理
        plt.show()

# 錯誤 B: 忘記 with
def test(capture_plot_calls):
    plt.plot([1, 2, 3])  # ❌ 不會被捕獲
    assert capture_plot_calls.plot_called

# 錯誤 C: 過度複雜
def test():
    mock = MagicMock()  # ❌ 不需要手動模擬
    with patch('plt', mock):
        plt.show()
```

---

## 🎯 目標檢查清單

### 新手目標（第 1 天）
- [ ] 閱讀 QUICK_REFERENCE.md
- [ ] 運行一個測試範例
- [ ] 寫第一個測試
- [ ] 測試通過

### 中級目標（第 1 週）
- [ ] 使用 capture_plot_calls
- [ ] 測試現有函數
- [ ] 理解所有 fixtures
- [ ] 寫 10+ 測試

### 高級目標（第 1 月）
- [ ] 自定義 fixtures
- [ ] 貢獻改進
- [ ] 幫助其他開發者
- [ ] 精通所有功能

---

## 🔗 快速跳轉

- 📘 [快速參考](QUICK_REFERENCE.md)
- 📗 [完整指南](MOCK_FIGURES_README.md)
- 📙 [總覽](README_MOCKING.md)
- 📕 [索引](INDEX.md)
- 📓 [範例](test_mock_figures.py)

---

**現在就開始！** 選擇您的路徑 → 跟隨流程 → 開始測試！🚀


