
text = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ") 
text1 = text.lower().strip()
if text1 == "42" or text1 == "forty two" or text1 == "forty-two" :
    print("Yes")
else : print("No")