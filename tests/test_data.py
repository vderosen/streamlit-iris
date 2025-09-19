import pandas as pd
from iris_app.data import load_iris_df, FEATURE_NAMES

def test_load_shapes_and_columns():
    df = load_iris_df()
    assert isinstance(df, pd.DataFrame)
    assert set(FEATURE_NAMES + ["target", "target_name"]).issubset(df.columns)
    assert len(df) == 150
    assert df["target_name"].nunique() == 3
