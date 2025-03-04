import google.generativeai as genai

# Replace with your actual API key
API_KEY = "AIzaSyCezVSzqVz8cri8Jfzvuf4EEHqHUWi_tzs"
genai.configure(api_key=API_KEY)

# Use the correct model name
model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Or try "gemini-2.0-pro-exp"

# Generate content
prompt = "Tell me an interesting AI fact."
response = model.generate_content(prompt)

# Print the response
print("\n🤖 Gemini AI Response:\n")
print(response.text)
