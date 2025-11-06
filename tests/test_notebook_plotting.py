"""
測試 notebook.py 和 notebook4e.py 中的繪圖函數。
展示如何將圖表模擬應用到現有的 AIMA-Python 代碼。
"""

import sys
import os
import pytest
from unittest.mock import patch, Mock, MagicMock
import numpy as np

# 添加父目錄到路徑以導入模組
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class TestNotebookPlotting:
    """測試 notebook.py 中的繪圖函數"""
    
    def test_plot_NQueens_with_dict_solution(self, no_display):
        """測試 plot_NQueens 函數（字典解）"""
        try:
            from notebook import plot_NQueens
            
            # NQueensCSP 返回字典解
            solution = {0: 0, 1: 4, 2: 7, 3: 5, 4: 2, 5: 6, 6: 1, 7: 3}
            
            # Mock Image.open 以避免載入實際圖片
            with patch('notebook.Image.open') as mock_open:
                mock_img = Mock()
                mock_img.size = (100, 100)
                mock_img.__array__ = Mock(return_value=np.zeros((100, 100, 4)))
                mock_open.return_value = mock_img
                
                # 執行函數（不會彈出視窗）
                plot_NQueens(solution)
                
        except ImportError:
            pytest.skip("無法導入 notebook 模組")
    
    def test_plot_NQueens_with_list_solution(self, no_display):
        """測試 plot_NQueens 函數（列表解）"""
        try:
            from notebook import plot_NQueens
            
            # NQueensProblem 返回列表解
            solution = [0, 4, 7, 5, 2, 6, 1, 3]
            
            with patch('notebook.Image.open') as mock_open:
                mock_img = Mock()
                mock_img.size = (100, 100)
                mock_img.__array__ = Mock(return_value=np.zeros((100, 100, 4)))
                mock_open.return_value = mock_img
                
                plot_NQueens(solution)
                
        except ImportError:
            pytest.skip("無法導入 notebook 模組")
    
    def test_heatmap_function(self, capture_plot_calls):
        """測試 heatmap 函數"""
        try:
            from notebook import heatmap
            
            with capture_plot_calls:
                # 創建簡單的網格
                grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
                heatmap(grid)
            
            # 驗證 imshow 被調用（熱圖的核心函數）
            assert capture_plot_calls.imshow_called
            
        except ImportError:
            pytest.skip("無法導入 notebook 模組")
    
    def test_show_iris(self, capture_plot_calls):
        """測試 show_iris 3D 繪圖函數"""
        try:
            from notebook import show_iris
            
            with capture_plot_calls:
                # 使用預設參數
                show_iris(i=0, j=1, k=2)
            
            # 驗證顯示被調用
            assert capture_plot_calls.show_called
            
        except ImportError:
            pytest.skip("無法導入 notebook 模組或資料")
        except Exception as e:
            # 如果資料檔案不存在，跳過測試
            if "iris" in str(e).lower():
                pytest.skip(f"Iris 資料集不可用: {e}")
            raise


class TestNotebook4ePlotting:
    """測試 notebook4e.py 中的繪圖函數"""
    
    def test_plot_NQueens_4e(self, no_display):
        """測試 notebook4e.py 中的 plot_NQueens"""
        try:
            from notebook4e import plot_NQueens
            
            solution = [0, 4, 7, 5, 2, 6, 1, 3]
            
            with patch('notebook4e.Image.open') as mock_open:
                mock_img = Mock()
                mock_img.size = (100, 100)
                mock_img.__array__ = Mock(return_value=np.zeros((100, 100, 4)))
                mock_open.return_value = mock_img
                
                plot_NQueens(solution)
                
        except ImportError:
            pytest.skip("無法導入 notebook4e 模組")
    
    def test_heatmap_4e(self, capture_plot_calls):
        """測試 notebook4e.py 中的 heatmap"""
        try:
            from notebook4e import heatmap
            
            with capture_plot_calls:
                grid = np.array([[1, 2], [3, 4]])
                heatmap(grid)
            
            assert capture_plot_calls.imshow_called
            
        except ImportError:
            pytest.skip("無法導入 notebook4e 模組")


class TestGuiPlotting:
    """測試 gui/ 目錄中的繪圖函數"""
    
    def test_grid_mdp_display(self, no_display):
        """測試 gui/grid_mdp.py 中的顯示函數"""
        try:
            # 這個測試需要 tkinter，可能在某些環境中不可用
            import gui.grid_mdp
            pytest.skip("GUI 測試需要完整的圖形環境")
        except ImportError:
            pytest.skip("無法導入 gui.grid_mdp 模組")


class TestIntegrationScenarios:
    """集成場景測試"""
    
    def test_multiple_plotting_calls(self, capture_plot_calls):
        """測試多個繪圖函數的連續調用"""
        import matplotlib.pyplot as plt
        
        with capture_plot_calls:
            # 場景：創建多個不同類型的圖表
            
            # 1. 線圖
            plt.figure()
            plt.plot([1, 2, 3], [1, 4, 9])
            
            # 2. 散點圖
            plt.figure()
            plt.scatter([1, 2, 3], [3, 2, 1])
            
            # 3. 熱圖
            plt.figure()
            plt.imshow(np.random.rand(5, 5))
            
            plt.show()
        
        # 驗證所有類型的繪圖都被調用
        assert capture_plot_calls.figure_called
        assert capture_plot_calls.plot_called
        assert capture_plot_calls.scatter_called
        assert capture_plot_calls.imshow_called
        assert capture_plot_calls.show_called
    
    def test_notebook_workflow(self, no_display):
        """模擬 Jupyter notebook 中的典型工作流程"""
        import matplotlib.pyplot as plt
        
        # 1. 創建資料
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        
        # 2. 繪製圖表
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(x, y, label='sin(x)')
        ax.set_xlabel('X')
        ax.set_ylabel('Y')
        ax.set_title('正弦函數')
        ax.legend()
        ax.grid(True)
        
        # 3. 顯示（被自動模擬）
        plt.show()
        
        # 4. 清理
        plt.close(fig)
        
        # 測試通過，沒有視窗彈出


class TestEdgeCases:
    """邊界情況測試"""
    
    def test_empty_plot(self, no_display):
        """測試空繪圖"""
        import matplotlib.pyplot as plt
        
        plt.figure()
        plt.show()
        plt.close()
    
    def test_plot_without_show(self, capture_plot_calls):
        """測試沒有調用 show() 的繪圖"""
        import matplotlib.pyplot as plt
        
        with capture_plot_calls:
            plt.plot([1, 2, 3])
            # 沒有調用 plt.show()
        
        assert capture_plot_calls.plot_called
        assert not capture_plot_calls.show_called
    
    def test_savefig_without_show(self, capture_plot_calls, tmp_path):
        """測試儲存圖表但不顯示"""
        import matplotlib.pyplot as plt
        
        with capture_plot_calls:
            plt.plot([1, 2, 3])
            plt.savefig(tmp_path / 'test.png')
        
        assert capture_plot_calls.plot_called
        assert capture_plot_calls.savefig_called
        assert not capture_plot_calls.show_called
    
    def test_multiple_shows(self, capture_plot_calls):
        """測試多次調用 show()"""
        import matplotlib.pyplot as plt
        
        with capture_plot_calls:
            plt.plot([1, 2, 3])
            plt.show()
            plt.plot([4, 5, 6])
            plt.show()
        
        # 檢查 show() 被調用兩次
        show_calls = [c for c in capture_plot_calls.calls if c[0] == 'show']
        assert len(show_calls) == 2


class TestPerformance:
    """效能相關測試"""
    
    def test_many_plots(self, no_display):
        """測試大量繪圖操作的效能"""
        import matplotlib.pyplot as plt
        import time
        
        start = time.time()
        
        for i in range(50):
            fig = plt.figure()
            plt.plot(range(100))
            plt.close(fig)
        
        elapsed = time.time() - start
        
        # 使用模擬後端應該很快（< 5 秒）
        assert elapsed < 5.0, f"50 個圖表花費 {elapsed:.2f} 秒（太慢）"
    
    def test_large_dataset(self, no_display):
        """測試大型資料集繪圖"""
        import matplotlib.pyplot as plt
        
        # 創建大型資料集
        x = np.linspace(0, 100, 10000)
        y = np.sin(x) * np.exp(-x / 10)
        
        plt.figure()
        plt.plot(x, y)
        plt.show()
        plt.close()
        
        # 測試通過，沒有記憶體問題


# 用於手動驗證的輔助函數
def manual_test_all():
    """
    手動運行所有測試的輔助函數。
    用法: python tests/test_notebook_plotting.py
    """
    print("=" * 60)
    print("手動測試模式")
    print("=" * 60)
    
    import matplotlib
    matplotlib.use('Agg')
    
    from unittest.mock import patch
    
    print("\n1. 測試基本繪圖...")
    with patch('matplotlib.pyplot.show'):
        import matplotlib.pyplot as plt
        plt.plot([1, 2, 3])
        plt.show()
    print("✓ 通過")
    
    print("\n2. 測試熱圖...")
    with patch('matplotlib.pyplot.show'):
        plt.imshow([[1, 2], [3, 4]])
        plt.show()
    print("✓ 通過")
    
    print("\n所有手動測試完成！")


if __name__ == '__main__':
    # 如果直接運行此檔案，執行手動測試
    manual_test_all()


