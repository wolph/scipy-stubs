from scipy._typing import Untyped
from scipy.sparse import coo_array as coo_array, csr_array as csr_array
from scipy.sparse._sputils import isscalarlike as isscalarlike

spcreators: Untyped
math_dtypes: Untyped

def toarray(a) -> Untyped: ...
def dat1d() -> Untyped: ...
def datsp_math_dtypes(dat1d) -> Untyped: ...

class TestArithmetic1D:
    def test_empty_arithmetic(self, spcreator): ...
    def test_abs(self, spcreator): ...
    def test_round(self, spcreator): ...
    def test_elementwise_power(self, spcreator): ...
    def test_real(self, spcreator): ...
    def test_imag(self, spcreator): ...
    def test_mul_scalar(self, spcreator, datsp_math_dtypes): ...
    def test_rmul_scalar(self, spcreator, datsp_math_dtypes): ...
    def test_sub(self, spcreator, datsp_math_dtypes): ...
    def test_add0(self, spcreator, datsp_math_dtypes): ...
    def test_elementwise_multiply(self, spcreator): ...
    def test_elementwise_multiply_broadcast(self, spcreator): ...
    def test_elementwise_divide(self, spcreator, dat1d): ...
    def test_pow(self, spcreator): ...
    def test_dot_scalar(self, spcreator, dat1d): ...
    def test_matmul(self, spcreator): ...
    def test_sub_dense(self, spcreator, datsp_math_dtypes): ...
    def test_size_zero_matrix_arithmetic(self, spcreator): ...
