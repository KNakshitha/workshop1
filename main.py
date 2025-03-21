import streamlit as st
st.title('hello world')
st.write('this is a simple program')

st.button('say hello')
st.text('hello streamlit')
st.text_input('Enter your name')

st.radio("gender",("male","female"),index=None)

if name:
    st.write(f'hello,{name}!')
if st.file_uploader('plz upload files:',type=['txt','csv']):
    st.write("thanks for uploading")
