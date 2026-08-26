text = input("Enter text: ")

result = ""
for char in text :
    if char.isupper():
        result += "_" + char.lower()
    else : result += char
print(f"snake_case: {result}")