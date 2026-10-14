from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-4o-mini")

reply = llm.invoke("What is the capital of India?")

print(reply.content)
