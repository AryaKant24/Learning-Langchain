from langchain_groq import ChatGroq
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional, Literal

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-120b")

#schema

class Review(TypedDict):
    key_themes: Annotated[list[str], 'Write down all the key themes mentioned in the review']
    summary:Annotated[str, 'A brief summary of the review']
    sentiment:Annotated[Literal["+", "-"], '  Return sentiment of the review: either positive, negative or neutral']
    pros:Annotated[Optional[list[str]], 'Write down all the pros']
    cons:Annotated[Optional[list[str]], 'Write down all the cons']

structured_model = model.with_structured_output(Review)

response = structured_model.invoke("""
    This shoe is having a manufacturing defect. Now the catch here is that you will only find it when you go on first run, and you will not even able to return it then.

I have been running marathons regularly and this is first time in my life that I came across such a defect.

The right sole is more depressed than left one so it will give you pain in legs and knees due to the mismatch.

I have written to Nike also, and writing it here as well so that you may not order wrong shoes.

For me this shoe is a waste as even if they do not replace, I will have to order new ones for me because these will give me knee and leg pain.
""")

print(response['sentiment'])