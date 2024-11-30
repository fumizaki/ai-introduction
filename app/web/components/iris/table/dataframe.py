import streamlit as st
from services.iris.dataframe import get_dataframe, get_mean


def render_dataframe() -> None:
    df = get_dataframe()
    sepal_length_mean = get_mean(df, "SepalLengthCm")
    sepal_width_mean = get_mean(df, "SepalWidthCm")
    petal_length_mean = get_mean(df, "PetalLengthCm")
    petal_width_mean = get_mean(df, "PetalWidthCm")
    st.dataframe(df)
    st.write(f"Mean sepal length: {sepal_length_mean}")
    st.write(f"Mean sepal width: {sepal_width_mean}")
    st.write(f"Mean petal length: {petal_length_mean}")
    st.write(f"Mean petal width: {petal_width_mean}")
    
