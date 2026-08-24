
math = input("Expression: ")
math1 = math.split(" ")
x, y, z = math1

x = int(x)
z = int(z)

if y == "+" :
    print(float(x + z))
elif y == "-" :
    print(float(x - z))
elif y == "/" :
    print(float(x / z))
elif y == "*" :
    print(float(x * z))