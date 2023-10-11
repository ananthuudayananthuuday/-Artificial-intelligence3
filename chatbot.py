import nltk
import random
from nltk.chat.util import Chat, reflections

# NLTK requires downloading some datasets
nltk.download("punkt")
nltk.download("averaged_perceptron_tagger")
nltk.download("vader_lexicon")

# Sample responses for the chatbot
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"what is your name?",
        ["I am a chatbot.",]
    ],
    [
        r"how are you",
        ["I'm good, thank you!", "I'm doing well, how about you?",]
    ],
    [
        r"quit",
        ["Bye, take care. Have a great day!", "It was nice talking to you. Goodbye!"]
    ],
    [
        r"(.*)",
        ["I'm sorry, I don't understand that.",]
    ]
]

# Creating the chatbot
def chatbot():
    print("Hello! I'm your chatbot. How can I assist you today?")
    chat = Chat(pairs, reflections)
    chat.converse()

# Calling the chatbot function
if __name__ == "__main__":
    chatbot()
