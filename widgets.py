import streamlit as st
import pandas as pd

name = st.text_input('Enter your name')
if name:
    st.write(f'Hello {name}')


# To create a slider for selecting age    
age = st.slider('Select your age', 0, 100, 25)
st.write(f'Your age is {age}')

#o create a select box for choosing a programming language
options = ['Python', 'Java', 'C', 'C++', 'JavaScript']
choice = st.selectbox('Choose your favorite programming language', options)
st.write(choice)
#Streamlit allows you to upload files, such as CSV files, and display their contents
uploaded_file = st.file_uploader('Choose a CSV file', type='csv')
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df)