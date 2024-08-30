from scipy._typing import Untyped

__all__ = ["fht", "fhtoffset", "ifht"]

def fht(a: Untyped, dln: Untyped, mu: Untyped, offset: float = 0.0, bias: float = 0.0) -> Untyped: ...
def ifht(A: Untyped, dln: Untyped, mu: Untyped, offset: float = 0.0, bias: float = 0.0) -> Untyped: ...
def fhtcoeff(n: Untyped, dln: Untyped, mu: Untyped, offset: float = 0.0, bias: float = 0.0, inverse: bool = False) -> Untyped: ...
def fhtoffset(dln: Untyped, mu: Untyped, initial: float = 0.0, bias: float = 0.0) -> Untyped: ...
