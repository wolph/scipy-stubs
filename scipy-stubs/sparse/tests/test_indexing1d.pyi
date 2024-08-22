from collections.abc import Generator

from .test_arithmetic1d import toarray as toarray
from scipy._typing import Untyped
from scipy.sparse import SparseEfficiencyWarning as SparseEfficiencyWarning, csr_array as csr_array, dok_array as dok_array

formats_for_index1d: Untyped

def check_remains_sorted(X) -> Generator[None, None, None]: ...

class TestGetSet1D:
    def test_None_index(self, spcreator): ...
    def test_getitem_shape(self, spcreator): ...
    def test_getelement(self, spcreator): ...
    def test_setelement(self, spcreator): ...

class TestSlicingAndFancy1D:
    def test_get_array_index(self, spcreator): ...
    def test_set_array_index(self, spcreator): ...
    def test_dtype_preservation(self, spcreator): ...
    def test_get_1d_slice(self, spcreator): ...
    def test_slicing_idx_slice(self, spcreator): ...
    def test_ellipsis_1d_slicing(self, spcreator): ...
    def test_slice_scalar_assign(self, spcreator): ...
    def test_slice_assign_2(self, spcreator): ...
    def test_self_self_assignment(self, spcreator): ...
    def test_slice_assignment(self, spcreator): ...
    def test_set_slice(self, spcreator): ...
    def test_assign_empty(self, spcreator): ...
    def test_dtype_preservation_empty_index(self, spcreator): ...
    def test_bad_index(self, spcreator): ...
    def test_fancy_indexing_2darray(self, spcreator): ...
    def test_fancy_indexing(self, spcreator): ...
    def test_fancy_indexing_boolean(self, spcreator): ...
    def test_fancy_indexing_sparse_boolean(self, spcreator): ...
    def test_fancy_indexing_seq_assign(self, spcreator): ...
    def test_fancy_indexing_empty(self, spcreator): ...
    def test_bad_index_assign(self, spcreator): ...
    def test_fancy_indexing_set(self, spcreator): ...
    def test_sequence_assignment(self, spcreator): ...
    def test_fancy_assign_empty(self, spcreator): ...
