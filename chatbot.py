print("Hi, I am a chatbot. How can I help you today?")

while True:
    user_input = input("You: ")
    
    if "hello" in user_input.lower():
        print("Chatbot: Hello there! How can I help you today?")
    elif "bye" in user_input.lower():
        print("Chatbot: Goodbye! Have a nice day.")
        break
    elif "what's your name" in user_input.lower():
        print("Chatbot: My name is Chatbot.")
    else:
        print("Chatbot: I am sorry, I don't understand what you're asking.")
