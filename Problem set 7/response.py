from validator_collection import validators
from validator_collection.errors import InvalidEmailError

def check(s):
    try:
        if validators.email(s):
            return "Valid"
        else:
            return "Invalid"
    except InvalidEmailError:
        return "Invalid"

print(check(input("What's your email address? ").strip()))
