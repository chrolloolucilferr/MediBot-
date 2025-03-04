import google.generativeai as genai

# Configure the API key
genai.configure(api_key="AIzaSyCezVSzqVz8cri8Jfzvuf4EEHqHUWi_tzs")

# List available models
models = genai.list_models()

print("Available Models:")
for model in models:
    print(model.name)
