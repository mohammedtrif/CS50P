text = input("Input: ")
result = ""
for char in text :
    if char.lower() in "aeiou" :
        continue
    else : result += char

print(f"Output: {result}")
