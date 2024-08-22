from scipy._typing import Untyped

pytestmark: Untyped
msg: str
sparse_params: Untyped

def check_sparse_version(min_ver) -> Untyped: ...
def sparse_cls(request) -> Untyped: ...
def graphs(sparse_cls) -> Untyped: ...
def test_csgraph_equiv(func, graphs): ...
def test_connected_components(graphs): ...
def test_laplacian(graphs): ...
def test_order_search(graphs, func): ...
def test_tree_search(graphs, func): ...
def test_minimum_spanning_tree(graphs): ...
def test_maximum_flow(graphs): ...
def test_min_weight_full_bipartite_matching(graphs): ...
def test_nonzero_fill_value(graphs, func, fill_value, comp_func): ...
