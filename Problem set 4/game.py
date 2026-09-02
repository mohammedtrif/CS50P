from random import randint
while True :
   try :
       n = int(input("Level: "))
       if n > 0 :
           secret = randint(1,n)
           break
       else :
           pass
   except ValueError :
       pass

while True :
    try:
        guess = int(input("Guess: "))
        if guess > 0 :
            if guess > secret :
                 print("Too large!")
            elif guess < secret :
                print("Too small!")
            elif guess == secret :
                print("Just right!")
                break
    except ValueError :
        pass