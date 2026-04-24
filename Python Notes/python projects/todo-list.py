
# 1. Simple TO-DO List :---->>

""" tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    
    choice = input("Enter choice : ")
    
    if choice == "1":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully!")
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available")
        else:
            print("\nYour Tasks: ")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")
    elif choice == "3":
        task_no = int(input("Enter task number to remove: "))
        if 1 <= task_no <= len(tasks):
            removed = tasks.pop(task_no - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number!")
    elif choice == "4":
        print("Exiting program...")
        break
    else:
        print("Invalid choice") """
        
        
# 2. TO-DO List Using Functions :---->>

""" tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added!")
    
def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
            
def remove_task():
    view_tasks()
    try:
        task_no = int(input("Enter task number to remove: "))
        tasks.pop(task_no - 1)
        print("Task removed")
    except:
        print("Invalid input")
        
while True:
    print("\n1. Add\n2. View \n3. Remove\n4. Exit")
    choice = input("Choice: ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        break
    else:
        print("Wrong choice") """
        
        
# 3. TO-DO List Using Dictinory :---->>

""" tasks = {}

def add_task():
    task = input("Enter task: ")
    tasks[task] = "Pending"
    
def view_tasks():
    for i, (task, status) in enumerate(tasks.items(), 1):
        print(f"{i}. {task} - {status}")
        
def mark_complete():
    task = input("Enter task name to mark complete: ")
    if task in tasks:
        tasks[task] = "Completed"
    else:
        print("Task not found!")
        
while True:
    print("\n1. Add\n2. View\n3. Mark Complete\n4. Exit")
    choice = input("Choice: ")
    
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        mark_complete()
    elif choice == "4":
        break """
        

# 4. TO-DO List Using TickInt :---->

""" import tkinter as tk
from tkinter import messagebox

# Main Window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x500")

tasks = []

# Functions
def add_task():
    task = entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Select a task to delete!")

def mark_complete():
    try:
        selected = listbox.curselection()[0]
        task = listbox.get(selected)
        listbox.delete(selected)
        listbox.insert(tk.END, task + " ✔")
    except:
        messagebox.showwarning("Warning", "Select a task!")

# Widgets
title = tk.Label(root, text="My To-Do List", font=("Arial", 18))
title.pack(pady=10)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack(pady=5)

listbox = tk.Listbox(root, font=("Arial", 14), width=30, height=10)
listbox.pack(pady=10)

delete_btn = tk.Button(root, text="Delete Task", command=delete_task)
delete_btn.pack(pady=5)

complete_btn = tk.Button(root, text="Mark Complete", command=mark_complete)
complete_btn.pack(pady=5)

root.mainloop() """


import customtkinter as ctk
from tkinter import messagebox

# Appearance
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# Main Window
app = ctk.CTk()
app.title("Modern To-Do List")
app.geometry("500x600")

tasks = []

# Functions
def add_task():
    task = entry.get()
    if task.strip() == "":
        messagebox.showwarning("Warning", "Please enter a task!")
        return
    
    task_label = ctk.CTkLabel(task_frame, text=task, anchor="w")
    task_label.pack(fill="x", pady=5, padx=10)
    tasks.append(task_label)
    entry.delete(0, "end")

def delete_task():
    if tasks:
        task = tasks.pop()
        task.destroy()
    else:
        messagebox.showwarning("Warning", "No task to delete!")

def mark_complete():
    if tasks:
        task = tasks[-1]
        task.configure(text=task.cget("text") + " ✔", text_color="green")
    else:
        messagebox.showwarning("Warning", "No task available!")

# Title
title = ctk.CTkLabel(app, text="📝 My To-Do List", font=("Arial", 24))
title.pack(pady=20)

# Entry
entry = ctk.CTkEntry(app, placeholder_text="Enter your task...", width=350)
entry.pack(pady=10)

# Buttons Frame
btn_frame = ctk.CTkFrame(app)
btn_frame.pack(pady=10)

add_btn = ctk.CTkButton(btn_frame, text="Add Task", command=add_task)
add_btn.grid(row=0, column=0, padx=10)

complete_btn = ctk.CTkButton(btn_frame, text="Mark Complete", command=mark_complete)
complete_btn.grid(row=0, column=1, padx=10)

delete_btn = ctk.CTkButton(btn_frame, text="Delete Task", fg_color="red", command=delete_task)
delete_btn.grid(row=0, column=2, padx=10)

# Scrollable Frame for Tasks
task_frame = ctk.CTkScrollableFrame(app, width=400, height=300)
task_frame.pack(pady=20)

app.mainloop()