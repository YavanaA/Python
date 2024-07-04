Limit = int(input("Enter a number : "))
for Num in range(1, Limit):
    if Num % 5 == 0 and Num % 3 == 0:
        print("FizzBuzz", end=" ")

    elif Num % 5 == 0:
        print("Buzz", end=" ")
    elif Num % 3 == 0:
        print("Fizz", end=" ")
    else:
        print(Num, end=" ")
