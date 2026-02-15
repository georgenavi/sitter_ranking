"""Utility functions."""

from source.config import FLOAT_PRECISION_EPSILON


def round2(x: float) -> float:
    """Round to 2 decimal places with epsilon for floating-point precision."""
    return round(x + FLOAT_PRECISION_EPSILON, 2)