from collections.abc import Sequence

from torch import dtype as Dtype

from .._internal import get_xp as get_xp
from ..common._aliases import (
    UniqueAllResult as UniqueAllResult,
    UniqueCountsResult as UniqueCountsResult,
    UniqueInverseResult as UniqueInverseResult,
)
from ..common._typing import Device as Device
from scipy._typing import Untyped

array: Untyped

def result_type(*arrays_and_dtypes: array | Dtype) -> Dtype: ...
def can_cast(from_: Dtype | array, to: Dtype, /) -> bool: ...

bitwise_invert: Untyped
newaxis: Untyped
add: Untyped
atan2: Untyped
bitwise_and: Untyped
bitwise_left_shift: Untyped
bitwise_or: Untyped
bitwise_right_shift: Untyped
bitwise_xor: Untyped
copysign: Untyped
divide: Untyped
equal: Untyped
floor_divide: Untyped
greater: Untyped
greater_equal: Untyped
less: Untyped
less_equal: Untyped
logaddexp: Untyped
multiply: Untyped
not_equal: Untyped
pow: Untyped
remainder: Untyped
subtract: Untyped

def max(x: array, /, *, axis: int | tuple[int, ...] | None = None, keepdims: bool = False) -> array: ...
def min(x: array, /, *, axis: int | tuple[int, ...] | None = None, keepdims: bool = False) -> array: ...

clip: Untyped

def sort(x: array, /, *, axis: int = -1, descending: bool = False, stable: bool = True, **kwargs) -> array: ...
def prod(
    x: array, /, *, axis: int | tuple[int, ...] | None = None, dtype: Dtype | None = None, keepdims: bool = False, **kwargs
) -> array: ...
def sum(
    x: array, /, *, axis: int | tuple[int, ...] | None = None, dtype: Dtype | None = None, keepdims: bool = False, **kwargs
) -> array: ...
def any(x: array, /, *, axis: int | tuple[int, ...] | None = None, keepdims: bool = False, **kwargs) -> array: ...
def all(x: array, /, *, axis: int | tuple[int, ...] | None = None, keepdims: bool = False, **kwargs) -> array: ...
def mean(x: array, /, *, axis: int | tuple[int, ...] | None = None, keepdims: bool = False, **kwargs) -> array: ...
def std(
    x: array, /, *, axis: int | tuple[int, ...] | None = None, correction: int | float = 0.0, keepdims: bool = False, **kwargs
) -> array: ...
def var(
    x: array, /, *, axis: int | tuple[int, ...] | None = None, correction: int | float = 0.0, keepdims: bool = False, **kwargs
) -> array: ...
def concat(arrays: tuple[array, ...] | list[array], /, *, axis: int | None = 0, **kwargs) -> array: ...
def squeeze(x: array, /, axis: int | tuple[int, ...]) -> array: ...
def broadcast_to(x: array, /, shape: tuple[int, ...], **kwargs) -> array: ...
def permute_dims(x: array, /, axes: tuple[int, ...]) -> array: ...
def flip(x: array, /, *, axis: int | tuple[int, ...] | None = None, **kwargs) -> array: ...
def roll(x: array, /, shift: int | tuple[int, ...], *, axis: int | tuple[int, ...] | None = None, **kwargs) -> array: ...
def nonzero(x: array, /, **kwargs) -> tuple[array, ...]: ...
def where(condition: array, x1: array, x2: array, /) -> array: ...
def reshape(x: array, /, shape: tuple[int, ...], copy: bool | None = None, **kwargs) -> array: ...
def arange(
    start: int | float,
    /,
    stop: int | float | None = None,
    step: int | float = 1,
    *,
    dtype: Dtype | None = None,
    device: Device | None = None,
    **kwargs,
) -> array: ...
def eye(
    n_rows: int, n_cols: int | None = None, /, *, k: int = 0, dtype: Dtype | None = None, device: Device | None = None, **kwargs
) -> array: ...
def linspace(
    start: int | float,
    stop: int | float,
    /,
    num: int,
    *,
    dtype: Dtype | None = None,
    device: Device | None = None,
    endpoint: bool = True,
    **kwargs,
) -> array: ...
def full(
    shape: int | tuple[int, ...],
    fill_value: bool | int | float | complex,
    *,
    dtype: Dtype | None = None,
    device: Device | None = None,
    **kwargs,
) -> array: ...
def ones(shape: int | tuple[int, ...], *, dtype: Dtype | None = None, device: Device | None = None, **kwargs) -> array: ...
def zeros(shape: int | tuple[int, ...], *, dtype: Dtype | None = None, device: Device | None = None, **kwargs) -> array: ...
def empty(shape: int | tuple[int, ...], *, dtype: Dtype | None = None, device: Device | None = None, **kwargs) -> array: ...
def tril(x: array, /, *, k: int = 0) -> array: ...
def triu(x: array, /, *, k: int = 0) -> array: ...
def expand_dims(x: array, /, *, axis: int = 0) -> array: ...
def astype(x: array, dtype: Dtype, /, *, copy: bool = True) -> array: ...
def broadcast_arrays(*arrays: array) -> list[array]: ...
def unique_all(x: array) -> UniqueAllResult: ...
def unique_counts(x: array) -> UniqueCountsResult: ...
def unique_inverse(x: array) -> UniqueInverseResult: ...
def unique_values(x: array) -> array: ...
def matmul(x1: array, x2: array, /, **kwargs) -> array: ...

matrix_transpose: Untyped

def vecdot(x1: array, x2: array, /, *, axis: int = -1) -> array: ...
def tensordot(x1: array, x2: array, /, *, axes: int | tuple[Sequence[int], Sequence[int]] = 2, **kwargs) -> array: ...
def isdtype(dtype: Dtype, kind: Dtype | str | tuple[Dtype | str, ...], *, _tuple: bool = True) -> bool: ...
def take(x: array, indices: array, /, *, axis: int | None = None, **kwargs) -> array: ...
