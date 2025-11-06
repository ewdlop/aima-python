"""
Pytest configuration and fixtures for AIMA tests.
包含 matplotlib 圖表模擬功能。
"""

import matplotlib
import matplotlib.pyplot as plt
import pytest
from unittest.mock import Mock, MagicMock, patch

# 設定 matplotlib 使用非互動式後端
matplotlib.use('Agg')


@pytest.fixture(autouse=True)
def mock_matplotlib_show():
    """
    自動模擬 plt.show()，防止在測試時顯示圖表視窗。
    此 fixture 會自動應用到所有測試。
    """
    with patch('matplotlib.pyplot.show'):
        yield


@pytest.fixture
def mock_figure():
    """
    提供一個模擬的 matplotlib Figure 物件。
    
    使用範例:
        def test_plotting(mock_figure):
            with patch('matplotlib.pyplot.figure', return_value=mock_figure):
                # 您的測試代碼
                pass
    """
    mock_fig = MagicMock(spec=plt.Figure)
    mock_ax = MagicMock()
    mock_fig.add_subplot.return_value = mock_ax
    mock_fig.add_axes.return_value = mock_ax
    mock_ax.plot.return_value = []
    mock_ax.imshow.return_value = None
    mock_ax.scatter.return_value = None
    mock_ax.axis.return_value = None
    return mock_fig


@pytest.fixture
def mock_plt():
    """
    提供完整的 matplotlib.pyplot 模擬物件。
    
    使用範例:
        def test_with_plotting(mock_plt):
            with patch('matplotlib.pyplot', mock_plt):
                # 您的測試代碼
                pass
    """
    mock_pyplot = MagicMock()
    mock_fig = MagicMock()
    mock_ax = MagicMock()
    
    # 設定常用的繪圖方法
    mock_pyplot.figure.return_value = mock_fig
    mock_pyplot.subplot.return_value = mock_ax
    mock_pyplot.subplots.return_value = (mock_fig, mock_ax)
    mock_fig.add_subplot.return_value = mock_ax
    mock_fig.add_axes.return_value = mock_ax
    
    # 模擬繪圖函數
    mock_pyplot.plot.return_value = []
    mock_pyplot.imshow.return_value = None
    mock_pyplot.scatter.return_value = None
    mock_pyplot.show.return_value = None
    mock_pyplot.savefig.return_value = None
    
    # 模擬設定函數
    mock_pyplot.xlabel.return_value = None
    mock_pyplot.ylabel.return_value = None
    mock_pyplot.title.return_value = None
    mock_pyplot.legend.return_value = None
    mock_pyplot.xlim.return_value = None
    mock_pyplot.ylim.return_value = None
    mock_pyplot.vlines.return_value = None
    mock_pyplot.hlines.return_value = None
    mock_pyplot.text.return_value = None
    mock_pyplot.tight_layout.return_value = None
    
    # 模擬 rcParams
    mock_pyplot.rcParams = {}
    mock_pyplot.rcParamsDefault = {}
    
    return mock_pyplot


@pytest.fixture
def capture_plot_calls():
    """
    捕獲並記錄繪圖調用，用於驗證測試。
    
    使用範例:
        def test_plot_behavior(capture_plot_calls):
            with capture_plot_calls:
                # 執行繪圖代碼
                plt.plot([1, 2, 3])
                plt.show()
            
            # 驗證調用
            assert capture_plot_calls.plot_called
            assert capture_plot_calls.show_called
    """
    class PlotCallCapture:
        def __init__(self):
            self.plot_called = False
            self.show_called = False
            self.figure_called = False
            self.imshow_called = False
            self.scatter_called = False
            self.savefig_called = False
            self.calls = []
            self._patches = []
        
        def __enter__(self):
            original_plot = plt.plot
            original_show = plt.show
            original_figure = plt.figure
            original_imshow = plt.imshow
            original_scatter = plt.scatter
            original_savefig = plt.savefig
            
            def track_plot(*args, **kwargs):
                self.plot_called = True
                self.calls.append(('plot', args, kwargs))
                return original_plot(*args, **kwargs) if original_plot else []
            
            def track_show(*args, **kwargs):
                self.show_called = True
                self.calls.append(('show', args, kwargs))
                # 不執行實際的 show
                pass
            
            def track_figure(*args, **kwargs):
                self.figure_called = True
                self.calls.append(('figure', args, kwargs))
                return original_figure(*args, **kwargs) if original_figure else MagicMock()
            
            def track_imshow(*args, **kwargs):
                self.imshow_called = True
                self.calls.append(('imshow', args, kwargs))
                return original_imshow(*args, **kwargs) if original_imshow else None
            
            def track_scatter(*args, **kwargs):
                self.scatter_called = True
                self.calls.append(('scatter', args, kwargs))
                return original_scatter(*args, **kwargs) if original_scatter else None
            
            def track_savefig(*args, **kwargs):
                self.savefig_called = True
                self.calls.append(('savefig', args, kwargs))
                # 不執行實際的 savefig
                pass
            
            self._patches.extend([
                patch('matplotlib.pyplot.plot', side_effect=track_plot),
                patch('matplotlib.pyplot.show', side_effect=track_show),
                patch('matplotlib.pyplot.figure', side_effect=track_figure),
                patch('matplotlib.pyplot.imshow', side_effect=track_imshow),
                patch('matplotlib.pyplot.scatter', side_effect=track_scatter),
                patch('matplotlib.pyplot.savefig', side_effect=track_savefig),
            ])
            
            for p in self._patches:
                p.__enter__()
            
            return self
        
        def __exit__(self, *args):
            for p in reversed(self._patches):
                p.__exit__(*args)
        
        def reset(self):
            """重置所有捕獲的狀態"""
            self.plot_called = False
            self.show_called = False
            self.figure_called = False
            self.imshow_called = False
            self.scatter_called = False
            self.savefig_called = False
            self.calls = []
    
    return PlotCallCapture()


@pytest.fixture
def no_display():
    """
    完全禁用所有顯示和繪圖操作的 fixture。
    適用於不需要驗證繪圖行為，只需要防止視窗彈出的測試。
    """
    with patch('matplotlib.pyplot.show'), \
         patch('matplotlib.pyplot.savefig'), \
         patch('IPython.display.display'):
        yield


