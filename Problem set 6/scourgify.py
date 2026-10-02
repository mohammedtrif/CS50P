import csv
import sys

def main():
    input_file, output_file = check()
    after(input_file, output_file)




def check():
    if len(sys.argv) > 3 :
        print("Too many command-line arguments")
        sys.exit(1)
    if len(sys.argv) < 3 :
        print("Too few command-line arguments")
        sys.exit(1)
    return sys.argv[1], sys.argv[2]

def before(input_file):
    names = []
    try:
        with open(input_file) as file:
            reader = csv.DictReader(file)
            for row in reader:
                names.append(row)
        return names
    except FileNotFoundError:
        print(f"Could not read {input_file}")
        sys.exit(1)

def after(input_file, output_file):

    with open(output_file, "w", newline="") as file1:
        writer= csv.DictWriter(file1, fieldnames=["first", "last", "house"])
        writer.writeheader()
        for row in before(input_file):
            last, first = row["name"].split(",")
            last = last.strip()
            first = first.strip()
            writer.writerow({"first": first, "last": last, "house": row["house"]})
main()

