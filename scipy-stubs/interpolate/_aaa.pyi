from scipy._typing import Untyped

class AAA:
    def __init__(self, points, values, *, rtol: Untyped | None = None, max_terms: int = 100): ...
    def __call__(self, z) -> Untyped: ...
    def poles(self) -> Untyped: ...
    def residues(self) -> Untyped: ...
    def roots(self) -> Untyped: ...
