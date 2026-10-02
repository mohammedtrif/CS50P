import sys
import os
from PIL import Image, ImageOps

def main():
    check_args()
    input_file = sys.argv[1]
    output_file = sys.argv[2]
    try:
        photo = Image.open(input_file)
    except FileNotFoundError:
        sys.exit("Input does not exist")
    shirt = Image.open("shirt.png")
    size = shirt.size
    photo = ImageOps.fit(photo, size)
    photo.paste(shirt, shirt)
    photo.save(output_file)
def check_args():
    if len(sys.argv) < 3 :
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3 :
        sys.exit("Too many command-line arguments")
    valid_extensions = (".jpg", ".jpeg", ".png")
    input_ext = os.path.splitext(sys.argv[1])[1].lower()
    output_ext = os.path.splitext(sys.argv[2])[1].lower()

    if input_ext not in valid_extensions:
        sys.exit("Invalid input")
    if output_ext not in valid_extensions:
        sys.exit("Invaild output")
    if input_ext != output_ext:
        sys.exit("Input and output have different extensions")

if __name__ == "__main__" :
    main()
