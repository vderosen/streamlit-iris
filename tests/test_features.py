import pytest
from iris_app.data import load_iris_df
from iris_app.features import filter_by_range, encode_target

def test_filter_by_range_keeps_bounds():
    df = load_iris_df()
    col = "petal_length"
    min_v, max_v = 2.0, 5.0
    fdf = filter_by_range(df, col, min_v, max_v)
    assert fdf[col].min() >= min_v - 1e-9
    assert fdf[col].max() <= max_v + 1e-9

def test_filter_unknown_column_raises():
    df = load_iris_df()
    with pytest.raises(ValueError):
        filter_by_range(df, "unknown", 0, 1)

def test_encode_target_shapes():
    df = load_iris_df()
    X, y = encode_target(df)
    assert X.shape[0] == y.shape[0]
    assert X.shape[1] == 4
    assert y.nunique() == 3
