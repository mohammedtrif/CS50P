
while True :
    try : 
        value = input("Fraction: ")
        x,y = value.split("/")
        x = int(x)
        y = int(y)
        if 0 <= x <= y and y > 0 :
            percentage = round(x /y * 100)
            if percentage >= 99:
                print("F")
                break
            elif percentage <= 1 :
                print("E")
                break
            else :
                print(f"{percentage}%")
                break
                

    except (ValueError,ZeroDivisionError) :
        pass
    

