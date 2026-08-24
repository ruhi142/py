#chatbot concept used- 
#string - user input
#if else - to decide chatbot decission/reaponse
#dict - to store our words and theor response
#func- to organize that logic of chatbot
#loops - to keep going// bye- to exit


print("hello")

#chatbout memory creation wil be in dict

response = {
    "hello": "hi",
    "how are you": "i am good, how are you?",
    "who are you": "im a rule based chatbot",
    "happy": "thats good for you",
    "function": "a function is a block of code that us used to perform a soecific task",
    "bye": "bye, have a good day"
    }

def getResponseBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in response:
        if eachKey in userQuestion:
            return response[eachKey]
    return "i cant tell"
    
while True:
    userInput = input("enter your msg: ")
    reply = getResponseBot(userInput)
    print("bot response:", reply)

    if userInput.lower() == "bye":
        break