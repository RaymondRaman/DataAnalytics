# import neccessary library
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sample_data = [3.12, -4.31, 6.76, -9.88, 1.09]
col1, col2, col3 = st.columns([3, 5, 3.8])

col1.subheader("Line Chart")
col1.line_chart(sample_data)

col2.subheader("Area Chart")
col2.area_chart(sample_data)

with col3:
    st.subheader("Bar Chart")
    st.bar_chart(sample_data)

df = pd.DataFrame(
    {"Mammal": ["Sea Lion", "Seal", "Walrus"], "Count": [3, 5, 2]})

st.dataframe(df)
with st.expander("Click to see a bar graph of the above data"):
    fig, ax = plt.subplots()
    ax.set_title("Mammal Count")
    ax = sns.barplot(x="Mammal", y="Count", data=df)
    st.pyplot(fig)
