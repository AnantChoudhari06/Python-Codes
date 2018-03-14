import re

def validate():
    while True:
        password = input("Enter a password: ")
        if len(password) < 6:
            print("Make sure your password is at lest 8 letters")
        elif re.search('[0-9]',password) is None:
            print("Make sure your password has a number in it")
        elif re.search('[A-Z]',password) is None: 
            print("Make sure your password has a capital letter in it")
        elif re.search('[a-z]',password) is None: 
            print("Make sure your password has a lower letter in it")
        else:
            print("Your password seems fine")
            break

validate()
