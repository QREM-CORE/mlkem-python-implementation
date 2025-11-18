# src/mlkem/hash.py

from __future__ import annotations
from hashlib import shake_128, sha3_256

def shake128_xof(input_bytes: bytes, outlen: int) -> bytes:
    """
    SHAKE128(input_bytes) -> outlen bytes.
    This is your generic XOF used everywhere in ML-KEM.
    """
    if outlen < 0:
        raise ValueError("outlen must be non-negative")
    return shake_128(input_bytes).digest(outlen)

def shake128_stream(input_bytes: bytes):
    """
    Return a SHAKE128 object so you can squeeze multiple times if needed.
    """
    return shake_128(input_bytes)

def sha3_256_hash(input_bytes: bytes) -> bytes:
    """Return SHA3-256(input_bytes) (32 bytes)."""
    return sha3_256(input_bytes).digest()