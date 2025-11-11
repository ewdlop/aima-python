"""Expose selected AIMA algorithms as HTTP APIs."""

from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.concurrency import run_in_threadpool

from ..schemas import (
    NQueensRequest,
    NQueensResponse,
    RomaniaRouteRequest,
    RomaniaRouteResponse,
)
from ..services import solve_nqueens, solve_romania_route
from ..settings import Settings, get_settings

router = APIRouter(prefix="/aima", tags=["aima"])


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

