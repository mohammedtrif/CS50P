
foods = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0
while True :
    try:
        item = input("Item: ")
        price = foods[item.lower().title()]
        total += price
    except KeyError : 
        pass 
    except EOFError :
        break
    else:
        print(f"${total:.2f}")