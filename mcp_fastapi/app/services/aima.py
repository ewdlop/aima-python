"""Service helpers that wrap selected AIMA algorithms."""

from __future__ import annotations

import json
import sys
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path
from typing import Any, Callable

from ..schemas import (
    NQueensRequest,
    NQueensResponse,
    RomaniaRouteRequest,
    RomaniaRouteResponse,
    RomaniaSearchAlgorithm,
)

PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

try:  # pragma: no cover - import validation
    import search  # type: ignore
    import csp  # type: ignore
except ModuleNotFoundError as exc:  # pragma: no cover
    raise RuntimeError("無法匯入 AIMA 模組，請確認專案根目錄設定。") from exc

ROMANIA_CITIES: tuple[str, ...] = tuple(sorted(search.romania_map.locations.keys()))


@dataclass
class SearchSummary:
    path: list[str]
    actions: list[str]
    cost: float
    explored_steps: int


def _validate_romania_city(name: str) -> None:
    """Ensure the provided city exists inside the Romania map."""
    if name not in search.romania_map.locations:
        raise ValueError(f"城市名稱無效：{name}")


def _run_search(
    problem: search.GraphProblem,
    algorithm: RomaniaSearchAlgorithm,
) -> SearchSummary:
    """Execute a search algorithm from the AIMA toolkit."""
    algorithm_table: dict[RomaniaSearchAlgorithm, Callable[[search.GraphProblem], Any]] = {
        RomaniaSearchAlgorithm.uniform_cost: search.uniform_cost_search,
        RomaniaSearchAlgorithm.breadth_first: search.breadth_first_graph_search,
        RomaniaSearchAlgorithm.astar: search.astar_search,
    }

    solver = algorithm_table[algorithm]
    result = solver(problem)
    if result is None:
        raise RuntimeError("搜尋失敗，未找到任何路徑。")

    node_path = result.path()
    path_states = [node.state for node in node_path]
    actions = result.solution()

    return SearchSummary(
        path=path_states,
        actions=actions,
        cost=result.path_cost,
        explored_steps=len(node_path) - 1,
    )


def solve_romania_route(payload: RomaniaRouteRequest) -> RomaniaRouteResponse:
    """Solve a pathfinding query on the Romania map."""
    _validate_romania_city(payload.start)
    _validate_romania_city(payload.goal)

    problem = search.GraphProblem(payload.start, payload.goal, search.romania_map)
    summary = _run_search(problem, payload.algorithm)

    return RomaniaRouteResponse(
        start=payload.start,
        goal=payload.goal,
        algorithm=payload.algorithm,
        path=summary.path,
        actions=summary.actions,
        total_cost=summary.cost,
        explored_steps=summary.explored_steps,
    )


@lru_cache
def _get_nqueens_solver(algorithm: str) -> Callable[..., Any]:
    """Return cached solver callable based on the algorithm name."""
    if algorithm == "backtracking":
        return csp.backtracking_search
    if algorithm == "min_conflicts":
        return csp.min_conflicts
    raise ValueError(f"未知的 N-Queens 演算法：{algorithm}")


def solve_nqueens(payload: NQueensRequest) -> NQueensResponse:
    """Solve the N-Queens problem using the requested algorithm."""
    problem = csp.NQueensCSP(payload.n)

    solver = _get_nqueens_solver(payload.algorithm.value)
    if payload.algorithm.value == "min_conflicts":
        if payload.max_steps is None:
            raise ValueError("使用 min_conflicts 時必須提供 max_steps。")
        assignment = solver(problem, max_steps=payload.max_steps)
    else:
        assignment = solver(problem)

    if assignment is None:
        raise RuntimeError("未能找到任何 N-Queens 解。")

    # backtracking_search returns dict, min_conflicts returns dict as well.
    ordered = [assignment[col] for col in sorted(assignment.keys())]

    return NQueensResponse(
        n=payload.n,
        algorithm=payload.algorithm,
        assignments=ordered,
        is_solution=problem.goal_test(assignment),
        raw=assignment,
    )


def describe_result_as_text(result: RomaniaRouteResponse | NQueensResponse) -> str:
    """Convert service results to a human-readable Traditional Chinese message."""
    if isinstance(result, RomaniaRouteResponse):
        details = json.dumps(result.dict(), ensure_ascii=False, indent=2)
        return (
            f"羅馬尼亞路線規劃完成：{result.start} → {result.goal}\n"
            f"使用演算法：{result.algorithm.value}\n"
            f"總成本：{result.total_cost}\n"
            f"經過節點：{' → '.join(result.path)}\n"
            f"JSON 詳細資料：\n{details}"
        )

    if isinstance(result, NQueensResponse):
        board_rows = ", ".join(str(pos) for pos in result.assignments)
        details = json.dumps(result.dict(), ensure_ascii=False, indent=2)
        return (
            f"N-Queens 求解成功：N = {result.n}\n"
            f"演算法：{result.algorithm.value}\n"
            f"各列位置（從 0 起算）：{board_rows}\n"
            f"JSON 詳細資料：\n{details}"
        )

    raise TypeError("不支援的結果型別。")

