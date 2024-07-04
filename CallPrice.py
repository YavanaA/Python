price = 3
while True:
    calls = int(input("Enter teh number of calls : "))
    if calls < 0:
        print("invalid number of calls !!!!")
    else:
        if calls < 30:
            pass
        elif calls > 30 and calls < 100:
            calls = calls - 30
            price = price + calls * 0.05

        elif calls >= 100 and calls < 200:
            calls = calls - 100
            price = price + 70 * 0.05 + calls * 0.03

        elif calls >= 200 and calls < 300:
            calls = calls - 200
            price = price + 70 * 0.05 + 100 * 0.03 + price*0.02
        response = input("Enter y to continue or other to exit : ")
        if response.lower() != "y":
            break

    
print("your price is ", price)
