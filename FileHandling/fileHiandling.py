# file1 = open("sampleFile.txt", "w")
# name = input("enter your name :")
# age = input("Enter your age :")
# job = input("Enter your job :")

# a = f" my name is {name}, I am {age},  my profession is {job}"
# introduction = " ".join(a)

# file1.write(introduction)
# file1.close()

file1 = open("sampleFile.txt", "r")
a = file1.read()
print(a)
file1.close()

