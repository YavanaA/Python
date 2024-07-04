while True:
    def PrimeChecker(num):
        count = 0
        for i in range(1, num+1):
            if num % i == 0:
                count = count + 1
        if count > 2:
            print(f"{num} is composite number ")
        else:
            if num == 2:
                print(f"{num} is the only even prime number")  
            else:
                print(f"{num} is prime number")  
                    
    num = int(input("Enter a number : "))
    PrimeChecker(num)
    response = input("Enter y to continue or other to exit : ")
    if response.lower() != "y":
        break
