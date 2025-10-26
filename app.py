import streamlit as st
import numpy as np
import pandas as pd
st.title("Hello jii")

st.write("This is simple , bhosdu")
df = pd.DataFrame({'first column': [1, 2, 3, 4], 'second column': [10, 20, 30, 40]})
st.write('Here is the data frame:')
st.write(df)
# Streamlit allows you to create charts with minimal code. For example, to create a line chart:
chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=['a', 'b', 'c']
)
st.line_chart(chart_data)