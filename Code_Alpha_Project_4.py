"""
Basic Rule-Based Chatbot
- Responds to common greetings and questions
- Maintains simple conversation flow
- Easy to extend with new rules
"""

def initialize_chatbot():
    """Initialize the chatbot with response rules"""
    return {
        "greetings": {
            "hello": ["Hi there!", "Hello!", "Hey!"],
            "hi": ["Hello!", "Hi!", "Hey there!"],
            "hey": ["Hi!", "Hello!", "What's up?"]
        },
        "farewells": {
            "bye": ["Goodbye!", "See you later!", "Bye!"],
            "goodbye": ["Farewell!", "Have a nice day!", "Goodbye!"],
            "exit": ["Chat session ended", "Goodbye!", "See you next time!"]
        },
        "questions": {
            "how are you": ["I'm just a program, but I'm functioning well!", 
                           "All systems operational!", "I don't have feelings, but thanks for asking!"],
            "what's your name": ["I'm ChatBot 1.0", "Call me CB", "I'm your friendly neighborhood chatbot"],
            "help": ["I can respond to greetings like hello/hi", 
                    "Try asking how I am or what my name is",
                    "Say bye to end our chat"]
        }
    }

def get_response(message, response_rules):
    """Generate appropriate response based on user input"""
    message = message.lower().strip()
    
    for pattern in response_rules["greetings"]:
        if pattern in message:
            return random.choice(response_rules["greetings"][pattern])
    
    for pattern in response_rules["farewells"]:
        if pattern in message:
            return random.choice(response_rules["farewells"][pattern])
    
    for pattern in response_rules["questions"]:
        if pattern in message:
            return random.choice(response_rules["questions"][pattern])
    
    return "I'm not sure how to respond to that. Try saying hello or asking for help."

def chat_session():
    """Run the chatbot interaction loop"""
    response_rules = initialize_chatbot()
    
    print("\n" + "="*40)
    print("CHATBOT 1.0".center(40))
    print("="*40)
    print("\nType 'bye' or 'exit' to end the chat")
    print("Try saying hello or asking how I am!\n")
    
    while True:
        user_input = input("You: ")
        response = get_response(user_input, response_rules)
        
        print(f"Bot: {response}")
        
        if any(exit_word in user_input.lower() 
               for exit_word in ['bye', 'goodbye', 'exit']):
            break

if __name__ == "__main__":
    import random
    try:
        chat_session()
    except KeyboardInterrupt:
        print("\nChat session ended unexpectedly")
    except Exception as e:
        print(f"\nAn error occurred: {e}")