from dataclasses import dataclass
from typing import NamedTuple

import numpy as np

from . import distributions as distributions
from ._common import ConfidenceInterval as ConfidenceInterval
from ._continuous_distns import norm as norm
from scipy._typing import Untyped
from scipy.fft import ifft as ifft
from scipy.optimize import shgo as shgo
from scipy.special import gamma as gamma, gammaln as gammaln, kv as kv

class Epps_Singleton_2sampResult(NamedTuple):
    statistic: Untyped
    pvalue: Untyped

def epps_singleton_2samp(x, y, t=(0.4, 0.8)) -> Untyped: ...
def poisson_means_test(k1, n1, k2, n2, *, diff: int = 0, alternative: str = "two-sided") -> Untyped: ...

class CramerVonMisesResult:
    statistic: Untyped
    pvalue: Untyped
    def __init__(self, statistic, pvalue) -> None: ...

def cramervonmises(rvs, cdf, args=()) -> Untyped: ...
@dataclass
class SomersDResult:
    statistic: float
    pvalue: float
    table: np.ndarray

def somersd(x, y: Untyped | None = None, alternative: str = "two-sided") -> Untyped: ...
@dataclass
class BarnardExactResult:
    statistic: float
    pvalue: float

def barnard_exact(table, alternative: str = "two-sided", pooled: bool = True, n: int = 32) -> Untyped: ...
@dataclass
class BoschlooExactResult:
    statistic: float
    pvalue: float

def boschloo_exact(table, alternative: str = "two-sided", n: int = 32) -> Untyped: ...
def cramervonmises_2samp(x, y, method: str = "auto") -> Untyped: ...

class TukeyHSDResult:
    statistic: Untyped
    pvalue: Untyped
    def __init__(self, statistic, pvalue, _nobs, _ntreatments, _stand_err) -> None: ...
    def confidence_interval(self, confidence_level: float = 0.95) -> Untyped: ...

def tukey_hsd(*args) -> Untyped: ...
