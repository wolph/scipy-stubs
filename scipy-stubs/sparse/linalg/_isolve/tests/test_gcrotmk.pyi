from scipy._typing import Untyped
from scipy.linalg import norm as norm
from scipy.sparse import csr_matrix as csr_matrix, eye as eye, rand as rand
from scipy.sparse.linalg import splu as splu
from scipy.sparse.linalg._interface import LinearOperator as LinearOperator
from scipy.sparse.linalg._isolve import gcrotmk as gcrotmk, gmres as gmres

Am: Untyped
b: Untyped
count: Untyped

def matvec(v) -> Untyped: ...

A: Untyped

def do_solve(**kw) -> Untyped: ...

class TestGCROTMK:
    def test_preconditioner(self): ...
    def test_arnoldi(self): ...
    def test_cornercase(self): ...
    def test_nans(self): ...
    def test_truncate(self): ...
    def test_CU(self): ...
    def test_denormals(self): ...
