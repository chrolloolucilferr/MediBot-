from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as genai

# Configure Gemini API
API_KEY = "Inser_Your_APIkey_here"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro-latest")

def chatbot_view(request):
    if request.method == "POST":
        user_input = request.POST.get("message", "")
        if user_input:
            response = model.generate_content(user_input)
            return JsonResponse({"response": response.text})
    return render(request, "chatbot/chat.html")
