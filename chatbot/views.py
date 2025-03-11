from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as genai
from django.views.decorators.csrf import csrf_protect
import re


# Configure Gemini API
API_KEY = "Insert_Your_API_Key"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-pro-latest")

# Define patterns for queries you want to handle specially
DATE_PATTERNS = [
    r"what('s| is)? (the )?date",
    r"what day is (it|today)",
    r"today'?s date",
    r"current date"
]

TIME_PATTERNS = [
    r"what('s| is)? (the )?time",
    r"current time"
]

@csrf_protect
def chatbot_view(request):
    if request.method == "POST":
        user_input = request.POST.get("message", "").strip().lower()
        
        if user_input:
            # Check for date/time related queries and provide custom responses
            if any(re.search(pattern, user_input) for pattern in DATE_PATTERNS):
                return JsonResponse({
                    "response": "I'm focused on medical questions. How can I help you with a health-related topic?"
                })
            
            elif any(re.search(pattern, user_input) for pattern in TIME_PATTERNS):
                return JsonResponse({
                    "response": "I'm focused on medical questions. How can I help you with a health-related topic?"
                })
            
            # Add more custom responses here
            elif "who are you" in user_input or "what are you" in user_input:
                return JsonResponse({
                    "response": "I'm MediBot, an AI assistant designed to help with medical and health-related questions."
                })
                
            try:
                # For all other queries, use the Gemini API
                # You can add system instructions to guide the model's behavior
                system_instruction = """
                You are MediBot, a medical assistant chatbot. Focus only on providing health and medical information in detail
                - Do not provide information about dates, times, or non-medical topics
                - If asked about date or time, redirect to medical topics
                - Keep responses concise and helpful 
                - When uncertain, suggest consulting a healthcare professional
                """
                #u can add and write in detail to make it a detail responsive BOT
                # Generate response from Gemini with the system instruction
                response = model.generate_content(
                    [system_instruction, user_input]
                )
                
                return JsonResponse({"response": response.text})
                
            except Exception as e:
                # Handle API errors
                return JsonResponse({"response": "I'm sorry, I'm having trouble processing your request. How can I help you with a health-related question?"}, status=500)
    
    # Render the chat template for GET requests
    return render(request, "chatbot/chat.html")
