import tkinter as tk
from tkinter import scrolledtext, messagebox
import google.generativeai as genai
import threading

class GeminiChatbotApp:
    def __init__(self, master):
        self.master = master
        master.title("Pearly AI Chatbot")
        master.geometry("500x600")
        master.configure(bg="#f0f0f0")

        # Configure API
        API_KEY = "AIzaSyCezVSzqVz8cri8Jfzvuf4EEHqHUWi_tzs"
        genai.configure(api_key=API_KEY)
        self.model = genai.GenerativeModel("gemini-1.5-pro-latest")

        # Chat Display Area
        self.chat_display = scrolledtext.ScrolledText(
            master, 
            wrap=tk.WORD, 
            width=60, 
            height=20, 
            font=("Arial", 10),
            state='disabled'
        )
        self.chat_display.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)

        # Input Frame
        input_frame = tk.Frame(master, bg="#f0f0f0")
        input_frame.pack(padx=10, pady=5, fill=tk.X)

        # User Input Entry
        self.user_input = tk.Entry(
            input_frame, 
            font=("Arial", 12), 
            width=40
        )
        self.user_input.pack(side=tk.LEFT, expand=True, fill=tk.X, padx=(0, 5))
        self.user_input.bind("<Return>", self.send_message)

        # Send Button
        send_button = tk.Button(
            input_frame, 
            text="Send", 
            command=self.send_message, 
            bg="#4CAF50", 
            fg="white"
        )
        send_button.pack(side=tk.RIGHT)

        # Welcome Message
        self.display_message("Pearly", "Hello! I'm Pearly, your AI assistant. How can I help you today?")

    def send_message(self, event=None):
        user_message = self.user_input.get().strip()
        if not user_message:
            return

        # Display user message
        self.display_message("You", user_message)
        
        # Clear input
        self.user_input.delete(0, tk.END)

        # Start a thread to get AI response
        threading.Thread(target=self.get_ai_response, args=(user_message,), daemon=True).start()

    def get_ai_response(self, user_message):
        try:
            # Generate AI response
            response = self.model.generate_content(user_message)
            
            # Display AI response in the main thread
            self.master.after(0, self.display_message, "Pearly", response.text)
        except Exception as e:
            # Display error message in the main thread
            self.master.after(0, self.display_message, "System", f"Error: {str(e)}")

    def display_message(self, sender, message):
        # Enable text widget to insert message
        self.chat_display.configure(state='normal')
        
        # Insert message with sender formatting
        self.chat_display.insert(tk.END, f"{sender}: ", "bold")
        self.chat_display.insert(tk.END, f"{message}\n\n")
        
        # Configure tags for formatting
        self.chat_display.tag_configure("bold", font=("Arial", 10, "bold"))
        
        # Scroll to the end
        self.chat_display.see(tk.END)
        
        # Disable text widget to prevent user editing
        self.chat_display.configure(state='disabled')

def main():
    root = tk.Tk()
    app = GeminiChatbotApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()