import streamlit as st
import matplotlib.pyplot as plt
from services.iris.dataframe import get_dataframe
from services.iris.perceptron import get_target, get_train, fit

def render_perceptron() -> None:
    df = get_dataframe()
    target = get_target(df)
    train = get_train(df)
    perceptron = fit(train, target)
    plt.plot(range(1, len(perceptron.errors) + 1), perceptron.errors, marker='o')
    plt.xlabel('Epochs')
    plt.ylabel('Number of updates')
    st.pyplot(plt)
