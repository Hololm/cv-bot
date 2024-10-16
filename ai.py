from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

messages = [
    {
        "role": "system",
        "content": (
            "You are designed to analyze a person's resume, and return a cover letter for the specified company."
            "The format for the user's prompt will be name of company, today's date, the job description, and the resume."
            "The cover letter you produce should be something highlighting the person's skills, potential to do well, and"
            "how it aligns with the company values and fits the job description, using certain keywords from the"
            "description."
        ),
    },
    {
        "role": "user",
        "content": (
            ""
        ),
    },
]

client = OpenAI(api_key=os.getenv("PERPLEXITY_KEY"), base_url="https://api.perplexity.ai")

# chat completion without streaming
response = client.chat.completions.create(
    model="llama-3-sonar-large-32k-online",
    messages=messages,
)
print(response)

# chat completion with streaming
response_stream = client.chat.completions.create(
    model="llama-3-sonar-large-32k-online",
    messages=messages,
    stream=True,
)
for response in response_stream:
    print(response)
