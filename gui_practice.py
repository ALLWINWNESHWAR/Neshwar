import tkinter as tk

def submit():
    name = name_entry.get()
    message = message_box.get("1.4",tk.END).strip()

    skills = ""
    if python_var.get():
        skills += "Python"
    if sql_var.get():
        skills += "SQL"

    result.config(text=f"Name:{name}\nMessage: {message}\nSkills: {skills}")

window = tk.Tk()

window.title("Student Form")
window.geometry("600x600")

name_label = tk.Label(window,text="Enter your name:")
name_label.pack()

name_entry = tk.Entry(window)
name_entry.pack()

message_label = tk.Label(window,text="Enter your message: ")
message_label.pack()

message_box = tk.Text(window,height = 5,width= 35)
message_box.pack()

python_var = tk.BooleanVar()
sql_var = tk.BooleanVar()

tk.Checkbutton(window,text="Python",variable = python_var).pack()
tk.Checkbutton(window,text="SQL",variable = sql_var).pack()

tk.Button(window,text="Submit",command=submit).pack()

result = tk.Label(window)
result.pack()

