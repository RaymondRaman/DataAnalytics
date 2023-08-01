# import neccessary library
import streamlit as st
import pandas as pd

number = st.sidebar.slider("Choose a number", min_value=-1.0, max_value=1.0,)
st.metric("Selected number", number)

with st.form("Order Form"):
    st.write("Order Details")
    fruit = st.select_slider(
        "Select a fruit", ["Banana", "Pawpaw", "Guava", "Mango"])

    quantity = st.number_input("Select the number of fruits", min_value=0)

    city = st.text_input("Type in your city")

    submitted = st.form_submit_button("Submit")

    if submitted:
        st.write(
            f"Your ordered {quantity} {fruit}(s) to be picked up at the {city} branch")

st.write(
    f"These values, {quantity}, {fruit} , and {city} that were set inside the form are acessible outside the form")
