import flights as f
from nltk.tokenize import word_tokenize
import random
class Bot:
    name = None
    email = None
    step = 0
    stage = "Start"
    def get_stage(self):
        if(Bot.name == None and Bot.email == None):
            return "no_name_no_email"
        elif(Bot.name != None and Bot.email == None ):
            return "no_email"
        elif(Bot.name != None and Bot.email != None):
            return "name_email"

    def bot_flow(self):
        stage = self.get_stage()
        print("stage",stage)
        if stage == "no_name_no_email":
            return "Please enter your name:"

    def find_origin_destination():
        pass
    def analyze_userText(self,userText):
        #Removing the entire usename and email.
        #separate the text into tokens

        #tokenized_word = word_tokenize(userText.lower)
        #print(tokenized_word)
        greetings_responses = ['Hi!', 'Hey, How can I help you today', 'Hello! I am TravelBot.', 'Hey there!']
        input = str(userText).lower()
        if input == "hi" or input == "hello":
            return random.choice(greetings_responses)
        if input == 'bye':
            return "Bye"
        
        step = Bot.step
        if step == 0:
            Bot.step+=1
            return 'Please enter your name'
        elif step ==1:
            #global name
            Bot.name = userText
            print(Bot.name)
            Bot.step+=1
            return 'Enter your email'
        elif step ==2:
            Bot.email = userText
            Bot.step+=1
            print(Bot.name)
            text = 'Hi {}, How can I help you today?'.format(Bot.name)
            return text 
        else:
            pass

        origin = 'MAD'
        destination = 'FCO'
        date = '2023-02-28'
        x =f.get_best_flights(origin,destination,date)
        return x 
        






