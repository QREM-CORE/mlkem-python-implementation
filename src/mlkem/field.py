# src/mlkem/field.py

from __future__ import annotations
from typing import Iterable, List
from .params import Q

def mod_q(x: int) -> int:
    """Reduce integer x into [0, Q-1]."""
    x %= Q
    if x < 0:
        x += Q
    return x

def add_mod(a: int, b: int) -> int:
    """(a + b) mod Q."""
    return mod_q(a + b)

def sub_mod(a: int, b: int) -> int:
    """(a - b) mod Q."""
    return mod_q(a - b)

def mul_mod(a: int, b: int) -> int:
    """(a * b) mod Q."""
    return mod_q(a * b)

def neg_mod(a: int) -> int:
    """-a mod Q."""
    return mod_q(-a)

def vector_add_mod(xs: Iterable[int], ys: Iterable[int]) -> List[int]:
    """Element-wise add of two coefficient lists mod Q."""
    return [add_mod(x, y) for x, y in zip(xs, ys)]

def vector_sub_mod(xs: Iterable[int], ys: Iterable[int]) -> List[int]:
    """Element-wise sub of two coefficient lists mod Q."""
    return [sub_mod(x, y) for x, y in zip(xs, ys)]

def scalar_mul_mod(c: int, xs: Iterable[int]) -> List[int]:
    """Scalar multiply coefficients by c mod Q."""
    return [mul_mod(c, x) for x in xs]