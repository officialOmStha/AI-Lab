# Simple Rule-Based Chatbot

user = input("Enter your message: \n").strip().lower()

if user == 'hello' or user == 'hi':
    print("Hello there, How can i help you.")
elif user == 'bye'  or user =='sayonara':
    print("Goodbye !!")
else:
    print("I dont understand!")
