from google import genai
from google.genai import errors

client = genai.Client(api_key="APIKey")

question = input("Ask Gemini: ")

try:
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=question
    )

    print("Gemini: " + response.text)

except errors.APIError as e:
    print("Gemini API error:", e)