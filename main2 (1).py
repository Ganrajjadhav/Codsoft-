mport tkinter as tk

# Create the main window
window = tk.Tk()
window.title("To-Do List")

# Create the list of tasks
tasks = []

# Create the function to add a task
def add_task():
    task = task_entry.get()
    tasks.append(task)
    task_list.insert(tk.END, task)
    task_entry.delete(0, tk.END)

# Create the function to delete a task
def delete_task():
    task = task_list.get(task_list.curselection())
    tasks.remove(task)
    task_list.delete(tk.ANCHOR)

# Create the function to mark a task as complete
def complete_task():
    task = task_list.get(task_list.curselection())
    tasks.remove(task)
    task_list.delete(tk.ANCHOR)
    task_list.insert(tk.END, task, "completed")

# Create the task entry field
task_entry = tk.Entry(window)
task_entry.pack(side=tk.TOP)

# Create the add task button
add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack(side=tk.TOP)

# Create the task list
task_list = tk.Listbox(window)
task_list.pack(side=tk.LEFT)

# Create the delete task button
delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack(side=tk.LEFT)

# Create the complete task button
complete_button = tk.Button(window, text="Complete Task", command=complete_task)
complete_button.pack(side=tk.LEFT)

# Start the main loop
window.mainloop()