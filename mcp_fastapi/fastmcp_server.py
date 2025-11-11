"""Run the AIMA tools as a FastMCP server."""

from __future__ import annotations

import os
from typing import Optional

from fastmcp import FastMCP

from app.schemas import (
    NQueensAlgorithm,
    NQueensRequest,
    RomaniaRouteRequest,
    RomaniaSearchAlgorithm,
)
from app.services import describe_result_as_text, solve_nqueens, solve_romania_route


app = FastMCP(
    description="AIMA Online MCP 伺服器，提供羅馬尼亞地圖搜尋與 N-Queens 求解。",
    instructions=(
        "使用工具 `romania_route` 計算城市路線，"
        "或 `nqueens` 求解 N 皇后問題。"
    ),
)


@app.tool(
    "romania_route",
    description="使用 AIMA 搜尋演算法計算羅馬尼亞城市間的最短路徑。",
)
def tool_romania_route(
    start: str,
    goal: str,
    algorithm: str = RomaniaSearchAlgorithm.uniform_cost.value,
) -> str:
    payload = RomaniaRouteRequest(
        start=start,
        goal=goal,
        algorithm=RomaniaSearchAlgorithm(algorithm),
    )
    result = solve_romania_route(payload)
    return describe_result_as_text(result)


@app.tool(
    "nqueens",
    description="使用 AIMA CSP 演算法解 N 皇后問題。",
)
def tool_nqueens(
    n: int = 8,
    algorithm: str = NQueensAlgorithm.backtracking.value,
    max_steps: Optional[int] = 1000,
) -> str:
    payload = NQueensRequest(
        n=n,
        algorithm=NQueensAlgorithm(algorithm),
        max_steps=max_steps,
    )
    result = solve_nqueens(payload)
    return describe_result_as_text(result)


def main() -> None:
    port = int(os.getenv("MCP_PORT", "3000"))
    host = os.getenv("MCP_HOST", "0.0.0.0")
    app.run(host=host, port=port)


if __name__ == "__main__":
    main()

