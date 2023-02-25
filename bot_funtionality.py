class Bot:
    name = None
    email = None
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

    def analyze_userText(self,userText):
        #stage1 = Bot.stage
        print(userText, "Checking user text ", Bot.stage)
        if(Bot.stage == "no_name_no_email"):
            print("Expecting name")
            Bot.stage =="expecting_name"
            print(Bot.stage)
            return "Please enter name"
        elif(Bot.stage == "expecting_name"):
            Bot.name = userText
            print("user name is: ", Bot.name)
            return "username is",Bot.name






