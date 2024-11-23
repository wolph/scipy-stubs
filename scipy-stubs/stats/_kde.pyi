from collections.abc import Callable
from typing import Literal, TypeAlias
from typing_extensions import Self

import numpy as np
import optype.numpy as onp
from scipy._typing import Seed

__all__ = ["gaussian_kde"]

_Float1D: TypeAlias = onp.Array1D[np.float64 | np.float32]
_Float2D: TypeAlias = onp.Array2D[np.float64 | np.float32]
_BWMethod: TypeAlias = Literal["scott", "silverman"] | onp.ToFloat | Callable[[gaussian_kde], onp.ToFloat]

###

class gaussian_kde:
    dataset: _Float1D | _Float2D
    covariance: _Float2D
    factor: np.float64
    d: int
    n: int

    @property
    def weights(self) -> onp.ArrayND[np.float64 | np.float32]: ...
    @property
    def inv_cov(self) -> _Float2D: ...
    @property
    def neff(self) -> int: ...
    def __init__(
        self,
        /,
        dataset: onp.ToFloat1D | onp.ToFloat2D,
        bw_method: _BWMethod | None = None,
        weights: onp.ToFloat1D | onp.ToFloat2D | None = None,
    ) -> None: ...
    def __call__(self, /, points: onp.ToFloat1D | onp.ToFloat2D) -> _Float1D: ...
    evaluate = __call__
    def pdf(self, /, x: onp.ToFloat1D | onp.ToFloat2D) -> _Float1D: ...
    def logpdf(self, /, x: onp.ToFloat1D | onp.ToFloat2D) -> _Float1D: ...
    def integrate_gaussian(self, /, mean: onp.ToFloat1D, cov: onp.ToFloat2D) -> np.float64 | np.float32: ...
    def integrate_box_1d(self, /, low: onp.ToFloat, high: onp.ToFloat) -> np.float64 | np.float32: ...
    def integrate_box(
        self,
        /,
        low_bounds: onp.ToFloat1D,
        high_bounds: onp.ToFloat1D,
        maxpts: int | None = None,
    ) -> np.float64 | np.float32: ...
    def integrate_kde(self, /, other: Self) -> np.float64 | np.float32: ...
    def resample(self, /, size: int | None = None, seed: Seed | None = None) -> _Float2D: ...
    def scotts_factor(self, /) -> np.float64: ...
    def silverman_factor(self, /) -> np.float64: ...
    def covariance_factor(self, /) -> np.float64: ...
    def set_bandwidth(self, /, bw_method: _BWMethod | None = None) -> None: ...
    def marginal(self, /, dimensions: onp.ToInt | onp.ToInt1D) -> Self: ...
