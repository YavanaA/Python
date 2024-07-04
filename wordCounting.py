Phrase = input("Enter a phrase or Sentence :")

while True:
    count = 1
    for letter in Phrase:
        if letter == " ":
            count = count + 1
        else:
            pass
        
    print(f"There are {count} words ")
    response = input("Enter y to continue or other to exit : ")
    if response.lower() != "y":
        break
            