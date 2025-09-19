import streamlit as st
import pandas as pd
from iris_app.data import load_iris_df, FEATURE_NAMES
from iris_app.features import filter_by_range, encode_target
from iris_app.model import fit_evaluate
from iris_app.viz import scatter

st.set_page_config(page_title="Iris Classifier", page_icon="🌸", layout="wide")

st.title("Iris mini project")
st.caption("Data import, filtering, simple model, and plots.")

# 1) Load
df = load_iris_df()
st.subheader("Data preview")
st.dataframe(df.head(10), use_container_width=True)

# 2) Filters
st.subheader("Filters")
with st.expander("Filter numeric ranges"):
    col = st.selectbox("Column", FEATURE_NAMES, index=2)
    cmin, cmax = float(df[col].min()), float(df[col].max())
    min_v, max_v = st.slider("Range", min_value=cmin, max_value=cmax, value=(cmin, cmax), step=0.1)
fdf = filter_by_range(df, col, min_v, max_v)

left, right = st.columns(2)
with left:
    st.metric("Rows after filter", len(fdf))
with right:
    st.write(f"Filtered on **{col}** in [{min_v:.2f}, {max_v:.2f}]")

# 3) Plot
st.subheader("Scatter plot")
x = st.selectbox("X", FEATURE_NAMES, index=2)
y = st.selectbox("Y", FEATURE_NAMES, index=3)
fig = scatter(fdf, x, y)
st.pyplot(fig, clear_figure=True)

# 4) Model
st.subheader("Train a simple classifier")
X, y = encode_target(fdf)
if len(fdf["target_name"].unique()) < 2:
    st.warning("Need at least 2 classes after filtering to train.")
else:
    pipe, acc = fit_evaluate(X, y, test_size=0.2, random_state=42)
    st.success(f"Holdout accuracy: {acc:.3f}")
    st.caption("Model: StandardScaler + Logistic Regression")
