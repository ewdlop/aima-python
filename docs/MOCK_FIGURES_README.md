# Matplotlib 圖表模擬指南

本文檔說明如何在 AIMA-Python 專案的測試中模擬 matplotlib 圖表。

## 概述

在運行測試時，我們不希望彈出圖表視窗或生成實際的圖像檔案。`conftest.py` 提供了多種 fixtures 來模擬 matplotlib 的繪圖功能。

## 可用的 Fixtures

### 1. `mock_matplotlib_show` (自動啟用)

**用途**: 自動模擬所有測試中的 `plt.show()`，防止彈出視窗。

**特點**: 
- 設定為 `autouse=True`，無需顯式調用
- 自動應用到所有測試
- 使用 `Agg` 非互動式後端

**範例**:
```python
def test_simple_plot():
    plt.plot([1, 2, 3])
    plt.show()  # 不會彈出視窗
```

### 2. `mock_figure`

**用途**: 提供一個模擬的 `Figure` 物件，用於測試繪圖邏輯。

**使用方法**:
```python
def test_with_mock_figure(mock_figure):
    with patch('matplotlib.pyplot.figure', return_value=mock_figure):
        fig = plt.figure(figsize=(10, 5))
        ax = fig.add_subplot(111)
        ax.plot([1, 2, 3])
        
        # 驗證方法被調用
        assert mock_figure.add_subplot.called
```

### 3. `mock_plt`

**用途**: 提供完整的 `matplotlib.pyplot` 模擬物件。

**使用方法**:
```python
def test_with_mock_plt(mock_plt):
    with patch.dict('sys.modules', {'matplotlib.pyplot': mock_plt}):
        mock_plt.figure()
        mock_plt.plot([1, 2, 3])
        
        assert mock_plt.plot.called
```

### 4. `capture_plot_calls`

**用途**: 捕獲並記錄所有繪圖調用，用於驗證繪圖行為。

**使用方法**:
```python
def test_capture_calls(capture_plot_calls):
    with capture_plot_calls:
        plt.figure()
        plt.plot([1, 2, 3])
        plt.show()
    
    # 驗證調用
    assert capture_plot_calls.figure_called
    assert capture_plot_calls.plot_called
    assert capture_plot_calls.show_called
    
    # 檢查調用歷史
    print(capture_plot_calls.calls)
```

**可用屬性**:
- `plot_called`: 是否調用了 `plot()`
- `show_called`: 是否調用了 `show()`
- `figure_called`: 是否調用了 `figure()`
- `imshow_called`: 是否調用了 `imshow()`
- `scatter_called`: 是否調用了 `scatter()`
- `savefig_called`: 是否調用了 `savefig()`
- `calls`: 所有調用的列表 `[(函數名, args, kwargs), ...]`

### 5. `no_display`

**用途**: 完全禁用所有顯示和繪圖操作。

**使用方法**:
```python
def test_no_display(no_display):
    plt.plot([1, 2, 3])
    plt.show()
    plt.savefig('test.png')
    # 所有操作都被靜默處理
```

## 使用場景

### 場景 1: 測試包含繪圖的函數

假設您有一個函數需要繪製圖表：

```python
# 在 notebook.py 中
def plot_NQueens(solution):
    n = len(solution)
    fig = plt.figure(figsize=(7, 7))
    ax = fig.add_subplot(111)
    ax.set_title('{} Queens'.format(n))
    plt.show()
```

測試這個函數：

```python
def test_plot_NQueens(no_display):
    solution = [0, 4, 7, 5, 2, 6, 1, 3]
    plot_NQueens(solution)  # 不會彈出視窗
    # 函數執行完成，沒有錯誤
```

### 場景 2: 驗證繪圖調用

如果您需要驗證特定的繪圖方法被調用：

```python
def test_verify_plotting_behavior(capture_plot_calls):
    with capture_plot_calls:
        # 執行繪圖代碼
        plt.figure()
        plt.plot([1, 2, 3], [4, 5, 6])
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.show()
    
    # 驗證
    assert capture_plot_calls.figure_called
    assert capture_plot_calls.plot_called
    assert capture_plot_calls.show_called
    assert len(capture_plot_calls.calls) >= 3
```

### 場景 3: 測試熱圖或複雜視覺化

```python
def test_heatmap(capture_plot_calls):
    with capture_plot_calls:
        grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        heatmap(grid)  # 您的熱圖函數
    
    assert capture_plot_calls.imshow_called
```

### 場景 4: 測試多個圖表

```python
def test_multiple_figures():
    # 自動模擬 show()
    for i in range(5):
        fig = plt.figure()
        plt.plot([1, 2, 3])
        plt.close(fig)
    # 無視窗彈出
```

## 最佳實踐

1. **預設使用自動模擬**: 大多數測試不需要顯式使用 fixture，因為 `mock_matplotlib_show` 會自動處理。

2. **需要驗證時使用 `capture_plot_calls`**: 當您需要驗證特定的繪圖方法被調用時。

3. **清理資源**: 使用 `plt.close()` 關閉不再需要的 figure 物件。

4. **隔離測試**: 每個測試應該獨立，不依賴其他測試的繪圖狀態。

## 配置說明

### matplotlib 後端

在 `conftest.py` 中設定：
```python
matplotlib.use('Agg')
```

這將 matplotlib 設定為非互動式後端，不會創建任何視窗。

### pytest.ini 配置

現有的 `pytest.ini` 已經配置了忽略警告：
```ini
[pytest]
filterwarnings =
    ignore::DeprecationWarning
    ignore::UserWarning
    ignore::RuntimeWarning
```

## 運行測試

運行所有測試：
```bash
pytest tests/
```

運行特定測試檔案：
```bash
pytest tests/test_mock_figures.py
```

運行特定測試：
```bash
pytest tests/test_mock_figures.py::test_capture_plot_calls
```

啟用詳細輸出：
```bash
pytest tests/ -v
```

## 故障排除

### 問題：測試時仍然彈出視窗

**解決方案**:
1. 確保 `conftest.py` 在 `tests/` 目錄中
2. 檢查是否有其他地方設定了互動式後端
3. 在測試檔案開頭添加：
   ```python
   import matplotlib
   matplotlib.use('Agg')
   ```

### 問題：Mock 物件沒有特定屬性

**解決方案**:
在 `conftest.py` 的相應 fixture 中添加該屬性的模擬。

### 問題：無法驗證繪圖調用

**解決方案**:
使用 `capture_plot_calls` fixture 並確保在其 context manager 內執行繪圖代碼。

## 範例測試檔案

完整的範例請參考 `tests/test_mock_figures.py`。

## 進階用法

### 自定義模擬行為

```python
def test_custom_mock():
    with patch('matplotlib.pyplot.plot') as mock_plot:
        mock_plot.return_value = [Mock()]
        plt.plot([1, 2, 3])
        
        # 驗證參數
        mock_plot.assert_called_once()
        args, kwargs = mock_plot.call_args
        assert len(args[0]) == 3
```

### 模擬特定模組的繪圖

```python
def test_module_specific():
    with patch('notebook.plt.show'):
        # 只模擬 notebook.py 中的 plt.show
        from notebook import plot_NQueens
        plot_NQueens([1, 3, 5, 7, 2, 0, 6, 4])
```

## 相關資源

- [pytest 文檔](https://docs.pytest.org/)
- [unittest.mock 文檔](https://docs.python.org/3/library/unittest.mock.html)
- [matplotlib 後端](https://matplotlib.org/stable/users/explain/backends.html)

## 維護

如果需要添加新的繪圖函數模擬，請更新 `conftest.py` 中相應的 fixture。


