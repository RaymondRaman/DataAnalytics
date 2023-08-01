import streamlit as st
import pandas as pd

# Metric
st.metric(label='Velocity in kilomtres per hour', value=75.4, delta=-2)

# Table
sample_data = {"Mammals": ["Cat", "Dog", "Pig"]}
df = pd.DataFrame(sample_data)
st.dataframe(df)
st.table(df)
st.json(sample_data)
