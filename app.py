from flask import Flask, render_template, request
from bot_funtionality import Bot
# import main
app = Flask(__name__)
app.static_folder = 'static'


@app.route("/")
def home():
    return render_template("index.html")


def chatbot_response(userText):

    bot = Bot()
    response = bot.bot_flow()
    return response
    # based on stage we will call the function
    # bot_response, stage =
    # m = main.Main()
    #
    #pass



@app.route("/get/")
def get_bot_response():
    #userText -> bot need to understand this
    userText = request.args.get('msg')

    bot = Bot()
    result = bot.analyze_userText(userText)
    #analyse userText()

    return result #chatbot_response(userText) #userText#"Please enter your name and email"  # chatbot_response(userText)#"Akhil"   #
