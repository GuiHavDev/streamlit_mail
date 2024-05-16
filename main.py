import streamlit as st

st.set_page_config(page_title="Generateur de mail", page_icon=":robot:")
st.header("My Header")

col1, col2, col3 = st.columns(3)

with col1:
  st.write("col1")

with col2:
  st.write("col2")

with col3:
  st.write("col3")
  #st.markdown("")
