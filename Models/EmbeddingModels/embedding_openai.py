from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model = 'text-ambedding-3-large', dimensions=32)

documents = [
    "Delhi is the capital of India",
    "France is the capital of Paris",
    "Buenos Aires is the capital of Argentina"
]

result = embedding.embed_documents(documents)

print(str(result))

response = embedding.embed_query("Shanghai is the capital of China")

print(response)