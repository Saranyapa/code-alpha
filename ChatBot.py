import nltk
import random
from nltk.chat.util import Chat, reflections

# Define some patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hi there!', 'Hey!']),
    (r'how are you?', ['I am doing well, thank you!', 'I\'m fine, thanks!', 'All good!']),
    (r'what\'?s your name?', ['You can call me Chatbot.', 'I\'m Chatbot, nice to meet you!']),
    (r'bye|goodbye', ['Goodbye!', 'See you later!', 'Bye!']),
    (r'i need (.*)', ['Why do you need %1?', 'What do you need %1 for?']),
    (r'(.*) (weather|temperature) (.*)',
     ['Weather forecast is not available right now.', 'You can check the weather online.']),
    (r'(.*)', ['I\'m sorry, I didn\'t understand that.', 'Can you please elaborate?'])
]

# Create a chatbot
def chatbot():
    print("Welcome! I'm Chatbot. How can I help you today?")
    chat = Chat(patterns, reflections)
    while True:
        user_input = input("You: ")
        response = chat.respond(user_input)
        print("Chatbot:", response)
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

# Run the chatbot
if __name__ == "__main__":
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    chatbot()
