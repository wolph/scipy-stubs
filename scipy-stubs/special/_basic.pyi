from typing import Literal

import numpy as np
import numpy.typing as npt
from numpy import sinc

from ._ufuncs import psi as digamma
from scipy._typing import Untyped

__all__ = [
    "ai_zeros",
    "assoc_laguerre",
    "bei_zeros",
    "beip_zeros",
    "ber_zeros",
    "bernoulli",
    "berp_zeros",
    "bi_zeros",
    "clpmn",
    "comb",
    "digamma",
    "diric",
    "erf_zeros",
    "euler",
    "factorial",
    "factorial2",
    "factorialk",
    "fresnel_zeros",
    "fresnelc_zeros",
    "fresnels_zeros",
    "h1vp",
    "h2vp",
    "ivp",
    "jn_zeros",
    "jnjnp_zeros",
    "jnp_zeros",
    "jnyn_zeros",
    "jvp",
    "kei_zeros",
    "keip_zeros",
    "kelvin_zeros",
    "ker_zeros",
    "kerp_zeros",
    "kvp",
    "lmbda",
    "lpmn",
    "lpn",
    "lqmn",
    "lqn",
    "mathieu_even_coef",
    "mathieu_odd_coef",
    "obl_cv_seq",
    "pbdn_seq",
    "pbdv_seq",
    "pbvv_seq",
    "perm",
    "polygamma",
    "pro_cv_seq",
    "riccati_jn",
    "riccati_yn",
    "sinc",
    "stirling2",
    "y0_zeros",
    "y1_zeros",
    "y1p_zeros",
    "yn_zeros",
    "ynp_zeros",
    "yvp",
    "zeta",
]

def diric(x: npt.ArrayLike, n: int) -> Untyped: ...
def jnjnp_zeros(nt: int) -> Untyped: ...
def jnyn_zeros(n: int, nt: int) -> Untyped: ...
def jn_zeros(n: int, nt: int) -> Untyped: ...
def jnp_zeros(n: int, nt: int) -> Untyped: ...
def yn_zeros(n: int, nt: int) -> Untyped: ...
def ynp_zeros(n: int, nt: int) -> Untyped: ...
def y0_zeros(nt: int, complex: bool = ...) -> Untyped: ...
def y1_zeros(nt: int, complex: bool = ...) -> Untyped: ...
def y1p_zeros(nt: int, complex: bool = ...) -> Untyped: ...
def jvp(v: npt.ArrayLike, z: complex, n: int = ...) -> Untyped: ...
def yvp(v: npt.ArrayLike, z: complex, n: int = ...) -> Untyped: ...
def kvp(v: npt.ArrayLike, z: complex, n: int = ...) -> Untyped: ...
def ivp(v: npt.ArrayLike, z: complex, n: int = ...) -> Untyped: ...
def h1vp(v: npt.ArrayLike, z: complex, n: int = ...) -> Untyped: ...
def h2vp(v: npt.ArrayLike, z: complex, n: int = ...) -> Untyped: ...
def riccati_jn(n: int, x: float) -> Untyped: ...
def riccati_yn(n: int, x: float) -> Untyped: ...
def erf_zeros(nt: int) -> Untyped: ...
def fresnelc_zeros(nt: int) -> Untyped: ...
def fresnels_zeros(nt: int) -> Untyped: ...
def fresnel_zeros(nt: int) -> Untyped: ...
def assoc_laguerre(x: float | npt.NDArray[np.float64], n: int, k: float = ...) -> Untyped: ...

def polygamma(n: npt.ArrayLike, x: npt.ArrayLike) -> Untyped: ...
def mathieu_even_coef(m: int, q: float) -> Untyped: ...
def mathieu_odd_coef(m: int, q: float) -> Untyped: ...
def lpmn(m: int, n: int, z: npt.ArrayLike) -> Untyped: ...
def clpmn(m: int, n: int, z: npt.ArrayLike, type: Literal[2, 3] = ...) -> Untyped: ...
def lqmn(m: int, n: int, z: npt.ArrayLike) -> Untyped: ...
def bernoulli(n: int) -> Untyped: ...
def euler(n: int) -> Untyped: ...
def lpn(n: int, z: npt.ArrayLike) -> Untyped: ...
def lqn(n: int, z: npt.ArrayLike) -> Untyped: ...
def ai_zeros(nt: int) -> Untyped: ...
def bi_zeros(nt: int) -> Untyped: ...
def lmbda(v: float, x: float) -> Untyped: ...
def pbdv_seq(v: float, x: float) -> Untyped: ...
def pbvv_seq(v: float, x: float) -> Untyped: ...
def pbdn_seq(n: int, z: complex) -> Untyped: ...
def ber_zeros(nt: int) -> Untyped: ...
def bei_zeros(nt: int) -> Untyped: ...
def ker_zeros(nt: int) -> Untyped: ...
def kei_zeros(nt: int) -> Untyped: ...
def berp_zeros(nt: int) -> Untyped: ...
def beip_zeros(nt: int) -> Untyped: ...
def kerp_zeros(nt: int) -> Untyped: ...
def keip_zeros(nt: int) -> Untyped: ...
def kelvin_zeros(nt: int) -> Untyped: ...
def pro_cv_seq(m: int, n: int, c: complex) -> Untyped: ...
def obl_cv_seq(m: int, n: int, c: complex) -> Untyped: ...
def comb(n: npt.ArrayLike, k: npt.ArrayLike, *, exact: bool = ..., repetition: bool = ...) -> Untyped: ...
def perm(n: npt.ArrayLike, k: npt.ArrayLike, *, exact: bool = ...) -> Untyped: ...
def factorial(n: npt.ArrayLike, *, exact: bool = ...) -> Untyped: ...
def factorial2(n: npt.ArrayLike, *, exact: bool = ...) -> Untyped: ...
def factorialk(n: npt.ArrayLike, k: int, *, exact: bool | None = ...) -> Untyped: ...
def stirling2(N: npt.ArrayLike, K: npt.ArrayLike, *, exact: bool = ...) -> Untyped: ...
def zeta(x: npt.ArrayLike, q: npt.ArrayLike | None = ..., out: npt.NDArray[np.generic] | None = ...) -> Untyped: ...
