#  a word said to be anadrome if its reverse gives another meaningful
Phrase = input("Enter a word or phrase :")
reversed = ""
for i in Phrase:
    reversed = i + reversed 
    
if reversed == Phrase:
    print(f"{Phrase} is  anadrome word ")
else:
    print(f"{Phrase} is not anadrome word")


#   another way to this is 

# a = len(Phrase)
# for letter in Phrase[a::-1]:
#     print(letter, end="")