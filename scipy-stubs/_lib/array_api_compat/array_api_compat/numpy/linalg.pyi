import numpy as np
from numpy.linalg import *

from .._internal import get_xp as get_xp
from ._aliases import matmul as matmul, matrix_transpose as matrix_transpose, tensordot as tensordot, vecdot as vecdot
from scipy._typing import Untyped

cross: Untyped
outer: Untyped
EighResult: Untyped
QRResult: Untyped
SlogdetResult: Untyped
SVDResult: Untyped
eigh: Untyped
qr: Untyped
slogdet: Untyped
svd: Untyped
cholesky: Untyped
matrix_rank: Untyped
pinv: Untyped
matrix_norm: Untyped
svdvals: Untyped
diagonal: Untyped
trace: Untyped

def solve(x1: np.ndarray, x2: np.ndarray, /) -> np.ndarray: ...

vector_norm: Untyped
