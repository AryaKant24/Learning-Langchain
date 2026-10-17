from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

#schema

class Review(TypedDict):
    summary:str
    sentiment:str

structured_model = model.with_structured_output(Review)

response = structured_model.invoke("""
I’m writing this review after one week of use. 
The display and camera quality are good, and the phone is very handy and comfortable to use. 
However, the battery performance is a genuine concern. 
The battery no longer lasts a full day, and the phone heats up while charging and during continuous calls lasting more than 15–20 minutes. 
Overall, the phone has some good features, but the battery life and heating issues are disappointing.
""")

# print(response)
print(response['summary'])
print(response['sentiment'])
