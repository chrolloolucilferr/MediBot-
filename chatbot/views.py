from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as genai
from django.views.decorators.csrf import csrf_protect

# Configure Gemini API
API_KEY = "Inser_Your_APIkey_here"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro-latest")

@csrf_protect
def chatbot_view(request):
    if request.method == "POST":
        user_input = request.POST.get("message", "")
        if user_input:
            try:
                # Generate response from Gemini
                response = model.generate_content(user_input)
                return JsonResponse({"response": response.text})
            except Exception as e:
                # Handle API errors
                return JsonResponse({"response": f"I'm sorry, I encountered an error: {str(e)}"}, status=500)
    
    # Render the chat template for GET requests
    return render(request, "chatbot/chat.html")