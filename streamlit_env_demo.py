import os
import polars as pl
import streamlit as st

keys: list[str] = []
values: list[str] = []

for key in os.environ:
    value = os.environ.get(key)
    keys.append(key)
    values.append(value)

env_vars_df = pl.DataFrame({
    "environment_variable": keys,
    "value": values,
})
st.dataframe(env_vars_df)

st.dataframe(pl.DataFrame({
    "path": os.listdir(".git"),
}))
