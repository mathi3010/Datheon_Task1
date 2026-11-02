from dotenv import load_dotenv
from google import genai
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

print("Testing Gemini connection...")

try:
    response = client.models.generate_content(
        model="gemini-3.8-flash",
        contents="Reply with only the word SUCCESS."
    )

    print("Gemini response:", response.text)

except Exception as error:
    print("Connection failed:", type(error).__name__)
    print(error)