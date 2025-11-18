import secrets
from typing import Callable

def random_bytes(n: int) -> bytes:
    """Return n cryptographically secure random bytes."""
    if n < 0:
        raise ValueError("n must be non-negative")
    return secrets.token_bytes(n)

# Optional: allow injecting a custom RNG for testing
RNGFunction = Callable[[int], bytes]

class RNG:
    """
    Wrapper around a random byte generator, so you can inject
    deterministic RNG in tests.
    """
    def __init__(self, rng_func: RNGFunction | None = None) -> None:
        self._rng = rng_func or random_bytes

    def bytes(self, n: int) -> bytes:
        return self._rng(n)

# Global default RNG instance
default_rng = RNG()