def SimpleCalculator(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Zero Division Error !!!")
            return
        else:
            return num1 / num2
    else:
        print("invalid operator!!")
        return


num1 = float(input("Enter the first number : "))
operator = input("enter the operator :  ")
num2 = float(input("Enter the  second number : "))


result = SimpleCalculator(num1, operator, num2)
print(f"The result is {result} ")


print("")