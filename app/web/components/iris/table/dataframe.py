import streamlit as st
from services.iris.util import get_dataframe, get_mean_petal_length


def render_dataframe() -> None:
    df = get_dataframe()
    mean = get_mean_petal_length()
    st.dataframe(df)
    st.write(f"Mean petal length: {mean}")
    
