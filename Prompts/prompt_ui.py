from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3.8-flash")

st.header('Research Tool')
user_input = st.text_input('Enter your prompt')

if st.button('Summarise'):
    if not user_input.strip():
        st.warning('Enter a prompt before summarising.')
    else:
        result = llm.invoke(user_input)
        st.write(result.content)