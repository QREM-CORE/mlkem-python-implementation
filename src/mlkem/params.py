# src/mlkem/params.py

from dataclasses import dataclass

Q = 3329              # modulus
N = 256               # polynomial degree

# These tuples are (k, η1, η2, du, dv) matching FIPS 203 (Kyber)
@dataclass(frozen=True)
class MLKEMParams:
    name: str
    k: int
    eta1: int
    eta2: int
    du: int
    dv: int

MLKEM_512 = MLKEMParams(
    name="ML-KEM-512", # number of polynomials in the vector
    k=2, # first noise parameter
    eta1=3, # second noise parameter
    eta2=2, # compression parameter for public key
    du=10, # compression parameter for secret key
    dv=4, # compression parameter for secret key
)

MLKEM_768 = MLKEMParams(
    name="ML-KEM-768", # number of polynomials in the vector
    k=3, # first noise parameter
    eta1=2, # second noise parameter
    eta2=2, # compression parameter for public key
    du=10, # compression parameter for secret key
    dv=4, # compression parameter for secret key
)

MLKEM_1024 = MLKEMParams(
    name="ML-KEM-1024", # number of polynomials in the vector
    k=4, # number of polynomials in the vector
    eta1=2, # first noise parameter
    eta2=2, # second noise parameter
    du=11, # compression parameter for public key
    dv=5, # compression parameter for secret key
)

# Default parameter set you’re targeting (change if needed)
DEFAULT_PARAMS = MLKEM_512