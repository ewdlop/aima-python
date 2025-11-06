# 📑 Matplotlib 模擬系統 - 檔案索引

## 🚀 從這裡開始

### 初次使用？（建議順序）

1. **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** ⏱️ 5 分鐘
   - 快速上手指南
   - 最常用的範例
   - 速查表

2. **[test_mock_figures.py](test_mock_figures.py)** ⏱️ 10 分鐘
   - 10 個實用測試範例
   - 可以直接運行
   - 涵蓋所有基本場景

3. **開始寫測試！** 🎉

### 需要更多資訊？

4. **[MOCK_FIGURES_README.md](MOCK_FIGURES_README.md)** ⏱️ 20 分鐘
   - 完整的使用指南
   - 所有 fixtures 的詳細說明
   - 故障排除

5. **[test_notebook_plotting.py](test_notebook_plotting.py)** ⏱️ 15 分鐘
   - 實際專案集成範例
   - 測試現有代碼
   - 進階技巧

---

## 📚 完整檔案列表

### 核心檔案

| 檔案 | 類型 | 說明 | 必讀 |
|------|------|------|------|
| **conftest.py** | 代碼 | Pytest 配置和所有 fixtures | ⭐⭐⭐ |

### 測試範例

| 檔案 | 說明 | 測試數量 | 難度 |
|------|------|----------|------|
| **test_mock_figures.py** | 基礎測試範例 | 10 | ⭐ |
| **test_notebook_plotting.py** | 集成測試範例 | 20+ | ⭐⭐ |

### 文檔

| 檔案 | 類型 | 長度 | 用途 |
|------|------|------|------|
| **QUICK_REFERENCE.md** | 快速參考 | 短 | 日常使用 |
| **README_MOCKING.md** | 總覽 | 中 | 了解系統 |
| **MOCK_FIGURES_README.md** | 完整指南 | 長 | 深入學習 |
| **INDEX.md** | 索引 | 短 | 本檔案 |

### 工具

| 檔案 | 說明 | 用途 |
|------|------|------|
| **verify_mock.py** | 驗證腳本 | 測試設置是否正確 |

### 設置說明

| 檔案 | 位置 | 說明 |
|------|------|------|
| **MOCK_FIGURES_SETUP.md** | 根目錄 | 完整的設置說明 |

---

## 🎯 根據需求選擇

### 我想...

#### 快速開始寫測試
➡️ `QUICK_REFERENCE.md` → 開始寫代碼

#### 學習所有功能
➡️ `MOCK_FIGURES_README.md` → `test_mock_figures.py`

#### 測試現有的繪圖函數
➡️ `test_notebook_plotting.py` → 參考範例

#### 了解實作細節
➡️ `conftest.py` → 研究代碼

#### 驗證設置
➡️ 運行 `verify_mock.py`

#### 解決問題
➡️ `MOCK_FIGURES_README.md` 的故障排除部分

---

## 📖 閱讀路徑

### 🎓 新手路徑（30 分鐘）

```
QUICK_REFERENCE.md
    ↓
test_mock_figures.py (前 3 個測試)
    ↓
開始寫測試
    ↓
遇到問題時查閱 MOCK_FIGURES_README.md
```

### 🔧 進階路徑（1 小時）

```
README_MOCKING.md
    ↓
MOCK_FIGURES_README.md (完整閱讀)
    ↓
test_mock_figures.py (所有測試)
    ↓
test_notebook_plotting.py
    ↓
conftest.py (研究實作)
```

### 🚀 專家路徑（2 小時）

```
研究所有檔案
    ↓
理解實作細節
    ↓
自定義 fixtures
    ↓
貢獻改進
```

---

## 🔍 快速搜尋

### 我需要找...

| 需求 | 檔案 | 章節 |
|------|------|------|
| 最簡單的範例 | QUICK_REFERENCE.md | 快速開始 |
| 所有 fixtures 列表 | README_MOCKING.md | 五個 Fixtures |
| capture_plot_calls 用法 | MOCK_FIGURES_README.md | Fixture 4 |
| 測試熱圖 | test_mock_figures.py | test_heatmap_plotting |
| 測試現有函數 | test_notebook_plotting.py | TestNotebookPlotting |
| 驗證設置 | verify_mock.py | 運行腳本 |
| 故障排除 | MOCK_FIGURES_README.md | 故障排除 |
| 效能資訊 | README_MOCKING.md | 效能比較 |

---

## 📊 檔案關係圖

```
┌─────────────────────────────────────────────┐
│         MOCK_FIGURES_SETUP.md               │
│         (根目錄 - 總體設置說明)              │
└─────────────────────────────────────────────┘
                      │
                      ↓
┌─────────────────────────────────────────────┐
│              tests/ 目錄                     │
└─────────────────────────────────────────────┘
                      │
        ┌─────────────┼─────────────┐
        ↓             ↓             ↓
   [核心代碼]      [測試]        [文檔]
        │             │             │
        ↓             ↓             ↓
  conftest.py   test_*.py    README*.md
                      │             │
                      ↓             ↓
              verify_mock.py   INDEX.md
```

---

## 🎯 常見任務速查

### 任務 1: 寫第一個測試

```python
# 參考: QUICK_REFERENCE.md
def test_my_plot():
    plt.plot([1, 2, 3])
    plt.show()
```

### 任務 2: 驗證繪圖調用

```python
# 參考: test_mock_figures.py::test_capture_plot_calls
def test(capture_plot_calls):
    with capture_plot_calls:
        my_function()
    assert capture_plot_calls.plot_called
```

### 任務 3: 測試現有函數

```python
# 參考: test_notebook_plotting.py::TestNotebookPlotting
def test(no_display):
    from notebook import my_plot_function
    my_plot_function()
```

### 任務 4: 檢查設置

```bash
# 參考: verify_mock.py
python tests/verify_mock.py
```

---

## 💡 提示

### 📌 收藏這些檔案

**日常使用**:
- `QUICK_REFERENCE.md` - 最常用

**深入學習**:
- `MOCK_FIGURES_README.md` - 最詳細

**參考範例**:
- `test_mock_figures.py` - 最實用

### 🔖 書籤建議

1. **新手**: QUICK_REFERENCE.md
2. **開發者**: test_mock_figures.py
3. **維護者**: conftest.py

---

## 📞 獲取幫助

### 方法 1: 查閱文檔

```
問題 → QUICK_REFERENCE.md → MOCK_FIGURES_README.md
```

### 方法 2: 查看範例

```
需求 → test_mock_figures.py → test_notebook_plotting.py
```

### 方法 3: 驗證設置

```
問題 → 運行 verify_mock.py → 查看輸出
```

### 方法 4: 研究代碼

```
深入 → conftest.py → 理解實作
```

---

## ✅ 檢查清單

### 初次設置

- [ ] 閱讀 `QUICK_REFERENCE.md`
- [ ] 運行 `pytest tests/test_mock_figures.py`
- [ ] 查看測試範例
- [ ] 寫第一個測試

### 日常使用

- [ ] 需要驗證時使用 `capture_plot_calls`
- [ ] 簡單測試讓自動模擬處理
- [ ] 使用 `plt.close()` 清理資源
- [ ] 保持測試獨立

### 深入學習

- [ ] 完整閱讀 `MOCK_FIGURES_README.md`
- [ ] 研究所有測試範例
- [ ] 理解 `conftest.py` 實作
- [ ] 嘗試自定義 fixtures

---

## 🎉 開始使用

### 最快上手（2 步驟）

1. **閱讀**: `QUICK_REFERENCE.md` (5 分鐘)
2. **實踐**: 寫一個測試並運行

### 完整學習（3 步驟）

1. **概覽**: `README_MOCKING.md` (10 分鐘)
2. **詳細**: `MOCK_FIGURES_README.md` (20 分鐘)
3. **範例**: `test_mock_figures.py` + `test_notebook_plotting.py` (20 分鐘)

---

## 🔄 更新日誌

### 版本 1.0 (2025-11-06)

- ✅ 創建完整的模擬系統
- ✅ 5 個 fixtures
- ✅ 30+ 測試範例
- ✅ 完整文檔
- ✅ 驗證工具

---

**準備好了嗎？** 從 [QUICK_REFERENCE.md](QUICK_REFERENCE.md) 開始！🚀


