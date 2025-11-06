# Matplotlib 圖表模擬系統設置完成

## 概述

已為 AIMA-Python 專案創建完整的 matplotlib 圖表模擬系統，用於在測試環境中防止圖表視窗彈出。

## 創建的檔案

### 1. `tests/conftest.py` ⭐ 核心配置檔案

**功能**: 
- 設定 matplotlib 使用非互動式後端 (`Agg`)
- 提供 5 個不同的 pytest fixtures 用於各種測試場景

**包含的 Fixtures**:

| Fixture | 類型 | 用途 |
|---------|------|------|
| `mock_matplotlib_show` | 自動啟用 | 自動模擬所有 `plt.show()` 調用 |
| `mock_figure` | 手動調用 | 提供模擬的 Figure 物件 |
| `mock_plt` | 手動調用 | 提供完整的 pyplot 模擬 |
| `capture_plot_calls` | 手動調用 | 捕獲並記錄所有繪圖調用 |
| `no_display` | 手動調用 | 完全禁用顯示和儲存操作 |

### 2. `tests/test_mock_figures.py` 📝 示例測試檔案

**內容**:
- 10 個完整的測試範例
- 展示每個 fixture 的使用方法
- 涵蓋各種繪圖場景（基本繪圖、熱圖、3D 繪圖等）

**測試案例**:
- ✓ `test_auto_mock_show()` - 自動模擬測試
- ✓ `test_with_mock_figure()` - 模擬 Figure 物件
- ✓ `test_with_mock_plt()` - 完整 pyplot 模擬
- ✓ `test_capture_plot_calls()` - 捕獲繪圖調用
- ✓ `test_no_display_fixture()` - 禁用顯示
- ✓ `test_multiple_plots()` - 多圖表處理
- ✓ `test_complex_plotting_scenario()` - 複雜場景
- ✓ `test_heatmap_plotting()` - 熱圖繪製
- ✓ `test_3d_plotting()` - 3D 繪圖

### 3. `tests/MOCK_FIGURES_README.md` 📚 完整文檔

**內容**:
- 詳細的使用指南
- 每個 fixture 的說明和範例
- 常見使用場景
- 最佳實踐建議
- 故障排除指南
- 進階用法

### 4. `tests/verify_mock.py` 🔍 驗證腳本

**用途**:
- 不依賴 pytest 的獨立驗證腳本
- 測試所有核心模擬功能
- 驗證 conftest.py 的正確性

## 使用方法

### 基本使用（最簡單）

```python
# 測試會自動使用 Agg 後端，plt.show() 會被自動模擬
def test_my_plotting_function():
    plt.plot([1, 2, 3])
    plt.show()  # 不會彈出視窗
```

### 驗證繪圖行為

```python
def test_verify_plotting(capture_plot_calls):
    with capture_plot_calls:
        my_plotting_function()
    
    assert capture_plot_calls.plot_called
    assert capture_plot_calls.show_called
```

### 完全禁用顯示

```python
def test_no_windows(no_display):
    my_plotting_function()  # 所有顯示操作被靜默
```

## 安裝和測試

### 1. 安裝依賴

```bash
# 安裝專案依賴（包括 pytest）
pip install -r requirements.txt

# 或只安裝 pytest
pip install pytest pytest-cov
```

### 2. 運行測試

```bash
# 運行所有測試
pytest tests/

# 運行模擬測試範例
pytest tests/test_mock_figures.py -v

# 運行特定測試
pytest tests/test_mock_figures.py::test_capture_plot_calls -v
```

### 3. 驗證設置

```bash
# 運行驗證腳本（不需要 pytest）
python tests/verify_mock.py
```

## 特點

✅ **自動化**: 使用 `autouse=True`，無需手動配置  
✅ **靈活性**: 提供多種 fixtures 適應不同需求  
✅ **驗證能力**: 可以捕獲和驗證繪圖調用  
✅ **完整文檔**: 詳細的使用指南和範例  
✅ **無侵入性**: 不需要修改現有代碼  
✅ **效能**: 避免實際渲染，測試運行更快  

## 適用場景

### ✓ 應該使用的情況

1. 測試包含繪圖的函數
2. 驗證特定繪圖方法被調用
3. 防止測試時彈出視窗
4. CI/CD 環境中的自動化測試
5. 無頭（headless）伺服器環境

### ✗ 不需要使用的情況

1. 互動式開發和調試
2. 需要視覺確認結果的情況
3. 生成實際報告或圖表文件

## 現有專案整合

此模擬系統已經可以與現有的 AIMA-Python 測試無縫整合：

```python
# 測試 notebook.py 中的繪圖函數
def test_plot_NQueens(no_display):
    from notebook import plot_NQueens
    solution = [0, 4, 7, 5, 2, 6, 1, 3]
    plot_NQueens(solution)  # 不會彈出視窗

# 測試 notebook.py 中的熱圖函數
def test_heatmap(capture_plot_calls):
    from notebook import heatmap
    grid = [[1, 2], [3, 4]]
    
    with capture_plot_calls:
        heatmap(grid)
    
    assert capture_plot_calls.imshow_called
```

## 檔案結構

```
aima-python/
├── tests/
│   ├── conftest.py                    # ⭐ 核心配置
│   ├── test_mock_figures.py           # 📝 示例測試
│   ├── MOCK_FIGURES_README.md         # 📚 詳細文檔
│   ├── verify_mock.py                 # 🔍 驗證腳本
│   └── [其他測試檔案...]
├── MOCK_FIGURES_SETUP.md              # 本檔案
└── pytest.ini                         # pytest 配置
```

## 進階功能

### 自定義模擬行為

```python
@pytest.fixture
def custom_mock_plot():
    """自定義繪圖模擬"""
    with patch('matplotlib.pyplot.plot') as mock:
        mock.return_value = [Mock()]
        yield mock
```

### 臨時啟用實際顯示

```python
import matplotlib
matplotlib.use('TkAgg')  # 或其他互動式後端
```

### 儲存測試圖表用於調試

```python
def test_save_for_debug(tmp_path):
    plt.plot([1, 2, 3])
    plt.savefig(tmp_path / 'debug.png')
    # tmp_path 會自動清理
```

## 維護

### 添加新的繪圖函數模擬

1. 打開 `tests/conftest.py`
2. 在相應的 fixture 中添加新方法
3. 更新 `tests/MOCK_FIGURES_README.md` 文檔
4. 在 `tests/test_mock_figures.py` 中添加測試範例

### 更新文檔

如果有新的使用場景或最佳實踐，請更新：
- `tests/MOCK_FIGURES_README.md` - 使用指南
- `tests/test_mock_figures.py` - 測試範例

## 相關資源

- **pytest 官方文檔**: https://docs.pytest.org/
- **unittest.mock 指南**: https://docs.python.org/3/library/unittest.mock.html
- **matplotlib 後端說明**: https://matplotlib.org/stable/users/explain/backends.html
- **pytest fixtures**: https://docs.pytest.org/en/stable/fixture.html

## 貢獻

如果您發現問題或有改進建議：
1. 在 `tests/test_mock_figures.py` 中添加測試案例
2. 更新相應的文檔
3. 運行 `pytest tests/test_mock_figures.py` 確保測試通過

## 總結

✅ **完成事項**:
- [x] 創建核心配置檔案 (`conftest.py`)
- [x] 實作 5 個不同的 fixtures
- [x] 提供完整的測試範例
- [x] 編寫詳細的使用文檔
- [x] 創建驗證腳本
- [x] 編寫設置說明

🎯 **立即可用**:
- 所有測試將自動使用 Agg 後端
- `plt.show()` 自動被模擬
- 可以選擇性使用更進階的 fixtures

📝 **下一步**:
1. 安裝依賴: `pip install -r requirements.txt`
2. 運行測試: `pytest tests/test_mock_figures.py -v`
3. 閱讀文檔: `tests/MOCK_FIGURES_README.md`
4. 在您的測試中使用這些 fixtures

---

**問題或建議？** 請查看 `tests/MOCK_FIGURES_README.md` 的故障排除部分。


