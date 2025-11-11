"""Service layer for the AIMA FastAPI application."""

from .aima import ROMANIA_CITIES, describe_result_as_text, solve_nqueens, solve_romania_route

__all__ = [
    "solve_romania_route",
    "solve_nqueens",
    "describe_result_as_text",
    "ROMANIA_CITIES",
]

