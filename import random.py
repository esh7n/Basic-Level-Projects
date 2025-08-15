import random


intents={}
     "greeting":{
        "keywords":["hello","hi","hey","greetings"],
        "responses":["Hello! How can I help you today?","Hi there! What can I do for you?","Hey! How's it going?"]
    },
    "goodbye":{
        "keywords":["bye","goodbye","see you","goodbye"],
        "responses":["Goodbye! Have a great day!","See you later! Take care!","Goodbye! Have a wonderful day!"]
    },
    "help":{
        "keywords":["help","assist","support","problem"],
        "responses":["I'm here to help! What do you need assistance with?"]
    },
    "joke":{
        "keywords":["joke","funny","humor","laugh"],
        "responses":["why don't scientists trust atoms?","because they make up everything!",
                     "A man was walking down the street and suddenly he fell on his back"]
    }


def detect_intent(user_input):

    #lowercase for matching
    user_input=user_input.lower()

    for intent, data in intents.items():
        for keyword in data ["keywords"]:
            if keyword in user_input:
                return intent
    return "unknown"


def get_response(user_input):
    intent=detect_ontent(user_input)
    if intent:
        return random.choice(intents[intent]["responses"])
    else:
        return "I'm sorry, I don't understand. Can you elaborate?"


def chatbot():
    print("Welcome to the chatbot! Type 'quit' to exit.")
     while True:
        user_input=input("You: ")
        if user_input.lower()=="quit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        response=get_response(user_input)
        print(f"Chatbot: {response}")

if __name__=="__main__":
     chatbot()
            
