import re
def email_check(email):
    regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    email = "adjf@gmail.com"
    if (re.search(regex, email)):
        print("Valid Email")
    else:
        print("Invalid  Email")

email_check("")