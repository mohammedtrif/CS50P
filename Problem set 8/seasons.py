from datetime import date
import inflect
import sys
import re
p = inflect.engine()


def main():
    result = input("Date of birth: ")
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", result):
        print("Invalid")
        sys.exit(1)

    try:
        birth = date.fromisoformat(result)
    except (ValueError):
        print("Invalid")
        sys.exit(1)

    result = minutes(birth)
    print(p.number_to_words(result, andword="").capitalize(), "minutes")


def minutes(birth):

    today = date.today()
    deltatime = today - birth
    return deltatime.days * 1440


if __name__ == "__main__":
    main()
