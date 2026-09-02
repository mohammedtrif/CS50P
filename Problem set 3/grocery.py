items = {}
while True :
    try :
        item = input("")
        item = item.lower()
        if item in items :
                items[item] += 1
        else : items[item] = 1
    except EOFError :
         break

for item in sorted(items):
    print(items[item], item.upper())