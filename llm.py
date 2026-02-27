import os
from dotenv import load_dotenv
from litellm import completion

load_dotenv()

def call_llm(prompt):
    response = completion(
        model=os.getenv("MODEL_NAME"),
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4,
        api_key=os.getenv("GROQ_API_KEY")
    )

    return response["choices"][0]["message"]["content"]