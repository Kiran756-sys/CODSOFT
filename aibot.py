import tkinter as tk
from tkinter import scrolledtext

# Create a basic chatbot response function
def chatbot_response(user_input):
    user_input = user_input.lower()

    # Simple rules for the chatbot
    if "hello" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bunch of code, but thanks for asking! How about you?"
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that, but I'm here to help!"

# Function to handle sending messages
def send_message():
    user_input = user_entry.get()
    if user_input:
        chat_window.insert(tk.END, "You: " + user_input + "\n")
        response = chatbot_response(user_input)
        chat_window.insert(tk.END, "Chatbot: " + response + "\n\n")
        user_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Simple Chatbot")

# Create a text widget to display conversation history
chat_window = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=15, state='normal')
chat_window.pack(padx=10, pady=10)
chat_window.insert(tk.END, "Chatbot: Hello! Type your message below.\n\n")

# Create an entry widget for the user to type their message
user_entry = tk.Entry(root, width=40)
user_entry.pack(padx=10, pady=10, side=tk.LEFT)

# Create a button to send the message
send_button = tk.Button(root, text="Send", command=send_message)
send_button.pack(padx=10, pady=10, side=tk.RIGHT)

# Run the GUI event loop
root.mainloop()
