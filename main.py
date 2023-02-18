import re


class Main:
    # from chatterbot import ChatBot

    # chatbot = ChatBot("Chatpot")

    def main(self):
        exit_conditions = (":q", "quit", "exit")
        print(f"Bot:", "Please enter your name and email")

        name = input("      Name : ").strip()

        is_email_valid = False
        while (not is_email_valid):
            email = input("      Email : ").strip()
            is_email_valid = self.email_check(email)


        print(f"Bot:", "Hi ", name)
        print(f"Bot:", "How can I help you today?")

        while True:
            query = input("> ")
            if query in exit_conditions:
                print("Thank you for using out bot :)")
                break
            else:
                # print(f"🪴 {chatbot.get_response(query)}")

                print(query)

    def email_check(self, email):
        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        if (re.search(regex, email)):
            return True
        else:
            print("Email entered is not valid, Please enter a valid Email")
            return False


x = Main()
x.main()
