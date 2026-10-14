from langchain_groq import ChatGroq
from dotenv import load_dotenv, load_prompt
import streamlit as st

load_dotenv()

llm = ChatGroq(model="openai/gpt-oss-120b")

st.header('Research Tool')
user_input = st.text_input('Enter your prompt')

template = load_prompt('template.json')

if st.button('Summarise'):
    if not user_input.strip():
        st.warning('Enter a prompt before summarising.')
    else:
        chain = template | llm
        result = chain.invoke({
                'paper_input':paper_input,
                'style_input':style_input,
                'length_input':length_input
                }
            )
        st.write(result.content)