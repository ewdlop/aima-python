"""Pydantic models for AIMA Online services."""

from __future__ import annotations

from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class RomaniaSearchAlgorithm(str, Enum):
    """Supported search algorithms for Romania map."""

    uniform_cost = "uniform_cost"
    breadth_first = "breadth_first"
    astar = "astar"


class RomaniaRouteRequest(BaseModel):
    """Request payload for Romania route search."""

    start: str = Field(..., description="起點城市名稱（區分大小寫）。")
    goal: str = Field(..., description="終點城市名稱（區分大小寫）。")
    algorithm: RomaniaSearchAlgorithm = Field(
        default=RomaniaSearchAlgorithm.uniform_cost,
        description="搜尋演算法。",
    )


class RomaniaRouteResponse(BaseModel):
    """Response payload describing the path between two Romanian cities."""

    start: str
    goal: str
    algorithm: RomaniaSearchAlgorithm
    path: list[str]
    actions: list[str]
    total_cost: float
    explored_steps: int


class RomaniaCityNode(BaseModel):
    """One city on the Romania map with optional layout coordinates."""

    name: str
    x: float | None = Field(default=None, description="圖上 x 座標（教材用示意）。")
    y: float | None = Field(default=None, description="圖上 y 座標（教材用示意）。")


class RomaniaRoadEdge(BaseModel):
    """Undirected road between two cities (deduplicated for API output)."""

    a: str
    b: str
    cost: float


class RomaniaGraphResponse(BaseModel):
    """Nodes and edges of the Romania road map."""

    nodes: list[RomaniaCityNode]
    edges: list[RomaniaRoadEdge]


class RomaniaCatalogResponse(BaseModel):
    """Discover Romania route API capabilities."""

    cities: list[str]
    search_algorithms: list[str]


class NQueensCatalogResponse(BaseModel):
    """Discover N-Queens API capabilities."""

    algorithms: list[str]
    n_min: int = 4
    n_max: int = 25


class NQueensAlgorithm(str, Enum):
    """Supported algorithms for N-Queens solver."""

    backtracking = "backtracking"
    min_conflicts = "min_conflicts"


class NQueensRequest(BaseModel):
    """Request payload for solving the N-Queens problem."""

    n: int = Field(default=8, ge=4, le=25, description="棋盤大小（N），介於 4 到 25。")
    algorithm: NQueensAlgorithm = Field(
        default=NQueensAlgorithm.backtracking, description="求解演算法。"
    )
    max_steps: int | None = Field(
        default=1000,
        description="使用 min_conflicts 時的最大步數限制。",
        ge=1,
    )


class NQueensResponse(BaseModel):
    """Response payload for N-Queens solutions."""

    n: int
    algorithm: NQueensAlgorithm
    assignments: list[int]
    is_solution: bool
    raw: dict[int, int] | None = Field(
        default=None,
        description="CSP 求解器回傳的原始指派：鍵為欄位（整數），值為該欄皇后所在列。",
    )


class HFTextGenerationRequest(BaseModel):
    """Request payload for Hugging Face text generation API."""

    prompt: str = Field(..., description="要傳送給模型的提示文字。")
    model: str | None = Field(
        default=None,
        description="覆寫預設模型 ID。",
    )
    inference_api_url: str | None = Field(
        default=None,
        description="覆寫預設的 Inference Endpoint URL。",
    )
    max_new_tokens: int = Field(default=256, ge=1, le=2048)
    temperature: float = Field(default=0.7, ge=0.0, le=2.0)
    top_p: float = Field(default=0.95, ge=0.0, le=1.0)
    repetition_penalty: float = Field(default=1.0, ge=0.0)
    do_sample: bool = True
    return_full_text: bool = False
    stop_sequences: list[str] | None = None


class HFTextGenerationResponse(BaseModel):
    """Response wrapper for Hugging Face text generation."""

    model: str
    content: str
    raw: Any | None = None


class HFSpaceDeploymentResult(BaseModel):
    """Metadata returned after deploying (creating/updating) a Space."""

    repo_id: str
    url: str
    space_sdk: str
    space_hardware: str
    private: bool | None = None


class HFSpaceDeployRequest(BaseModel):
    """Request payload for Space deployment endpoint."""

    repo_id: str | None = Field(
        default=None,
        description="要建立/更新的 Space repo，例如 username/mcp-fastapi。",
    )
    space_sdk: str | None = Field(default=None, description="Space SDK 類型，例如 docker、gradio。")
    space_hardware: str | None = Field(
        default=None,
        description="Space 硬體設定，例如 cpu-basic、t4-small 等。",
    )
    private: bool | None = Field(default=None, description="是否建立為私人 Space。")
    update_only: bool = Field(
        default=False,
        description="設定為 True 時僅更新既有 Space，不會自動建立新的。",
    )

