from scipy._typing import Untyped
from scipy.sparse.linalg._isolve import minres as minres

def get_sample_problem() -> Untyped: ...
def test_singular(): ...
def test_x0_is_used_by(): ...
def test_shift(): ...
def test_asymmetric_fail(): ...
def test_minres_non_default_x0(): ...
def test_minres_precond_non_default_x0(): ...
def test_minres_precond_exact_x0(): ...
