"""
測試 matplotlib 圖表模擬功能的示例測試。
展示如何在測試中使用各種圖表模擬 fixtures。
"""

import matplotlib.pyplot as plt
import numpy as np
from unittest.mock import patch


def test_auto_mock_show():
    """
    測試自動模擬 plt.show()。
    由於 mock_matplotlib_show fixture 設定為 autouse=True，
    所有測試都會自動模擬 show()，不會彈出視窗。
    """
    fig, ax = plt.subplots()
    ax.plot([1, 2, 3], [1, 4, 9])
    plt.show()  # 不會彈出視窗
    plt.close()
    # 測試通過，沒有彈出視窗


def test_with_mock_figure(mock_figure):
    """測試使用 mock_figure fixture"""
    with patch('matplotlib.pyplot.figure', return_value=mock_figure):
        fig = plt.figure(figsize=(10, 5))
        ax = fig.add_subplot(111)
        ax.plot([1, 2, 3], [1, 2, 3])
        
        # 驗證方法被調用
        assert mock_figure.add_subplot.called
        assert ax.plot.called


def test_with_mock_plt(mock_plt):
    """測試使用完整的 mock_plt fixture"""
    with patch.dict('sys.modules', {'matplotlib.pyplot': mock_plt}):
        # 模擬繪圖操作
        mock_plt.figure()
        mock_plt.plot([1, 2, 3])
        mock_plt.xlabel('X軸')
        mock_plt.ylabel('Y軸')
        mock_plt.show()
        
        # 驗證調用
        assert mock_plt.figure.called
        assert mock_plt.plot.called
        assert mock_plt.show.called


def test_capture_plot_calls(capture_plot_calls):
    """測試捕獲繪圖調用"""
    with capture_plot_calls:
        plt.figure()
        plt.plot([1, 2, 3], [4, 5, 6])
        plt.imshow(np.random.rand(10, 10))
        plt.show()
    
    # 驗證各種調用
    assert capture_plot_calls.figure_called
    assert capture_plot_calls.plot_called
    assert capture_plot_calls.imshow_called
    assert capture_plot_calls.show_called
    
    # 檢查調用歷史
    assert len(capture_plot_calls.calls) == 4
    assert capture_plot_calls.calls[0][0] == 'figure'
    assert capture_plot_calls.calls[1][0] == 'plot'
    assert capture_plot_calls.calls[2][0] == 'imshow'
    assert capture_plot_calls.calls[3][0] == 'show'


def test_no_display_fixture(no_display):
    """測試 no_display fixture"""
    # 所有顯示操作都被模擬
    plt.plot([1, 2, 3])
    plt.show()  # 不會顯示
    plt.savefig('test.png')  # 不會儲存
    # 沒有錯誤拋出


def test_multiple_plots():
    """測試多個圖表的創建（自動模擬 show）"""
    # 第一個圖表
    fig1, ax1 = plt.subplots()
    ax1.plot([1, 2, 3], [1, 4, 9])
    ax1.set_title('圖表 1')
    plt.close(fig1)
    
    # 第二個圖表
    fig2, ax2 = plt.subplots()
    ax2.scatter([1, 2, 3], [3, 2, 1])
    ax2.set_title('圖表 2')
    plt.close(fig2)
    
    # 測試通過


def test_complex_plotting_scenario(capture_plot_calls):
    """測試複雜的繪圖場景"""
    with capture_plot_calls:
        # 創建子圖
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
        
        # 第一個子圖
        x = np.linspace(0, 10, 100)
        ax1.plot(x, np.sin(x))
        ax1.set_xlabel('X')
        ax1.set_ylabel('sin(x)')
        
        # 第二個子圖
        ax2.scatter(x, np.cos(x))
        ax2.set_xlabel('X')
        ax2.set_ylabel('cos(x)')
        
        plt.tight_layout()
        plt.show()
    
    # 驗證
    assert capture_plot_calls.show_called
    assert len(capture_plot_calls.calls) > 0


def test_heatmap_plotting(capture_plot_calls):
    """測試熱圖繪製"""
    with capture_plot_calls:
        data = np.random.rand(10, 10)
        plt.figure(figsize=(8, 6))
        plt.imshow(data, cmap='viridis', interpolation='nearest')
        plt.colorbar()
        plt.title('熱圖示例')
        plt.show()
    
    assert capture_plot_calls.figure_called
    assert capture_plot_calls.imshow_called
    assert capture_plot_calls.show_called


def test_3d_plotting():
    """測試 3D 繪圖（自動模擬）"""
    from mpl_toolkits.mplot3d import Axes3D
    
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x, y)
    Z = np.sin(np.sqrt(X**2 + Y**2))
    
    ax.plot_surface(X, Y, Z, cmap='coolwarm')
    plt.show()
    plt.close()
    
    # 測試通過，沒有顯示視窗



