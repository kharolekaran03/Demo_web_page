import streamlit as st
import pandas as pd
st.title("Welcome to My website")
st.header("Demo Project ")
st.subheader("Project Code")
st.markdown(" Download and try you ")
st.code("""
import streamlit as st
import pandas as pd
st.title("Welcome to My website")
st.header("Demo Project ")
st.subheader("java")
st.markdown("I love Python")
st.code()
data = pd.read_csv("Data Accenture.csv")

st.dataframe(data)

name = st.text_input("Enter the your name:")
f_name = st.text_input("Enter your Father name:")
adr = st.text_area("Enter your text")
class_data = st.selectbox("Enter your Class :",("1st year","2nd year","3rd year","4th year"))

button = st.button("Done")
if button:
    st.markdown(f"""
         """ Name :{name}  
         Father Name : {f_name}
         address : {adr}
         class : {class_data}""")
""")"""
data = pd.read_csv("Data Accenture.csv")

st.dataframe(data)

name = st.text_input("Enter the your name:")
f_name = st.text_input("Enter your Father name:")
adr = st.text_area("Enter your text")
class_data = st.selectbox("Enter your Class :",("1st year","2nd year","3rd year","4th year"))

button = st.button("Done")
if button:
    st.markdown(f"""
         Name :{name}  
         Father Name : {f_name}
         address : {adr}
         class : {class_data}""")