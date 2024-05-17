import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI

template = """
    En dessous est un mail mal formulé.
    Ton but est de:
    - Formater professionellement le mail
    - Convertir le texte d'entrée dans un format spécifique
    - Convertir le texte d'entrée dans un français spécifique

    Ici sont des exemple de formats spécifiques:
    - Formel: Nous sommes allés à Barcelone pour le week-end. Nous avons énormément d'histoires à vous raconter.
    - Informel: On était à Barcelone ce weekend. Plein de choses à te raconter.

    Icic sont des exemple de mots dans différents dialectes:
    - Français: Bavarder, Petit ami, Petite ami, Portable, Diner, Partie
    - Québécois: Clavarder, Chum, Blonde, Cellulaire, Souper, Joute

    Exemple de phrases de chaque dialectes:
    - Français: J'aime embrassé mon petit ami. Cela n’a pas de sens.
    - Québécois: J’aime frencher mon chum !. Ça a pas d’allure ! 

    S'il vous plait, commencez le mail avec une chaleureuse introduction. Ajoutez une indroduction si besoin.
    
    En dessous, il y a le mail, le format et le dialecte:
    Format: {tone}
    Dialecte: {dialect}
    Mail: {email}
    
    YOUR {dialect} RESPONSE:
"""

prompt = PromptTemplate(
    input_variables=["tone", "dialect", "email"],
    template=template,
)

def load_LLM(openai_api_key):
    """Logic for loading the chain you want to use should go here."""
    # Make sure your openai_api_key is set as an environment variable
    llm = OpenAI(temperature=.7, openai_api_key=openai_api_key)
    return llm

st.set_page_config(page_title="Generateur de mail", page_icon=":robot:")
st.header("Generateur de mail")

col1, col2 = st.columns(2)

with col1:
  st.markdown("Régulièrement, les professionnels aimerait améliorer la qualité de leurs mails mais n'ont pas les compétences pour le faire. Cet outil vous aidera à améliorer vos compétences en écriture de mail en augmentant vos mails grâce à l'IA générative.")

with col2:
  st.image(image='TweetScreenshot.png', width=500, caption='https://twitter.com/DannyRichman/status/1598254671591723008')

st.markdown("## Ecrivez le mail à augmenter")

def get_api_key():
    input_text = st.text_input(label="OpenAI API Key ",  placeholder="Ex: sk-2twmA8tfCb8un4...", key="openai_api_key_input")
    return input_text

openai_api_key = get_api_key()

col1, col2 = st.columns(2)
with col1:
    option_tone = st.selectbox(
        'Which tone would you like your email to have?',
        ('Formal', 'Informal'))
    
with col2:
    option_dialect = st.selectbox(
        'Which English Dialect would you like?',
        ('American', 'British'))

def get_text():
    input_text = st.text_area(label="Email Input", label_visibility='collapsed', placeholder="Your Email...", key="email_input")
    return input_text

email_input = get_text()

if len(email_input.split(" ")) > 700:
    st.write("Please enter a shorter email. The maximum length is 700 words.")
    st.stop()

def update_text_with_example():
    print ("in updated")
    st.session_state.email_input = "Sally I am starts work at yours monday from dave"

st.button("*See An Example*", type='secondary', help="Click to see an example of the email you will be converting.", on_click=update_text_with_example)

st.markdown("### Your Converted Email:")

if email_input:
    if not openai_api_key:
        st.warning('Please insert OpenAI API Key. Instructions [here](https://help.openai.com/en/articles/4936850-where-do-i-find-my-secret-api-key)', icon="⚠️")
        st.stop()

    llm = load_LLM(openai_api_key=openai_api_key)

    prompt_with_email = prompt.format(tone=option_tone, dialect=option_dialect, email=email_input)

    formatted_email = llm(prompt_with_email)

    st.write(formatted_email)
