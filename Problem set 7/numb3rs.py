import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        result = re.fullmatch(r"([1-9])?([1-9])?(\d?)\.([1-9])?([1-9])?(\d?)\.([1-9])?([1-9])?(\d?)\.([1-9])?([1-9])?(\d?)", ip)
        result1 = result.group(0)
        x,y,z,n = str(result1).split(".")
        if 0 <= int(x) <= 255 and 0 <= int(y) <= 255 and 0 <= int(z) <= 255 and 0 <= int(n) <= 255 :
            return True
        else:
            return False
    except(AttributeError, ValueError):
        return False
if __name__ == "__main__":
    main()

