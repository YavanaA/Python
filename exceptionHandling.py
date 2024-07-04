               
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Division by zero!")
except ValueError:
    print("Error: Please enter valid integers.")
except Exception as e:
    print("An error occurred:", e)
else:
    print("No error occurred.")
finally:
    print("Execution completed.")