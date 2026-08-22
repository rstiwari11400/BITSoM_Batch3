from google import genai
from google.genai import errors
from Function_Folder1.myfunctions01 import print_colored_message

client = genai.Client(api_key="AQ.Ab8RN6JNm2fBoGd5ZTTGAwIyCb-CzPsJQRdHUlj_R8X_PJ3X3w")

question = input("Ask Gemini: ")

try:
    response = client.models.generate_content(
        model="gemini-3.1-flash-lite",
        contents=question
    )

    print_colored_message("Gemini: " + response.text, "green")

except errors.APIError as e:
    print("Gemini API error:", e)