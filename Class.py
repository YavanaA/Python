class Student:
    def __init__(self, Name, Age, Id, Department, Mark):
        self.name = Name
        self.age = Age
        self.id = Id
        self.department = Department
        self.mark = Mark

    def introduction(self):
        print("")
        print(f" Hello Every one MY name is {self.name}")
        print(f"I am {self.age} years old")

    def Studying(self):
        print(f" Currently , I am studying {self.department}") 

        
while True:
    Name = input("\nEnter you name : ")
    Age = input("Enter your age : ")
    Id = input("Enter you Id number : ")
    Department = input("Enter your department :")
    Mark = input("Enter your Score :")
    
    a = Student(Name, Age, Id, Department, Mark)
    a.introduction()
    a.Studying()
    print("My Id Number is ", a.id)
    print("My score is ", a.mark)
    
    response = input("\nEnter y to continue and other to exit : ")
    if response.lower() != 'y':
        break
