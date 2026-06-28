import google.generativeai as genai

genai.configure(
    api_key="API_KEY"
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

response = model.generate_content(
    "What is entrepreneurship?"
)

print(response.text)