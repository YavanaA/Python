#  a word said to be palindrome if its reverse gives another meaningful

Phrase = input("Enter a word or phrase :")
reversed = ""
for i in Phrase:
    reversed = i + reversed 
    
if reversed == Phrase:
    print(f"{Phrase} is  Palindrome word ")
else:
    print(f"{Phrase} is not Palindrome word")


