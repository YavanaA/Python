def Grading(assignment, mid, final):
    total = assignment + mid + final
    
    if total >= 90:
        grade = "A+"

    elif total >= 85:
        grade = "A"
    elif total >= 80:
        grade = "A-"
    elif total >= 75:
        grade = "B"
    elif total >= 70:
        grade = "C"
        
    return grade 


assignment = int(input("Enter the assignment :"))
if assignment < 0 or assignment > 20:
    print("assignment must be between 0 and 20")
else:
    mid = int(input("enter the mid result :"))
    if mid < 0 or mid > 30:
        print("mid must be between  0 and 30")
    else:
        final = int(input("Enter the final result :"))
        if final < 0 or final > 50:
            print("final must be between 0 and 50")
        else:
            Grading(assignment, mid, final) 
            
            
    
