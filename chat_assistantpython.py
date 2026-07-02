print("~~Welcome to your billu chatbot~~")
print("You can ask me any basic question,Type bye to exit from bot")
#chatbot memory creation
responses={"hello":"Hi!Welcome How can I help you?","How are you":
    "I am amazing.Thank You!","Who are you?":"I am BILLU",
    "Motivate me?":"Every bug of the project make you better.Keep Going!"}

#method function to get the response
def getResponseofBot(userQuestion):
    userQuestion=userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
    return "I am still in learning mode ,Sorry"


#Take user input:
while True:
    userInput=input("Please ask your question:")
    reply=getResponseofBot(userInput)
    print("Bot response:",reply)

    if "bye" in userInput.lower():
        break
    
