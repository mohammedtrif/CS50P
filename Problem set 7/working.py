import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    match = re.fullmatch(
        r"(\d{1,2})(?::(\d{2}))? (AM|PM) to "
        r"(\d{1,2})(?::(\d{2}))? (AM|PM)",
        s
    )

    if not match:
        raise ValueError

    h1, m1, period1, h2, m2, period2 = match.groups()

    h1 = int(h1)
    h2 = int(h2)

    if h1 < 1 or h1 > 12 or h2 < 1 or h2 > 12:
        raise ValueError

    if m1 is None:
        m1 = "00"

    if m2 is None:
        m2 = "00"

    if int(m1) > 59 or int(m2) > 59:
        raise ValueError

    if period1 == "AM":
        h1 = 0 if h1 == 12 else h1
    else:
        h1 = 12 if h1 == 12 else h1 + 12

    if period2 == "AM":
        h2 = 0 if h2 == 12 else h2
    else:
        h2 = 12 if h2 == 12 else h2 + 12

    return f"{h1:02}:{m1} to {h2:02}:{m2}"


if __name__ == "__main__":
    main()
