# import neccessary library
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

df = np.random.randn(5, 5)

c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("## Line Chart")
    st.line_chart(df)
with c2:
    st.markdown("## Area Chart")
    st.area_chart(df)
with c3:
    st.markdown("## Bar Chart")
    st.bar_chart(df)

arr1, arr2 = np.random.randn(100), np.random.randn(100)
arr3 = np.random.randint(1, 1001, 100)

c4, c5, c6 = st.columns(3)

with c4:
    fig, ax = plt.subplots()
    ax.set_title("Matpplotlib Scatter Plot")
    ax.scatter(arr1, arr2, s = arr3, c = arr3, alpha = 0.6)
    st.pyplot(fig)

with c5:
	fig, ax = plt.subplots()
	ax.set_title("Seaborn Scatter Plot")
	ax = sns.scatterplot(x = arr1, y = arr2)
	st.pyplot(fig)
        
with c6:
    fig = px.scatter(x = arr1, y = arr2, title='Plotly Scatter Plot')
    st.plotly_chart(fig, use_container_width=True)
    