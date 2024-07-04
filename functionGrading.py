total = 0
while True:
    def GradeCalculator(mid, final):
        total = mid + final
        print(f"Total : {total}")
        if total >= 90:
            print("Grade : A+ ")
        elif total >= 85:
            print("Grade : A ")
        elif total >= 80:
            print("Grade : A- ")
        elif total >= 75:
            print("Grade : B+")
        elif total >= 70:
            print("Grade : B")
        elif total >= 65:
            print("Grade : B-")
        elif total >= 60:
            print("Grade : C+")
        elif total >= 55:
            print("Grade : C ")
        elif total >= 45:
            print("Grade : C- ")
        elif total >= 40:
            print("Grade : D ")
        else:
            print("Grade : F ") 

    mid = float(input("Enter the mid result : "))
    if mid < 0 or mid > 30:
        print("mid must be between 0 and 30")
    else:
        final = float(input("Enter the final result : "))
        if final < 0 or final > 70:
            print("Final must be between 0 and 70")
        else:
            GradeCalculator(mid, final)
    response = input("Enter y to continue or other to exit : ")
    if response.lower() != "y":
        break