from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

#added a chat history to maintain context 
chat_history = [
    SystemMessage(content = "You are a helpful assistant")
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content = user_input))
    if user_input == 'exit':
        break
    else:
        # response = model.invoke(user_input)
        response = model.invoke(chat_history)
        chat_history.append(AIMessage(content = response.text))
        print("AI: ",response.text)

print(chat_history)