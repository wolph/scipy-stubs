from scipy._typing import Untyped

class _ScipyBackend:
    __ua_domain__: str
    @staticmethod
    def __ua_function__(method, args, kwargs) -> Untyped: ...

def set_global_backend(backend, coerce: bool = False, only: bool = False, try_last: bool = False): ...
def register_backend(backend): ...
def set_backend(backend, coerce: bool = False, only: bool = False) -> Untyped: ...
def skip_backend(backend) -> Untyped: ...
