from openai import OpenAI
from dotenv import load_dotenv
from pyparsing import Each

load_dotenv()          # reads OPENAI_API_KEY from .env
client = OpenAI()

prompt = "Suggest 5 clothing brand shop names inspired by love and bueaty. Each name should be unique, meaningful, and suitable for a wedding. Return the names with a short explanation of each name."

# gpt-4.1-mini supports temperature; some reasoning models (e.g. GPT-5) may not
for temp in [0, 0.7, 1.2]:
    print(f"\n--- temperature = {temp} ---")
    for _ in range(2):
        r = client.responses.create(
            model="gpt-5.4-mini",
            input=prompt,
            temperature=temp,
        )
        print(r.output_text)