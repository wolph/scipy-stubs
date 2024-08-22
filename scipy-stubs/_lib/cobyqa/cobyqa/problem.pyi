from .settings import BARRIER as BARRIER, PRINT_OPTIONS as PRINT_OPTIONS
from .utils import CallbackSuccess as CallbackSuccess, exact_1d_array as exact_1d_array, get_arrays_tol as get_arrays_tol
from scipy._typing import Untyped
from scipy.optimize import (
    Bounds as Bounds,
    LinearConstraint as LinearConstraint,
    NonlinearConstraint as NonlinearConstraint,
    OptimizeResult as OptimizeResult,
)
from scipy.optimize._constraints import PreparedConstraint as PreparedConstraint

class ObjectiveFunction:
    def __init__(self, fun, verbose, debug, *args) -> None: ...
    def __call__(self, x) -> Untyped: ...
    @property
    def n_eval(self) -> Untyped: ...
    @property
    def name(self) -> Untyped: ...

class BoundConstraints:
    is_feasible: Untyped
    m: Untyped
    pcs: Untyped
    def __init__(self, bounds) -> None: ...
    @property
    def xl(self) -> Untyped: ...
    @property
    def xu(self) -> Untyped: ...
    def maxcv(self, x) -> Untyped: ...
    def violation(self, x) -> Untyped: ...
    def project(self, x) -> Untyped: ...

class LinearConstraints:
    pcs: Untyped
    def __init__(self, constraints, n, debug) -> None: ...
    @property
    def a_ub(self) -> Untyped: ...
    @property
    def b_ub(self) -> Untyped: ...
    @property
    def a_eq(self) -> Untyped: ...
    @property
    def b_eq(self) -> Untyped: ...
    @property
    def m_ub(self) -> Untyped: ...
    @property
    def m_eq(self) -> Untyped: ...
    def maxcv(self, x) -> Untyped: ...
    def violation(self, x) -> Untyped: ...

class NonlinearConstraints:
    pcs: Untyped
    def __init__(self, constraints, verbose, debug) -> None: ...
    def __call__(self, x) -> Untyped: ...
    @property
    def m_ub(self) -> Untyped: ...
    @property
    def m_eq(self) -> Untyped: ...
    @property
    def n_eval(self) -> Untyped: ...
    def maxcv(self, x, cub_val: Untyped | None = None, ceq_val: Untyped | None = None) -> Untyped: ...
    def violation(self, x, cub_val: Untyped | None = None, ceq_val: Untyped | None = None) -> Untyped: ...

class Problem:
    def __init__(
        self,
        obj,
        x0,
        bounds,
        linear,
        nonlinear,
        callback,
        feasibility_tol,
        scale,
        store_history,
        history_size,
        filter_size,
        debug,
    ) -> None: ...
    def __call__(self, x) -> Untyped: ...
    @property
    def n(self) -> Untyped: ...
    @property
    def n_orig(self) -> Untyped: ...
    @property
    def x0(self) -> Untyped: ...
    @property
    def n_eval(self) -> Untyped: ...
    @property
    def fun_name(self) -> Untyped: ...
    @property
    def bounds(self) -> Untyped: ...
    @property
    def linear(self) -> Untyped: ...
    @property
    def m_bounds(self) -> Untyped: ...
    @property
    def m_linear_ub(self) -> Untyped: ...
    @property
    def m_linear_eq(self) -> Untyped: ...
    @property
    def m_nonlinear_ub(self) -> Untyped: ...
    @property
    def m_nonlinear_eq(self) -> Untyped: ...
    @property
    def fun_history(self) -> Untyped: ...
    @property
    def maxcv_history(self) -> Untyped: ...
    @property
    def type(self) -> Untyped: ...
    @property
    def is_feasibility(self) -> Untyped: ...
    def build_x(self, x) -> Untyped: ...
    def maxcv(self, x, cub_val: Untyped | None = None, ceq_val: Untyped | None = None) -> Untyped: ...
    def violation(self, x, cub_val: Untyped | None = None, ceq_val: Untyped | None = None) -> Untyped: ...
    def best_eval(self, penalty) -> Untyped: ...
