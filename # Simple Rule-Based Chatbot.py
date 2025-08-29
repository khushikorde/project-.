# Simple Rule-Based Chatbot

def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "your name" in user_input:
        return "I am your AI internship chatbot."
    elif "bye" in user_input:
        return "Goodbye! Have a great day!"
    elif "help" in user_input:
        return "Sure! I can answer simple questions like greetings, name, etc."
    else:
        return "Sorry, I don't understand that. Can you try again?"

print("Chatbot: Hi! Type 'bye' to exit.")
while True:
    user = input("You: ")
    if user.lower() == "bye":
        print("Chatbot:", chatbot_response(user))
        break
    print("Chatbot:", chatbot_response(user))
