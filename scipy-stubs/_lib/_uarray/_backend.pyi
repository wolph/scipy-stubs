import typing
from collections.abc import Generator

from ._uarray import BackendNotImplementedError as BackendNotImplementedError
from scipy._typing import Untyped

ArgumentExtractorType: Untyped
ArgumentReplacerType: typing.TypeAlias = typing.Callable[[tuple, dict, tuple], tuple[tuple, dict]]

def unpickle_function(mod_name, qname, self_) -> Untyped: ...
def pickle_function(func) -> Untyped: ...
def pickle_state(state) -> Untyped: ...
def pickle_set_backend_context(ctx) -> Untyped: ...
def pickle_skip_backend_context(ctx) -> Untyped: ...
def get_state() -> Untyped: ...
def reset_state() -> Generator[None, None, None]: ...
def set_state(state) -> Generator[None, None, None]: ...
def create_multimethod(*args, **kwargs) -> Untyped: ...
def generate_multimethod(
    argument_extractor: ArgumentExtractorType,
    argument_replacer: ArgumentReplacerType,
    domain: str,
    default: typing.Callable | None = None,
): ...
def set_backend(backend, coerce: bool = False, only: bool = False) -> Untyped: ...
def skip_backend(backend) -> Untyped: ...
def get_defaults(f) -> Untyped: ...
def set_global_backend(backend, coerce: bool = False, only: bool = False, *, try_last: bool = False): ...
def register_backend(backend): ...
def clear_backends(domain, registered: bool = True, globals: bool = False): ...

class Dispatchable:
    value: Untyped
    type: Untyped
    coercible: Untyped
    def __init__(self, value, dispatch_type, coercible: bool = True): ...
    def __getitem__(self, index) -> Untyped: ...

def mark_as(dispatch_type) -> Untyped: ...
def all_of_type(arg_type) -> Untyped: ...
def wrap_single_convertor(convert_single) -> Untyped: ...
def wrap_single_convertor_instance(convert_single) -> Untyped: ...
def determine_backend(value, dispatch_type, *, domain, only: bool = True, coerce: bool = False) -> Untyped: ...
def determine_backend_multi(dispatchables, *, domain, only: bool = True, coerce: bool = False, **kwargs) -> Untyped: ...
