import sys
import csv
from tabulate import tabulate

def main():
     document = check_sys()
     print(tabulate(csv_reader(document), headers="keys", tablefmt="grid"))


def check_sys():
        if len(sys.argv) > 2:
            print("Too many command-line arguments")
            sys.exit(1)
        if len(sys.argv) < 2 :
            print("Too few command-line arguments")
            sys.exit(1)
        if  not sys.argv[1].endswith(".csv"):
            print("Not a CSV file")
            sys.exit(1)
        return sys.argv[1]

def csv_reader(document):
     try:
        pizza = []
        with open(document) as file:
            reader = csv.DictReader(file)
            for row in reader:
                 pizza.append(row)
        return pizza
     except(FileNotFoundError):
          print("File does not exist")
          sys.exit(1)

main()
