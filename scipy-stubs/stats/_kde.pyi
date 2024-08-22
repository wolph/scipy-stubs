from ._stats import (
    gaussian_kernel_estimate as gaussian_kernel_estimate,
    gaussian_kernel_estimate_log as gaussian_kernel_estimate_log,
)
from scipy import linalg as linalg, special as special
from scipy._lib._util import check_random_state as check_random_state
from scipy._typing import Untyped

class gaussian_kde:
    dataset: Untyped
    def __init__(self, dataset, bw_method: Untyped | None = None, weights: Untyped | None = None): ...
    def evaluate(self, points) -> Untyped: ...
    __call__ = evaluate
    def integrate_gaussian(self, mean, cov) -> Untyped: ...
    def integrate_box_1d(self, low, high) -> Untyped: ...
    def integrate_box(self, low_bounds, high_bounds, maxpts: Untyped | None = None) -> Untyped: ...
    def integrate_kde(self, other) -> Untyped: ...
    def resample(self, size: Untyped | None = None, seed: Untyped | None = None) -> Untyped: ...
    def scotts_factor(self) -> Untyped: ...
    def silverman_factor(self) -> Untyped: ...
    covariance_factor = scotts_factor
    def set_bandwidth(self, bw_method: Untyped | None = None) -> Untyped: ...
    factor: Untyped
    @property
    def inv_cov(self) -> Untyped: ...
    def pdf(self, x) -> Untyped: ...
    def logpdf(self, x) -> Untyped: ...
    def marginal(self, dimensions) -> Untyped: ...
    @property
    def weights(self) -> Untyped: ...
    @property
    def neff(self) -> Untyped: ...
