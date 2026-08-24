
def main() :
    time = convert((input("What time is it? ").split(":")))
    if 7 <= time <= 8 :
        print("breakfast time")
    elif 12 <= time <= 13 :
        print("lunch time")
    elif 18 <= time <= 19 :
        print("dinner time ")
    

def convert(t):
    x,y = t
    x = int(x)
    y = int(y)
    t = x + y/60 
    return float(t)

main()