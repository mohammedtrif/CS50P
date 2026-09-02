from random import randint


def main():
    score = 0
    level = get_level()

    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        answer = x + y
        correct = False

        for _ in range(3):
            try:
                user_answer = int(input(f"{x} + {y} = "))

                if user_answer == answer:
                    score += 1
                    correct = True
                    break
                else:
                    print("EEE")

            except ValueError:
                print("EEE")

        if not correct:
            print(f"{x} + {y} = {answer}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            level = int(input("Level: "))

            if level in [1, 2, 3]:
                return level

        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return randint(0, 9)

    elif level == 2:
        return randint(10, 99)

    elif level == 3:
        return randint(100, 999)

    else:
        raise ValueError


if __name__ == "__main__":
    main()