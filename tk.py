import tkinter as tk
from tkinter import messagebox, simpledialog

# Initialize main window
root = tk.Tk()
root.title("Student Management System")

admin_password = "DBU1234"
default_password = "12345678"

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
selectionSummary = []
selectingStudentList = []

StudentsList = [
    {'name': "Hailemeskel Getaneh", "ID": "DBU1501246", 
     'score': 90, 'password': "1234"},
    
    {'name': "Hailemariam Kassaw", "ID": "DBU1501245", 
     'score': 94, 'password': "1235"},
    
    {'name': "Abebe Kebede", "ID": "DBU1501239",
     'score': 87, 'password': "1111"},
    
    {'name': "Nigus Tatek", "ID": "DBU1501244",
     'score': 96, 'password': "2222"},
    
    {'name': "Hailemeskel Kebede",  "ID": "DBU1501240",
     'score': 90, 'password': "3333"},
    {'name': "Hanna Selemon", "ID": "DBU1501241", 
     'score': 80, 'password': "4444"},
    
    {'name': "Girum Ermiyas", "ID": "DBU1501242", 
     'score': 85, 'password': "5555"},
    
    {'name': "Abiy Ahimed", "ID": " DBU1501243", 
     'score': 56, 'password': "6666"},
    
    {'name': "Selamawit Ayele", "ID": "DBU1501238",
     'score': 78, 'password': "7777"},
    
    {'name': "Girma Geremew", "ID": "DBU1501237",
     'score': 76, 'password': "8888"},
    {'name': "Martemuz Zemedkun", "ID": "DBU1501236", 
     'score': 100, 'password': "9999"},
    
    {'name': "Betelhem Debebe", "ID": "DBU1501235", 
     'score': 86, 'password': "0000"}
]


def sort_students_by_score(student_list):
    return sorted(student_list, key=lambda x: x['score'], reverse=True)


def add_new_student():
    new_student = {
        'name': simpledialog.askstring("Input", "Enter the name of the student: "),
        'ID': simpledialog.askstring("Input", "Enter the student's ID: "),
        'score': int(simpledialog.askstring("Input", "Enter the score: ")),
        'password': default_password
    }
    if any(student['ID'] == new_student['ID'] for student in StudentsList):
        messagebox.showerror("Error", "This ID already exists!")
    else:
        StudentsList.append(new_student)
        messagebox.showinfo("Success", "New student added successfully!")


def change_admin_password():
    global admin_password
    current_password = simpledialog.askstring("Input", "Enter the previous password:", show='*')
    if current_password == admin_password:
        new_password = simpledialog.askstring("Input", "Enter new password:", show='*')
        confirm_new_password = simpledialog.askstring("Input", "Confirm new password:", show='*')
        if new_password == confirm_new_password:
            admin_password = new_password
            messagebox.showinfo("Success", "Admin password changed successfully!")
        else:
            messagebox.showerror("Error", "Passwords do not match!")
    else:
        messagebox.showerror("Error", "Incorrect password!")


def search_user():
    choice = simpledialog.askstring("Input", "Search by: 1. Name, 2. ID, 3. Score")
    search_term = simpledialog.askstring("Input", "Enter search term:")
    results = []

    if choice == '1':
        results = [student for student in StudentsList if search_term.lower() in student['name'].lower()]
    elif choice == '2':
        results = [student for student in StudentsList if search_term == student['ID']]
    elif choice == '3':
        results = [student for student in StudentsList if int(search_term) == student['score']]

    if results:
        result_text = "\n".join([f"Name: {student['name']}, ID: {student['ID']}, Score: {student['score']}" for student in results])
        messagebox.showinfo("Search Results", result_text)
    else:
        messagebox.showinfo("Search Results", "No results found.")


def delete_user():
    student_id = simpledialog.askstring("Input", "Enter the ID number to delete:")
    student = next((student for student in StudentsList if student['ID'] == student_id), None)
    if student:
        confirm_id = simpledialog.askstring("Input", "Confirm the ID:")
        if confirm_id == student_id:
            caution = simpledialog.askstring("Input", "Do you want to delete permanently? (yes/no)")
            if caution.lower() == "yes":
                StudentsList.remove(student)
                messagebox.showinfo("Success", "User deleted successfully!")
    else:
        messagebox.showerror("Error", "No result found to delete")


def set_limit():
    global limitSE, limitCS, limitDS, limitIS, limitIT
    choice = simpledialog.askstring("Input", "Set limit for: 1. SE, 2. CS, 3. DS, 4. IS, 5. IT")
    limit = int(simpledialog.askstring("Input", "Enter the intake capacity:"))
    
    if choice == '1':
        limitSE = limit
    elif choice == '2':
        limitCS = limit
    elif choice == '3':
        limitDS = limit
    elif choice == '4':
        limitIS = limit
    elif choice == '5':
        limitIT = limit
    else:
        messagebox.showerror("Error", "Invalid choice!")


def display_students():
    sorted_students = sort_students_by_score(StudentsList)
    result_text = "\n".join([f"Name: {student['name']}, ID: {student['ID']}, Score: {student['score']}" for student in sorted_students])
    messagebox.showinfo("All Students", result_text)


def admin_activities():
    activities_window = tk.Toplevel(root)
    activities_window.title("Admin Activities")

    tk.Button(activities_window, text="Add new user", command=add_new_student).pack()
    tk.Button(activities_window, text="Change admin password", command=change_admin_password).pack()
    tk.Button(activities_window, text="Search user", command=search_user).pack()
    tk.Button(activities_window, text="Delete user", command=delete_user).pack()
    tk.Button(activities_window, text="Display users", command=display_students).pack()
    tk.Button(activities_window, text="Set intake capacity", command=set_limit).pack()


def selecting():
    DepartmentsList()


def DepartmentsList():
    departments_window = tk.Toplevel(root)
    departments_window.title("Department Selection")

    tk.Label(departments_window, text="Select a department:").pack()
    tk.Button(departments_window, text="1. Software Engineering", command=selecting).pack()
    tk.Button(departments_window, text="2. Computer Science", command=selecting).pack()
    tk.Button(departments_window, text="3. Data Science", command=selecting).pack()
    tk.Button(departments_window, text="4. Information System", command=selecting).pack()
    tk.Button(departments_window, text="5. Information Technology", command=selecting).pack()


def main_menu():
    tk.Label(root, text="Welcome to DBU Student Management System").pack()

    tk.Button(root, text="Admin Activities", command=admin_activities).pack()
    tk.Button(root, text="Select a Department", command=selecting).pack()
    tk.Button(root, text="Exit", command=root.quit).pack()


if __name__ == "__main__":
    main_menu()
    root.mainloop()
