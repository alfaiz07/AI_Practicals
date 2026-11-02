print("Chatbot: Hello! Welcome to Simple Chatbot.")
print("Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if "hello" in user or "hi" in user:
        print("Bot: Hello! How are you?")

    elif "name" in user:
        print("Bot: I am a Simple Chatbot.")

    elif "how are you" in user:
        print("Bot: I am fine. Thank you!")

    elif "help" in user:
        print("Bot: How can I help you?")

    elif "bye" in user:
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand.")