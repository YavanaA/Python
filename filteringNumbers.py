print("This program filters square of even and odd numbers entered")
limit = int(input(" how many numbers ar you want to filter : "))
EvensSquare = []
OddsSquare = []
for number in range(limit):
    if number %2 == 0:
        EvensSquare.append(number*number) 
    else:
        OddsSquare.append(number)
 
print(f"the square of the evens is {EvensSquare} ")       
print(f"the square of the odds is {OddsSquare} ")       