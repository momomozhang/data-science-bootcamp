import numpy as np
import pandas as pd
import streamlit as st


@st.cache_data
def load_data():
    data = pd.DataFrame(np.random.randint(1, 100, size=(10, 2)), columns=["Column 1", "Column 2"])
    return data


df = load_data()

st.header("Simple Data Summary App")
st.write("Here is a random dataset:")
st.write(df)

st.write(f"Sum of all numbers: {df.sum().sum()}")
st.write(f"Mean of all numbers: {df.mean().mean()}")

if "counter" not in st.session_state:
    st.session_state.counter = 0

if st.button("Increment Counter"):
    st.session_state.counter += 1

if st.button("Reset"):
    st.session_state.counter = 0

st.write(f"Counter: {st.session_state.counter}")
