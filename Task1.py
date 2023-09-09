import tkinter as tk

def create_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def update_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        selected_task = selected_task[0]
        new_task = task_entry.get()
        if new_task:
            task_listbox.delete(selected_task)
            task_listbox.insert(selected_task, new_task)
            task_entry.delete(0, tk.END)

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)

root = tk.Tk()
root.title("To-Do List Application")
root.maxsize(500,600)
root.config(bg="aquamarine")

frame = tk.Frame(root,bg="aquamarine")
frame.pack(pady=10)

head=tk.Label(root,text="Well Come To My ToDo List",font=("Berlin Sans FB",16),bg="aquamarine")
head.pack(pady=5)
task_entry = tk.Entry(frame, font=("Helvetica", 14))
task_entry.pack(side=tk.LEFT, padx=10,pady=5)
add_button = tk.Button(frame, text="Add Task", command=create_task, font=("Helvetica", 12),bg="green",borderwidth=1)
add_button.pack(side=tk.LEFT)

update_button = tk.Button(root, text="Update Task", command=update_task, font=("Helvetica", 12),bg="grey",width=48,borderwidth=1)
update_button.pack(pady=10)
delete_button = tk.Button(root, text="Delete Task", command=delete_task, font=("Helvetica", 12),bg="red",width=48,borderwidth=1)
delete_button.pack()

task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, font=("Helvetica", 14), height=10, width=40,bg="azure")
task_listbox.pack(pady=20)

root.mainloop()