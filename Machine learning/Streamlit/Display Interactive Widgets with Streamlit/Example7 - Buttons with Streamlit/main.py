# import neccessary library
import streamlit as st
import pandas as pd

st.button("Click button")

sample_data = {"Mammals": ['Cat', 'Dog', 'Bat', 'Fox', 'Pig'],
               "Birds": ["Parrot", "Eagle", "Duck", "Pegeon", "Vulture"]}

df = pd.DataFrame(sample_data)

st.dataframe(df)

if st.button("Click to show only mammals"):
    st.dataframe(df['Mammals'])
