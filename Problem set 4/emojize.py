import emoji

emo = input("Input: ")
emo1 = emoji.emojize(emo ,language ="alias" )
print(f"Output: {emo1}")