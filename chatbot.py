import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [r"my name is (.*)", ["Hello %1, nice to meet you!"]],
    [r"hi|hey|hello", ["Hello there!", "Hey!", "Hi! How can I help you?"]],
    [r"what is your name?", ["I am a chatbot created for the Codec Internship."]],

    # --- NEW RULES FOR CODEC ---
    [r"(.*)codec internship(.*)",
     ["The Codec Technologies internship is a great program to learn Python, Web Dev, and AI skills."]],
    [r"(.*)codec technologies(.*)",
     ["Codec Technologies is a software company providing training and internships in cutting-edge tech."]],
    [r"(.*)about codec(.*)",
     ["Codec Technologies offers internships to help students gain real-world coding experience."]],
    [r"(.*)python(.*)",
     ["Python is a versatile programming language used for Web Dev, AI, and Data Science. We are using it right now!"]],

    [r"how are you?", ["I'm doing well, thank you!", "I'm just a bot, but I'm functioning perfectly."]],
    [r"quit", ["Bye! Take care.", "Goodbye!"]],
    [r"(.*)", ["I'm sorry, I didn't quite understand that. Try asking about 'Codec' or 'Internship'."]]
]


def get_response(user_input):
    # Make input lowercase to match patterns easier
    chat = Chat(pairs, reflections)
    return chat.respond(user_input.lower())