import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    try:
        result = re.search(r'<iframe.*?src="https?://(?:www\.)?youtube\.com/embed/(\w+)".*?></iframe>', s)


        if result :
            return f"https://youtu.be/{result.group(1)}"
        return None

    except (AttributeError):
            return None

if __name__ == "__main__":
    main()
