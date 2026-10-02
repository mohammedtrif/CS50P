import re
import sys


def main():
    print(count(input("Text: ")))



def count(s):
    result = re.findall(r"\bum\b" , s, re.I)
    total= 0
    for um in result:
        total += 1
    return total


if __name__ == "__main__":
    main()
