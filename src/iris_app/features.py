import pandas as pd

def filter_by_range(df: pd.DataFrame, col: str, min_v: float | None, max_v: float | None) -> pd.DataFrame:
    """Filter df to [min_v, max_v] on a numeric column. None means open bound."""
    if col not in df.columns:
        raise ValueError(f"Unknown column: {col}")
    out = df.copy()
    if min_v is not None:
        out = out[out[col] >= float(min_v)]
    if max_v is not None:
        out = out[out[col] <= float(max_v)]
    return out

def encode_target(df: pd.DataFrame) -> tuple[pd.DataFrame, pd.Series]:
    """Return X numeric features and y labels."""
    X = df[["sepal_length", "sepal_width", "petal_length", "petal_width"]]
    y = df["target_name"]
    return X, y