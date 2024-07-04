Numbers = []
count = 0 
for i in range(100, 500):
    if i % 5 == 0 and i % 7 == 0:
        count = count + 1
        Numbers.append(i)
print(f"{count} numbers are divisible by 5 and 7 from 100 up 500")
print( f" These are : {Numbers}")