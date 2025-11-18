# src/mlkem/poly.py

from __future__ import annotations
from dataclasses import dataclass
from typing import List, Iterable
from .params import N, Q
from .field import (
    mod_q,
    vector_add_mod,
    vector_sub_mod,
    scalar_mul_mod,
)

@dataclass
class Poly:
    """
    Polynomial f(x) = sum_{i=0}^{N-1} f[i] x^i over Z_q,
    represented as a list of length N with coefficients in [0, Q-1].
    """
    coeffs: List[int]

    def __post_init__(self) -> None:
        if len(self.coeffs) != N:
            raise ValueError(f"Polynomial must have length {N}, got {len(self.coeffs)}")
        # Ensure coefficients are in canonical form mod q
        self.coeffs = [mod_q(c) for c in self.coeffs]

    @classmethod
    def zero(cls) -> "Poly":
        return cls([0] * N)

    @classmethod
    def from_iterable(cls, it: Iterable[int]) -> "Poly":
        coeffs = list(it)
        if len(coeffs) != N:
            raise ValueError(f"Expected {N} coefficients, got {len(coeffs)}")
        return cls(coeffs)

    def to_list(self) -> List[int]:
        return list(self.coeffs)

    # --- basic arithmetic ---

    def __add__(self, other: "Poly") -> "Poly":
        return Poly(vector_add_mod(self.coeffs, other.coeffs))

    def __sub__(self, other: "Poly") -> "Poly":
        return Poly(vector_sub_mod(self.coeffs, other.coeffs))

    def __neg__(self) -> "Poly":
        from .field import neg_mod  # avoid circular import at top
        return Poly([neg_mod(c) for c in self.coeffs])

    def scale(self, c: int) -> "Poly":
        return Poly(scalar_mul_mod(c, self.coeffs))

    # Plain-schoolbook polynomial multiplication (slow but correct).
    # We'll later plug in NTT-based multiplication instead.
    def mul_schoolbook(self, other: "Poly") -> "Poly":
        from .field import add_mod, mul_mod
        # Multiplication in Z_q[x]/(x^N + 1) for Kyber
        res = [0] * N
        for i in range(N):
            for j in range(N):
                k = (i + j) % N
                sign = 1 if i + j < N else -1  # x^N = -1
                term = mul_mod(self.coeffs[i], other.coeffs[j])
                if sign == 1:
                    res[k] = add_mod(res[k], term)
                else:
                    res[k] = add_mod(res[k], -term)
        return Poly(res)

    # will later get .ntt(), .intt(), etc.