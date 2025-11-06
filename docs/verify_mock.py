#!/usr/bin/env python
"""
簡單的驗證腳本，用於測試 matplotlib 模擬功能。
這個腳本不需要 pytest 就能運行。
"""

import sys
import os

# 添加父目錄到路徑
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# 設定非互動式後端
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from unittest.mock import patch, MagicMock
import numpy as np

print("=" * 60)
print("測試 1: 基本繪圖（使用 Agg 後端）")
print("=" * 60)

try:
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [1, 4, 9])
    with patch('matplotlib.pyplot.show'):
        plt.show()  # 被模擬，不會顯示
    plt.close()
    print("✓ 基本繪圖測試通過")
except Exception as e:
    print(f"✗ 基本繪圖測試失敗: {e}")

print("\n" + "=" * 60)
print("測試 2: 模擬 plt.show()")
print("=" * 60)

try:
    show_called = False
    
    def mock_show():
        global show_called
        show_called = True
    
    with patch('matplotlib.pyplot.show', side_effect=mock_show):
        plt.plot([1, 2, 3])
        plt.show()
    
    assert show_called, "show() 應該被調用"
    print("✓ plt.show() 模擬測試通過")
except Exception as e:
    print(f"✗ plt.show() 模擬測試失敗: {e}")

print("\n" + "=" * 60)
print("測試 3: 模擬 Figure 物件")
print("=" * 60)

try:
    mock_fig = MagicMock(spec=plt.Figure)
    mock_ax = MagicMock()
    mock_fig.add_subplot.return_value = mock_ax
    
    with patch('matplotlib.pyplot.figure', return_value=mock_fig):
        fig = plt.figure(figsize=(10, 5))
        ax = fig.add_subplot(111)
        ax.plot([1, 2, 3])
        
        assert mock_fig.add_subplot.called, "add_subplot 應該被調用"
        assert ax.plot.called, "plot 應該被調用"
    
    print("✓ Figure 物件模擬測試通過")
except Exception as e:
    print(f"✗ Figure 物件模擬測試失敗: {e}")

print("\n" + "=" * 60)
print("測試 4: 捕獲繪圖調用")
print("=" * 60)

try:
    calls = []
    
    def track_plot(*args, **kwargs):
        calls.append(('plot', args, kwargs))
        return []
    
    def track_show(*args, **kwargs):
        calls.append(('show', args, kwargs))
    
    with patch('matplotlib.pyplot.plot', side_effect=track_plot), \
         patch('matplotlib.pyplot.show', side_effect=track_show):
        plt.plot([1, 2, 3], [4, 5, 6])
        plt.show()
    
    assert len(calls) == 2, f"應該有 2 個調用，但有 {len(calls)} 個"
    assert calls[0][0] == 'plot', "第一個調用應該是 plot"
    assert calls[1][0] == 'show', "第二個調用應該是 show"
    
    print(f"✓ 捕獲到 {len(calls)} 個調用:")
    for call_name, args, kwargs in calls:
        print(f"  - {call_name}() 被調用")
except Exception as e:
    print(f"✗ 捕獲繪圖調用測試失敗: {e}")

print("\n" + "=" * 60)
print("測試 5: 複雜繪圖場景")
print("=" * 60)

try:
    with patch('matplotlib.pyplot.show'):
        # 創建多個圖表
        fig1, ax1 = plt.subplots()
        ax1.plot([1, 2, 3], [1, 4, 9])
        ax1.set_title('圖表 1')
        
        fig2, (ax2, ax3) = plt.subplots(1, 2, figsize=(10, 5))
        ax2.scatter([1, 2, 3], [3, 2, 1])
        ax3.bar([1, 2, 3], [3, 5, 2])
        
        plt.show()
        plt.close('all')
    
    print("✓ 複雜繪圖場景測試通過")
except Exception as e:
    print(f"✗ 複雜繪圖場景測試失敗: {e}")

print("\n" + "=" * 60)
print("測試 6: 熱圖繪製")
print("=" * 60)

try:
    imshow_called = False
    
    def track_imshow(*args, **kwargs):
        global imshow_called
        imshow_called = True
        return None
    
    with patch('matplotlib.pyplot.imshow', side_effect=track_imshow), \
         patch('matplotlib.pyplot.show'):
        data = np.random.rand(5, 5)
        plt.imshow(data, cmap='viridis')
        plt.show()
    
    assert imshow_called, "imshow 應該被調用"
    print("✓ 熱圖繪製測試通過")
except Exception as e:
    print(f"✗ 熱圖繪製測試失敗: {e}")

print("\n" + "=" * 60)
print("測試 7: conftest.py 導入測試")
print("=" * 60)

try:
    # 嘗試導入 conftest 模組
    from conftest import mock_matplotlib_show
    print("✓ conftest.py 成功導入")
    print(f"  可用的 fixtures:")
    
    # 列出可用的 fixtures
    import conftest
    fixtures = [name for name in dir(conftest) if not name.startswith('_')]
    for fixture in fixtures:
        obj = getattr(conftest, fixture)
        if hasattr(obj, '_pytestfixturefunction'):
            print(f"    - {fixture}")
    
except Exception as e:
    print(f"✗ conftest.py 導入測試失敗: {e}")

print("\n" + "=" * 60)
print("所有測試完成！")
print("=" * 60)
print("\n建議:")
print("1. 安裝 pytest 以運行完整測試套件: pip install pytest pytest-cov")
print("2. 運行完整測試: pytest tests/test_mock_figures.py -v")
print("3. 查看文檔: tests/MOCK_FIGURES_README.md")


