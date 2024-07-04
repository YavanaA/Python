print("Hello World")
Numbers = []
count = 0
while True:
    for limit in range(10000):
        sum = 0
        Divisors = []
        for number in range(1, limit):
            if limit % number == 0:
                Divisors.append(number)
        for i in Divisors:
            sum = sum + i  
        if sum == limit:
            count = count + 1
            Numbers.append(limit)
    print(Numbers)
    response = input("Enter y to continue or other to exit : ")
    if response.lower() != "y":
        break

