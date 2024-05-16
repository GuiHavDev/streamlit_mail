import streamlit as st

st.set_page_config(page_title="Generateur de mail", page_icon=":robot:")
st.header("Generateur de mail")

col1, col2 = st.columns(2)

with col1:
  st.markdown("Régulièrement, les professionnels aimerait améliorer la qualité de leurs mails mais n'ont pas les compétences pour le faire. Cet outil vous aidera à améliorer vos compétences en écriture de mail en augmentant vos mails grâce à l'IA générative.")

with col2:
  st.write("col2")
