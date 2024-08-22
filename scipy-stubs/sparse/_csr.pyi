from ._base import sparray as sparray
from ._compressed import _cs_matrix
from ._matrix import spmatrix as spmatrix
from ._sparsetools import (
    csr_count_blocks as csr_count_blocks,
    csr_sample_values as csr_sample_values,
    csr_tobsr as csr_tobsr,
    csr_tocsc as csr_tocsc,
    get_csr_submatrix as get_csr_submatrix,
)
from ._sputils import upcast as upcast
from scipy._typing import Untyped

__docformat__: str

class _csr_base(_cs_matrix):
    def transpose(self, axes: Untyped | None = None, copy: bool = False) -> Untyped: ...
    def tolil(self, copy: bool = False) -> Untyped: ...
    def tocsr(self, copy: bool = False) -> Untyped: ...
    def tocsc(self, copy: bool = False) -> Untyped: ...
    def tobsr(self, blocksize: Untyped | None = None, copy: bool = True) -> Untyped: ...
    def __iter__(self) -> Untyped: ...

def isspmatrix_csr(x) -> Untyped: ...

class csr_array(_csr_base, sparray): ...
class csr_matrix(spmatrix, _csr_base): ...
