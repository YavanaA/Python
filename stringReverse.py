Phrase = input("Enter a  word or phrase :")

reversed = ""
for i in Phrase:
    reversed = i + reversed 
print(reversed)


#   another way to this is 

# a = len(Phrase)
# for letter in Phrase[a::-1]:
#     print(letter, end="")