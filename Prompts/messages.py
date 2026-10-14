from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

messages = [
    SystemMessage(content = "You are a helpful assistant. Keep your responses concise."),
    HumanMessage(content = "Tell me about dinosaurs")
]

response = model.invoke(messages)

messages.append(AIMessage(content = response.content))
print(messages)

#the defined roles help differentiate the stored chats