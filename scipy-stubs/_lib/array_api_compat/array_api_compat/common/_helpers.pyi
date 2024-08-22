from typing import Any

from ._typing import Array as Array, Device as Device
from scipy._typing import Untyped

def is_numpy_array(x) -> Untyped: ...
def is_cupy_array(x) -> Untyped: ...
def is_torch_array(x) -> Untyped: ...
def is_ndonnx_array(x) -> Untyped: ...
def is_dask_array(x) -> Untyped: ...
def is_jax_array(x) -> Untyped: ...
def is_pydata_sparse_array(x) -> bool: ...
def is_array_api_obj(x) -> Untyped: ...
def array_namespace(*xs, api_version: Untyped | None = None, use_compat: Untyped | None = None) -> Untyped: ...

get_namespace = array_namespace

class _dask_device: ...

def device(x: Array, /) -> Device: ...
def to_device(x: Array, device: Device, /, *, stream: int | Any | None = None) -> Array: ...
def size(x) -> Untyped: ...
