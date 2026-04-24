"""Expose selected AIMA algorithms as HTTP APIs."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.concurrency import run_in_threadpool

from ..schemas import (
    NQueensAlgorithm,
    NQueensCatalogResponse,
    NQueensRequest,
    NQueensResponse,
    RomaniaCatalogResponse,
    RomaniaGraphResponse,
    RomaniaRouteRequest,
    RomaniaRouteResponse,
    RomaniaSearchAlgorithm,
)
from ..services import ROMANIA_CITIES, get_romania_graph, solve_nqueens, solve_romania_route
from ..settings import Settings, get_settings

router = APIRouter(prefix="/aima", tags=["aima"])


@router.get(
    "/catalog/romania",
    response_model=RomaniaCatalogResponse,
    summary="列出羅馬尼亞地圖城市與可用的路線搜尋演算法。",
)
async def get_romania_catalog(_: Settings = Depends(get_settings)) -> RomaniaCatalogResponse:
    return RomaniaCatalogResponse(
        cities=list(ROMANIA_CITIES),
        search_algorithms=[a.value for a in RomaniaSearchAlgorithm],
    )


@router.get(
    "/catalog/nqueens",
    response_model=NQueensCatalogResponse,
    summary="列出 N 皇后 API 支援的演算法與 N 的合法範圍。",
)
async def get_nqueens_catalog(_: Settings = Depends(get_settings)) -> NQueensCatalogResponse:
    return NQueensCatalogResponse(algorithms=[a.value for a in NQueensAlgorithm])


@router.get(
    "/graph/romania",
    response_model=RomaniaGraphResponse,
    summary="取得羅馬尼亞地圖的節點座標與道路邊（供視覺化或除錯）。",
)
async def get_romania_graph_endpoint(_: Settings = Depends(get_settings)) -> RomaniaGraphResponse:
    return await run_in_threadpool(get_romania_graph)


@router.post(
    "/search/romania",
    response_model=RomaniaRouteResponse,
    summary="使用 AIMA 搜尋演算法規劃羅馬尼亞地圖路線。",
)
async def post_romania_route(
    payload: RomaniaRouteRequest,
    _: Settings = Depends(get_settings),
) -> RomaniaRouteResponse:
    try:
        return await run_in_threadpool(solve_romania_route, payload)
    except ValueError as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    except RuntimeError as exc:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(exc)) from exc


@router.post(
    "/csp/nqueens",
    response_model=NQueensResponse,
    summary="使用 AIMA 的 CSP 演算法求解 N 皇后問題。",
)
async def post_nqueens(
    payload: NQueensRequest,
    _: Settings = Depends(get_settings),
) -> NQueensResponse:
    try:
        return await run_in_threadpool(solve_nqueens, payload)
    except (ValueError, RuntimeError) as exc:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc

