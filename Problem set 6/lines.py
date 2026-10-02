import sys
def main():
        text = cla()
        print(python(text))


def cla():
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    if len(sys.argv) > 2 :
        print("Too many command-line arguments")
        sys.exit(1)
    if len(sys.argv) == 2 and not sys.argv[1].endswith(".py"):
        print("Not a Python file")
        sys.exit(1)
    if len(sys.argv) == 2 and  sys.argv[1].endswith(".py") :
        return sys.argv[1]



def python(text):
    count = 0
    try:
        with open(text) as file:
            lines = file.readlines()
            for line in lines:
                 if line.lstrip().startswith("#"):
                    continue
                 if line.isspace() or line == "\n":
                    continue
                 else: count += 1
            return count
    except (FileNotFoundError):
            print("File does not exist")
            sys.exit(1)

main()


