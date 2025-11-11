"""Gradio UI for interacting with AIMA services."""

from __future__ import annotations

import gradio as gr

from .schemas import (
    NQueensAlgorithm,
    NQueensRequest,
    RomaniaRouteRequest,
    RomaniaSearchAlgorithm,
)
from .services import ROMANIA_CITIES, describe_result_as_text, solve_nqueens, solve_romania_route


def _romania_callback(start: str, goal: str, algorithm: str) -> str:
    try:
        request = RomaniaRouteRequest(
            start=start,
            goal=goal,
            algorithm=RomaniaSearchAlgorithm(algorithm),
        )
        result = solve_romania_route(request)
        return describe_result_as_text(result)
    except Exception as exc:  # noqa: broad-except - 向使用者顯示錯誤
        return f"❌ 計算失敗：{exc}"


def _nqueens_callback(n: int, algorithm: str, max_steps: int | None) -> str:
    try:
        request = NQueensRequest(
            n=n,
            algorithm=NQueensAlgorithm(algorithm),
            max_steps=max_steps,
        )
        result = solve_nqueens(request)
        return describe_result_as_text(result)
    except Exception as exc:  # noqa: broad-except - 向使用者顯示錯誤
        return f"❌ 求解失敗：{exc}"


def build_gradio_app() -> gr.Blocks:
    """Create and return the Gradio Blocks interface."""
    romania_options = sorted(ROMANIA_CITIES)
    algorithm_options = [(alg.value, alg.value) for alg in RomaniaSearchAlgorithm]
    nqueens_algorithms = [(alg.value, alg.value) for alg in NQueensAlgorithm]

    with gr.Blocks(title="AIMA Online Demo") as demo:
        gr.Markdown(
            """
            # AIMA Online Demo
            使用下方介面呼叫 AIMA 套件演算法，結果也會同步於 FastAPI 與 FastMCP 的服務邏輯。
            """
        )

        with gr.Tab("羅馬尼亞路線搜尋"):
            gr.Markdown("選擇起點與終點城市，並指定搜尋演算法。")
            with gr.Row():
                start = gr.Dropdown(romania_options, value="Arad", label="起點城市")
                goal = gr.Dropdown(romania_options, value="Bucharest", label="終點城市")
            algorithm = gr.Radio(
                algorithm_options,
                value=RomaniaSearchAlgorithm.uniform_cost.value,
                label="搜尋演算法",
            )
            romania_button = gr.Button("開始搜尋")
            romania_output = gr.Textbox(
                label="搜尋結果",
                lines=12,
                interactive=False,
            )
            romania_button.click(
                fn=_romania_callback,
                inputs=[start, goal, algorithm],
                outputs=romania_output,
            )

        with gr.Tab("N 皇后問題"):
            gr.Markdown("設定棋盤大小與演算法，取得每一列的皇后位置。")
            n_value = gr.Slider(4, 25, value=8, step=1, label="棋盤大小 N")
            n_algorithm = gr.Radio(
                nqueens_algorithms,
                value=NQueensAlgorithm.backtracking.value,
                label="演算法",
            )
            n_max_steps = gr.Number(
                value=1000,
                label="Max Steps（min_conflicts 使用）",
            )
            nqueens_button = gr.Button("求解 N 皇后")
            nqueens_output = gr.Textbox(
                label="求解結果",
                lines=12,
                interactive=False,
            )
            nqueens_button.click(
                fn=_nqueens_callback,
                inputs=[n_value, n_algorithm, n_max_steps],
                outputs=nqueens_output,
            )

        gr.Markdown("➡️ 亦可透過 `/gradio` 路徑直接存取此介面。")

    return demo

