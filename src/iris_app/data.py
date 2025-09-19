from sklearn.datasets import load_iris
import pandas as pd

# Define consistent feature names
FEATURE_NAMES = ["sepal_length", "sepal_width", "petal_length", "petal_width"]

def load_iris_df() -> pd.DataFrame:
    """
    Return the Iris dataset as a DataFrame with target and target_name.
    """
    # Load dataset from sklearn
    iris = load_iris(as_frame=True)

    # Copy into DataFrame
    df = iris.frame.copy()

    # Rename columns
    df.columns = FEATURE_NAMES + ["target"]

    # Map numeric target (0,1,2) to actual species name
    df["target_name"] = df["target"].map({i: name for i, name in enumerate(iris.target_names)})

    return df
