'''
            💐💐 Welcome Here🌱🌷

This program  is a student Management system in a University or college
That allows:
        => the students - to select their department
                        - to know their priority form all students
                        - to know their priority in one department
                        - to change their password
                        
        => the admin    -  To Add new user 
                        -  To change password of admin
                        -  To Search a user or users
                        -  To Delete a user or users 
                        -  To display users 
                        -  To update users information
                        -  To set limit of the intake capacity 
                        
        🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻🌻                 
        🌺 Developed By:                    💐
        🌺         Hailemeskel Getaneh      💐
        🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿🌿

'''

import os

admin = "DBU1234"
Default = "12345678"

SoftwareStudents = []
limitSE = 3
ComputerScienceStudents = []
limitCS = 3
DataScienceStudents = []
limitDS = 3
InformationSystemStudents = []
limitIS = 3
InformationTechnologyStudents = []
limitIT = 2

studentPassword = ""
student = {}
student = student in SoftwareStudents

StudentsList = [
    {'name': "Hailemeskel Getaneh", "ID": "DBU1501246", 'score': 90, 'password': 1234},
    {'name': "Hailemariam Kassaw", "ID": "DBU1501245", 'score': 94, 'password': 1235},
    {'name': "Abebe Kebede", "ID": "DBU1501239", 'score': 87, 'password': 1111},
    {'name': "Nigus Tatek", "ID": "DBU1501244", 'score': 96, 'password': 2222},
    {'name': "Hailemeskel Kebede",  "ID": "DBU1501240", 'score': 90, 'password': 3333},
    {'name': "Hanna Selemon", "ID": "DBU1501241", 'score': 80, 'password': 4444},
    {'name': "Girum Ermiyas", "ID": "DBU1501242", 'score': 85, 'password': 5555},
    {'name': "Abiy Ahimed", "ID": " DBU1501243", 'score': 56, 'password': 6666},
    {'name': "Selamawit Ayele", "ID": "DBU1501238", 'score': 78, 'password': 7777},
    {'name': "Girma Geremew", "ID": "DBU1501237", 'score': 76, 'password': 8888},
    {'name': "Martemuz Zemedkun", "ID": "DBU1501236", 'score': 100, 'password': 9999},
    {'name': "Betelhem Debebe", "ID": "DBU1501235", 'score': 86, 'password': 0000}
]

new = {'name': "Dagnachew Kebede", "ID": "DBU15012347", 'score': 95, 'password': 1212}
StudentsList.append(new)
new1 = {'name': "Alemu Alemneh", "ID": "DBU1501250",
        'score': 67, 'password': 2323}
StudentsList.append(new1)
admin = "DBU1234"

# Adding a new student to the list of Students
    
    
def adminActivities():
    print("1. To Add new user :")
    print("2. To change password :")
    print("3. To Search a user or users:")
    print("4. To Delete a user or users :")
    print("5. To display users :")
    print("6. Set the intake capacity")
    
    
def addNewStudent():
    Name = input("Enter the name of the student  : ")
    Id = input("Enter the students' Id  : ")
    Score = input("Enter the score : ")
    for student in StudentsList:
        if student["ID"] == Id:
            print("This Id already exists!!")
            break
        else:
            NewStudent = {'name': Name, "ID": Id,
                    'score': Score, 'password': Default}
            print("New Student added successfully !!!")
            StudentsList.append(NewStudent)
            break

# Change the  admin Password


def ChangeAdminPassword():
    global admin
    password = input("Enter the previous  password : ")
    if password == admin:
        newPassword = input("Enter you password : ")
        confirmNewPassword = input("Confirm your Password : ")
    if newPassword == confirmNewPassword:
        admin = newPassword
    else:
        print("you Entered to different password")
        os.system("cls")
        exit()

# search users or students by Id , Name or Score


def SearchUser():
    print("1. search by Name ")
    print("2. search by Id ")
    print("3. search by Score ")
    choice = input("\n Enter you choice : ")

    def DisplaySearched():
        count = 1
        print(" No. \t\tName \t\t   ID \t\t Score")
        for i in searched:
            space1 = 23 - len(i['name'])
            space2 = 15 - len(i["ID"])
            print(count, ".\t", i['name'], " "*space1, i['ID'], " "*space2,  i['score'])
            count = count + 1

    searched = []
    if choice == '1':
        count = 0
        Name = input(" Enter the Name of the user : ")
        names = []
        for student in StudentsList:
            names.append(student["name"])

        for Student in StudentsList:
            if Name in names:
                if Student["name"] == Name:
                    count = count + 1
                    searched.append(Student)
                else:
                    pass
            else:
                print("No result found")
                break
        if count != 0:
            print(f"\n{count} results found ")
            DisplaySearched()
        else:
            pass

    elif choice == '2':
        count = 0
        Id = input(" Enter the Id of the user : ")
        IDs = []
        for student in StudentsList:
            IDs.append(student["ID"])
        for Student in StudentsList:
            if Id in IDs:
                if Student["ID"] == Id:
                    count = count + 1
                    searched.append(Student)
                else:
                    pass
            else:
                print("No result found")
                break
        if count != 0:
            print(f"{count} results found ")
            DisplaySearched()
        else:
            pass

    elif choice == '3':
        count = 0
        score = int(input(" Enter the Score of the student : "))
        scores = []
        for student in StudentsList:
            student["score"] = int(student["score"])
            scores.append(student["score"])

        for Student in StudentsList:
            if score in scores:
                if Student["score"] == score:
                    count = count + 1
                    searched.append(Student)
                else:
                    pass
            else:
                print("No result found")
                break
        if count != 0:
            print(f"{count} results found ")
            DisplaySearched()
        else:
            pass
    else:
        print("invalid choice ")
        os.system("cls")
        exit()


def DeleteUsers():

    Id = input("Enter the Id number to delete : ")
    for Student in StudentsList:
        if Id in Student["ID"]:
            if Student["ID"] == Id:
                confirmId = input("Confirm the Id : ")
                if confirmId == Id:
                    caution = input(
                        "Do You Want to delete permanently ? write yes or no :")
                    if caution.lower() == "yes":
                        StudentsList.remove(Student)
                        print("User deleted successfully!!")
                    else:
                        pass
        else:
            print("No result found  to delete")
            break

# limit the intake capacity of a department


def checkingPresence():
    global student, SoftwareStudents
    global SoftwareStudents, ComputerScienceStudents, DataScienceStudents
    global InformationSystemStudents, InformationTechnologyStudents
    
    if student in SoftwareStudents:
        SoftwareStudents.remove(student)
    else:
        pass
    if student in ComputerScienceStudents:
        ComputerScienceStudents.remove(student)
    else:
        pass        
    if student in DataScienceStudents: 
        DataScienceStudents.remove(student)
    else:
        pass       
    if student in InformationTechnologyStudents:
        InformationSystemStudents.remove(student)
    else:
        pass
    if student in InformationSystemStudents:
        InformationTechnologyStudents.remove(student)
    else:
        pass


def setLimit():
    global limitSE, limitCS, limitDS, limitIS, limitIT
    print("1. limit intake capacity of software engineering")
    print("2. limit intake capacity of Computer science")
    print("3. limit intake capacity of Data Science")
    print("4. limit intake capacity of Information system")
    print("5. limit intake capacity of Information technology")
    
    choice = int(input("Enter your choice : "))
    limit = int(input("Enter the intake capacity : "))
    if choice == 1:
        limitSE = limit
    elif choice == 2:
        limitCS = limit
    elif choice == 3:
        limitDS = limit
    elif choice == 4:
        limitIS = limit
    elif choice == 5:
        limitIT = limit
    else:
        print("invalid choice")
        exit()


#    Sorting students by their score


def Sorting():

    sortedScore = []

    for j in StudentsList:
        j["score"] = int(j["score"])
        sortedScore.append(j["score"])
    sortedScore.sort()
    sortedScore.reverse()

    sortedStudents = []

    for k in sortedScore:
        for i in StudentsList:
            if i["score"] == k:
                sortedStudents.append(i)
    return sortedStudents

#  Display Students which are sorted by their score


def Display():
    StudentsList = Sorting()
    count = 1
    print("\n No. \t\tName \t\t   ID \t\t Score")
    for i in StudentsList:
        space1 = 23 - len(i['name'])
        space2 = 15 - len(i["ID"])
        print(count, ".\t", i['name'], " "*space1, i['ID'], " "*space2,  i['score'])
        count = count + 1


def SoftwareEngineering():
    global SoftwareStudents, ComputerScienceStudents, DataScienceStudents
    global InformationSystemStudents, InformationTechnologyStudents

    def SortingSE():
        sortedScore = []

        for student in SoftwareStudents:
            student["score"] = int(student["score"])
            sortedScore.append(student["score"])
        sortedScore.sort()
        sortedScore.reverse()

        sortedStudents = []

        for k in sortedScore:
            for i in SoftwareStudents:
                if i["score"] == k:
                    sortedStudents.append(i)
        return sortedStudents

    def DisplaySE():
        SoftwareStudents = SortingSE()
        count = 1
        print(" No. \t\tName \t\t   ID \t\t Score")
        for i in SoftwareStudents:
            space1 = 23 - len(i['name'])
            space2 = 15 - len(i["ID"])
            print(count, ".\t", i['name'], " "*space1,
                  i['ID'], " "*space2,  i['score'])
            count = count + 1

    while True:
        studentID = input(" Enter your ID number :")
        for student in StudentsList:
            if studentID == student["ID"]:
                checkingPresence()
                if len(SoftwareStudents) < limitSE:
                    SoftwareStudents.append(student)
                    SoftwareStudents = SortingSE()
                    DisplaySE()
                else:
                    SoftwareStudents.append(student)

                    SoftwareStudents = SortingSE()
                    SoftwareStudents.pop()
                    DisplaySE()
                    break
            # else:
        #     print("CHECKING...")

        choice = input("\nEnter y to continue or other to exit : ")
        print(" ")
        if choice.upper() != "Y":
            break


def ComputerScience():
    global SoftwareStudents, ComputerScienceStudents, DataScienceStudents
    global InformationSystemStudents, InformationTechnologyStudents

    def SortingCS():
        sortedScore = []

        for student in ComputerScienceStudents:
            student["score"] = int(student["score"])
            sortedScore.append(student["score"])
        sortedScore.sort()
        sortedScore.reverse()

        sortedStudents = []

        for k in sortedScore:
            for i in ComputerScienceStudents:
                if i["score"] == k:
                    sortedStudents.append(i)
        return sortedStudents

    def DisplaySE():
        ComputerScienceStudents = SortingCS()
        count = 1
        print(" No. \t\tName \t\t   ID \t\t Score")
        for i in ComputerScienceStudents:
            space1 = 23 - len(i['name'])
            space2 = 15 - len(i["ID"])
            print(count, ".\t", i['name'], " "*space1, i['ID'], " "*space2,  i['score'])
            count = count + 1

    while True:
        studentID = input(" Enter your ID number :")
        for student in StudentsList:
            if studentID == student["ID"]:
                checkingPresence()
                if len(ComputerScienceStudents) < limitCS:
                    ComputerScienceStudents.append(student)
                    ComputerScienceStudents = SortingCS()
                    DisplaySE()
                else:
                    ComputerScienceStudents.append(student)

                    ComputerScienceStudents = SortingCS()
                    ComputerScienceStudents.pop()
                    DisplaySE()
        # else:
        #     print("CHECKING...")

        choice = input("\nEnter y to continue or other to exit : ")
        print(" ")
        if choice.upper() != "Y":
            break


def DataScience():
    DataScienceStudents = []

    def SortingDS():
        sortedScore = []

        for student in DataScienceStudents:
            student["score"] = int(student["score"])
            sortedScore.append(student["score"])
        sortedScore.sort()
        sortedScore.reverse()

        sortedStudents = []

        for k in sortedScore:
            for i in DataScienceStudents:
                if i["score"] == k:
                    sortedStudents.append(i)
        return sortedStudents

    def DisplaySE():
        DataScienceStudents = SortingDS()
        count = 1
        print(" No. \t\tName \t\t   ID \t\t Score")
        for i in DataScienceStudents:
            space1 = 23 - len(i['name'])
            space2 = 15 - len(i["ID"])
            print(count, ".\t", i['name'], " "*space1,
                  i['ID'], " "*space2,  i['score'])
            count = count + 1

    while True:
        studentID = input(" Enter your ID number :")
        for student in StudentsList:
            if studentID == student["ID"]:
                checkingPresence()
                if len(DataScienceStudents) < limitDS:
                    DataScienceStudents.append(student)
                    DataScienceStudents = SortingDS()
                    DisplaySE()
                else:
                    DataScienceStudents.append(student)

                    DataScienceStudents = SortingDS()
                    DataScienceStudents.pop()
                    DisplaySE()
        # else:
        #     print("CHECKING...")

        choice = input("\nEnter y to continue or other to exit : ")
        print(" ")
        if choice.upper() != "Y":
            break


def InformationSystem():
    global SoftwareStudents, ComputerScienceStudents, DataScienceStudents
    global InformationSystemStudents, InformationTechnologyStudents

    def SortingIS():
        sortedScore = []

        for student in InformationSystemStudents:
            student["score"] = int(student["score"])
            sortedScore.append(student["score"])
        sortedScore.sort()
        sortedScore.reverse()

        sortedStudents = []

        for k in sortedScore:
            for i in InformationSystemStudents:
                if i["score"] == k:
                    sortedStudents.append(i)
        return sortedStudents

    def DisplaySE():
        InformationSystemStudents = SortingIS()
        count = 1
        print(" No. \t\tName \t\t   ID \t\t Score")
        for i in InformationSystemStudents:
            space1 = 23 - len(i['name'])
            space2 = 15 - len(i["ID"])
            print(count, ".\t", i['name'], " "*space1,
                    i['ID'], " "*space2,  i['score'])
            count = count + 1

    while True:
        studentID = input(" Enter your ID number :")
        for student in StudentsList:
            if studentID == student["ID"]:
                if len(InformationSystemStudents) < limitIS:
                    InformationSystemStudents.append(student)
                    InformationSystemStudents = SortingIS()
                    DisplaySE()
                else:
                    InformationSystemStudents.append(student)

                    InformationSystemStudents = SortingIS()
                    InformationSystemStudents.pop()
                    DisplaySE()
        # else:
        #     print("CHECKING...")

        choice = input("\nEnter y to continue or other to exit : ")
        print(" ")
        if choice.upper() != "Y":
            break


def InformationTechnology():
    global SoftwareStudents, ComputerScienceStudents, DataScienceStudents
    global InformationSystemStudents, InformationTechnologyStudents

    def SortingIT():
        sortedScore = []

        for student in InformationTechnologyStudents:
            student["score"] = int(student["score"])
            sortedScore.append(student["score"])
        sortedScore.sort()
        sortedScore.reverse()

        sortedStudents = []

        for k in sortedScore:
            for i in InformationTechnologyStudents:
                if i["score"] == k:
                    sortedStudents.append(i)
        return sortedStudents

    def DisplaySE():
        InformationTechnologyStudents = SortingIT()
        count = 1
        print(" No. \t\tName \t\t   ID \t\t Score")
        for i in InformationTechnologyStudents:
            space1 = 23 - len(i['name'])
            space2 = 15 - len(i["ID"])
            print(count, ".\t", i['name'], " "*space1,
                  i['ID'], " "*space2,  i['score'])
            count = count + 1

    while True:
        studentID = input(" Enter your ID number :")
        for student in StudentsList:
            if studentID == student["ID"]:
                checkingPresence()
                if len(InformationTechnologyStudents) < limitIT:
                    InformationTechnologyStudents.append(student)
                    InformationTechnologyStudents = SortingIT()
                    DisplaySE()
                else:
                    InformationTechnologyStudents.append(student)

                    InformationTechnologyStudents = SortingIT()
                    InformationTechnologyStudents.pop()
                    DisplaySE()
        # else:
        #     print("CHECKING...")

        choice = input("\nEnter y to continue or other to exit : ")
        print(" ")
        if choice.upper() != "Y":
            break


def ChangePassword():
    password = input("Enter the previous  password : ")
    for student in StudentsList:
        if student["password"] == password:
            newPassword = input("Enter you password : ")
            confirmNewPassword = input("Confirm your Password : ")
            if newPassword == confirmNewPassword:
                student["password"] = newPassword
                print("Password Successfully Changed !!")
            else:
                print("you Entered to different password")
                break


def DepartmentSelection():
    print("\t\n🌺🌻 Welcome to Department Selection 🌼🌸")
    print("\nSelect a department : ")
    print("1. Software Engineering ")
    print("2. Computer science ")
    print("3. Data Science ")
    print("4. information System ")
    print("5. Information Technology")

    response = int(input("\nEnter your Choice : "))

    if response == 1:
        SoftwareEngineering()
    elif response == 2:
        ComputerScience()
    elif response == 3:
        DataScience()
    elif response == 4:
        InformationSystem()
    elif response == 5:
        InformationTechnology()
    else:
        print(" invalid  Choice ")
        os.system("cls")
        exit()


while True:
    print("  \n🙌 🌷Welcome DBU Student management system 🌺💐\n")

    print("\n1. For Admin activities")
    print("2. Select a department ")
    print("3. General priority from all")
    print("4. Priority in one Department ")
    print("5. Change you password")
    print("0. To exit the program")

    response = int(input("\nEnter your Choice : "))

    if response == 1:
        print("This is only for the admin !!!")
        adminPassword = input("\nEnter the admin  password  : ")
        if adminPassword == admin:
            adminActivities()
            choice = input("\nEnter your choice : ")
            if choice == '1':
                addNewStudent()
            elif choice == '2':
                ChangeAdminPassword()
            elif choice == '3':
                SearchUser()
            elif choice == "4":
                DeleteUsers()
            elif choice == "5":
                Display()
            elif choice == "6":
                setLimit()
            else:
                print("invalid choice !!")
        else:
            print("incorrect password!!")
            os.system("cls")
            break
    elif response == 2:
        DepartmentSelection()
    elif response == 3:
        Display()
    elif response == 4:
        pass
    elif choice == 5:
        ChangePassword()
    elif response == 0:
        os.system("cls")
        break

    else:
        print(" invalid  Choice ")
        os.system("cls")
        break

