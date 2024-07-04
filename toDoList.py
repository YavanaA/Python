"""
   This is a program that allows you to manage tasks.
      specifically : - to create or paln tasks
                             - to display tasks
                             - to update to tasks
                             - to delete tasks

"""

import os

print(" \n\n     This is my to do list \n ")
Tasks = []


def create_task():  # used to create a new task
    title = input(" Enter the title of the task : ")
    status = input(" Enter the status of the task (pending / in progress /done!!) : ")
    time = input(" Enter the time of the task : ")
    Task = {"title": title, "status": status, "time": time}
    Tasks.append(Task)
    print("Task successfully created 🙏")
    
    
def display_tasks():  # used to display tasks
    if len(Tasks) == 0:
        print("There is no tasks to be displayed 👁️")
    else:
        count = 1
        print("\n No. \t Title\t\t\t Status \t   time")
        for Task in Tasks:
            space1 = 23 - len(Task['title'])
            space2 = 15 - len(Task["status"])
            print(count, ".\t", Task['title'], " "*space1, Task['status'], " "*space2,  Task['time'])
            count = count + 1
        
        
def search_task():
    print("1. search by title")
    print("2. search by status")
    print("3. search by time")

    def simpleSearchChoices():
        print("1. price search")
        print("2. exact search")
        
    def DisplaySearched():
        count = 1
        print("\n No. \t\t Title\t\t   Status \t\t time")
        for Task in searched:
            space1 = 23 - len(Task['title'])
            space2 = 15 - len(Task["status"])
            print(count, ".\t", Task['title'], " "*space1, Task['status'], " "*space2,  Task['time'])
            count = count + 1
        
        # Searching by title
    choice = input("Enter you choice : ")
    if choice == '1':
        simpleSearchChoices()
        response = int(input("Enter your choice : "))
        if response == 1:  # precise title search
            searchingTitle = input("Enter the title of the task : ")
            count = 0
            titles = []
            for task in Tasks:
                titles.append(task["title"])
            searched = []
            for Task in Tasks:
                if searchingTitle in titles:
                    if searchingTitle in Task["title"]:
                        count = count + 1
                        searched.append(Task)
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
            
        elif response == 2:  # Exact title search
            searchingTitle = input("Enter the title of the task : ")
            count = 0
            titles = []
            for task in Tasks:
                titles.append(task["title"])
            searched = []
            for Task in Tasks:
                if searchingTitle in titles:
                    if Task["title"] == searchingTitle:
                        count = count + 1
                        searched.append(Task)
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
# searching by status
    if choice == '2':
        simpleSearchChoices()
        response = int(input("Enter your choice : "))
        if response == 1:  # precise status search
            searchingStatus = input("Enter the status of the task : ")
            count = 0
            statuses = []
            for task in Tasks:
                statuses.append(task["status"])
                searched = []
            for Task in Tasks:
                if searchingStatus in statuses:
                    if searchingTitle in Task["title"]:
                        count = count + 1
                        searched.append(Task)
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
        elif response == 2: # exact status search
            searchingTitle = input("Enter the status of the task : ")
            count = 0
            statuses = []
            for task in Tasks:
                statuses.append(task["status"])
            searched = []
            for Task in Tasks:
                if searchingStatus in statuses:
                    if Task["status"] == searchingStatus:
                        count = count + 1
                        searched.append(Task)
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
 
        # searching by time 
    elif choice == '3':  
        simpleSearchChoices()
        response = int(input("Enter your choice : "))
        if response == 1: # precise time search
            searchingTime = input("Enter the time of the task : ")
            count = 0
            times = []
            for task in Tasks: 
                statuses.append(task["time"])
            searched = []
            for Task in Tasks:
                if searchingTime in times:
                    if searchingTime in Task["time"]:
                        count = count + 1
                        searched.append(Task)
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
        elif response == 2:
            searchingTime = input("Enter the time of the task : ")
            count = 0
            times = []
            for task in Tasks:
                times.append(task["time"])
            searched = []
            for Task in Tasks:
                if searchingTime in times:
                    if Task["time"] == searchingTime:
                        count = count + 1
                        searched.append(Task)
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
   

def update_task():  # used to update tasks
    task_index = int(input("Enter the task number")) - 1
    if 0 <= task_index < len(Tasks):
        title = input(" Enter the title of the task which needs status update : ")
        new_status = input(" Enter the new status(pending / in progress /done!!)")
        new_time = input(" Enter the the new time  of the task : ")
        Tasks[task_index]['title'] = title
        Tasks[task_index]['status'] = new_status
        Tasks[task_index]['time'] = new_time
        Task = {"task": title, "status": new_status, "time": new_time}
        Tasks.pop(task_index)
        Tasks.append(Task)
        print("Task successfully updated 🙏")
    else: 
        print("invalid index  😔")
        return
  
       
def delete_task() :  # used to delete tasks
    task_index = int(input("Enter the task number : ")) - 1
    if 0 <= task_index < len(Tasks):
        del Tasks[task_index]
        print("Task successfully deleted ❌")
    else:
        print("invalid index  😔")
    return
    
while True:
    print("  \n Menu  ")
    print("Enter 1 - to create tasks  p\n")
    print("Enter 2 - to display tasks  \n")
    print("Enter 3 - to search tasks  \n")
    print("Enter 4 - to delete tasks  \n")
    print("Enter 5 - to update tasks  \n")
    print("Enter 0 - to exit \n")
    response = input(" please enter your choice : \n ")
    if response == '1':
        create_task()
    elif response == '2':
        display_tasks()
    elif response == '3':
        search_task()

    elif response == '4':
        delete_task()
    elif response == '5':
        update_task()
    elif response == '0':
        break
    else:
        print("Invalid choice ⚠️")
        break













































