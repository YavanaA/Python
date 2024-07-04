import math 
Numbers = [2, 4, 5, 64, 45, 43, 343, 343, 33, 34]
sum = 0
for number in Numbers:
    sum = sum + math.pow(number, 2)
print(f"The sum of the square of the list is  {sum} ")
