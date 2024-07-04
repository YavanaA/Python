import random

# Generate a random integer between 1 and 100
print("Enter your guess between 1 and 10 ")
count = 0
guessCount = 1
for i in range(10):
    random_number = random.randint(1, 10)
    guess = int(input(f"Enter guess {guessCount}  : "))
    if guess < 1 or guess > 10:
        print("The guess must be between 1 and 10")
        quit()
    else:
       
        if guess == random_number:
            print("You got it!!")
            count += 1
        else:
            print('you lose it ')
            print(f"The secret number is {random_number} ")
            
    guessCount = guessCount + 1
print(f" You got {count} out of 10")
