import google.generativeai as genai

# Replace with your actual API key
API_KEY = "AIzaSyCezVSzqVz8cri8Jfzvuf4EEHqHUWi_tzs"
genai.configure(api_key=API_KEY)

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-pro-latest")  # You can also try "gemini-2.0-pro-exp"

print("\n🤖 Pearly AI Chatbot:\n Type 'ahhh' to stop.\n") #edit bot name

while True:
    user_input = input("You: ")
    
    if user_input.lower() == "ahhh":
        print("\nGoodbye! 👋") #last message
        break
    
    response = model.generate_content(user_input)
    print("\nPearly: ", response.text, "\n") #edit bot name
