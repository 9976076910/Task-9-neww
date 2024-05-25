import re

# RE for validating an email
regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'


# function for validating an Email
def check_em(email):
    # pass the regular expression and the string into the fullmatch() method
    if (re.fullmatch(regex, email)):
        print("Valid Email")

    else:
        print("Invalid Email")


# Driver Code
if __name__ == '__main__':

    # Enter the email
    email = "anju1234@gmail.com"

    # Check  the email
    check_em(email)

