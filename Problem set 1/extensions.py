
words = input("File name: ").lower().strip()
if words.endswith(".gif"):
    print("image/gif")
elif words.endswith(".jpg"):
    print("image/jpeg")
elif words.endswith(".jpeg"):
    print("image/jpeg")
elif words.endswith(".png"):
    print("image/png")
elif words.endswith(".pdf"):
    print("application/pdf")
elif words.endswith(".txt"):
    print("text/plain")
elif words.endswith(".zip"):
    print("application/zip")
else : print("application/octet-stream")