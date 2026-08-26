amount_due = 50
print("Amount Due: 50")
while amount_due > 0 :
    x = int(input("Insert coin: "))
    if x == 25 or x == 10 or x == 5 :
        amount_due = amount_due - x
        if amount_due > 0 :
            print(f"Amount Due: {amount_due}")
    else : print (f"Amount Due: {amount_due}")

change = abs(amount_due)
print(f"Change Owed: {change}")
