import re
import random
import googlesearch

# Responses dictionary
responses = {
    "greeting": ["Hello! How can I assist you today?", "Hi there! What can I do for you?", "Hey! What brings you here?", "Howdy! What can I help you with?", "Hola! How can I assist you?"],
    "farewell": ["Goodbye! Have a great day!", "Farewell! Until next time!", "Bye! Take care!", "See you later! Have a good one!"],
    "thanks": ["You're welcome! Happy to help!", "No problem! Feel free to ask anything else!", "Anytime! Let me know if you need further assistance!"],
    "about_bot": ["I'm a simple chatbot designed to assist you with your queries.", "I'm here to help you with any questions you may have.", "I'm just a bot programmed to provide assistance and information."],
    "about_user": ["I'm sorry, but I don't have information about you. Could you tell me more?", "Unfortunately, I don't have access to personal information about users.", "I'm designed to respect user privacy, so I don't have details about you."],
    "age": ["I'm just a computer program, so I don't have an age.", "I don't age, thankfully!"],
    "creator": ["I was created by a team of developers.", "My creators are the brilliant minds behind me!"],
    "purpose": ["I'm here to help you with your queries.", "I exist to assist you in any way I can."],
    "weather": ["The weather is quite unpredictable.", "You might want to check a weather website for the latest forecast."],
    "jokes": ["Why don't scientists trust atoms? Because they make up everything!",
              "Parallel lines have so much in common. It's a shame they'll never meet!",
              "Why did the scarecrow win an award? Because he was outstanding in his field!"],
    "default": ["I'm not sure I understand.", "Could you please rephrase that?", "I'm sorry, I didn't get that."]
}

# Pattern-response pairs for matching
patterns = {
    r"(hello|hi|hey|howdy|hola)": "greeting",
    r"(goodbye|bye|see you|farewell)": "farewell",
    r"(thanks|thank you)": "thanks",
    r"(who are you|what are you|what can you do|tell me about yourself)": "about_bot",
    r"(what about me|tell me about me)": "about_user",
    r"(how old are you|what's your age)": "age",
    r"(who created you|who made you)": "creator",
    r"(what's your purpose|why do you exist)": "purpose",
    r"(what's the weather|how's the weather|weather)": "weather",
    r"(tell me a joke|say something funny)": "jokes"
}

def get_response(user_input):
    for pattern, response_key in patterns.items():
        if re.search(pattern, user_input, re.IGNORECASE):
            return random.choice(responses[response_key])
    return ask_chatgpt(user_input)

def ask_chatgpt(question):
    try:
        search_results = googlesearch.search(question, num=1, stop=1, pause=2)
        top_result = next(search_results)
        return top_result
    except Exception as e:
        print("Error:", e)
        return "I'm having trouble processing your request at the moment. Please try again later."

# Main function to handle user interaction
def chat():
    print("Welcome! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("Bot: Goodbye!")
            break
        response = get_response(user_input)
        print("Bot:", response)

# Run the chat
if __name__ == "__main__":
    chat()
