import random

# Function to greet the user
def greet():
    responses = ["Hello!", "Hi there!", "Hey!", "Greetings!"]
    return random.choice(responses)

# Function to respond based on user input
def respond(user_input):
    if "how are you" in user_input:
        return "I'm good, thank you!"
    elif "your name" in user_input:
        return "I am a chatbot."
    elif "bye" in user_input:
        return "Goodbye!"
    else:
        return "Sorry, I don't understand that."

# Function to simulate the chat
def chat():
    print("Bot: " + greet())
    while True:
        user_input = input("User: ")
        response = respond(user_input.lower())
        print("Bot:", response)
        if "bye" in user_input:
            break

# Main function to start the chatbot
if __name__ == "__main__":
    print("Welcome to the ChatBot demo!")
    chat()
