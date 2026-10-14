from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("HUGGINGFACEHUB_API_TOKEN") or os.getenv("HF_TOKEN")
if not token:
    raise RuntimeError(
        "Missing Hugging Face token. Add HUGGINGFACEHUB_API_TOKEN or HF_TOKEN to .env."
    )

llm = HuggingFaceEndpoint(
    repo_id="google/gemma-2-9b-it",
    task="text-generation",
    huggingfacehub_api_token=token,
)

model = ChatHuggingFace(llm=llm)

response = model.invoke("What is the capital of India?")

print(response.text)