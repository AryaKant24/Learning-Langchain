from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

#temperature controls the creativity and deterministic ability of the model
#0 - 0.3 = factual answers
#0.5 - 0.7 = general response
#0.9 - 1.2 - creative answers, storytelling
#1.5+ = wild and brainstorming

#max_completion_tokens = max words output. Helps financing.
model = ChatOpenAI(model = 'gpt-4', temperature = 0.3, max_completion_tokens = 50)

response = model.invoke("What is the capital of India?")

print(response)

#to print only answer
print(response.content)