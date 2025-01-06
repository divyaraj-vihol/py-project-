from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import asksaveasfilename, askopenfile
import subprocess
import os

# Create the main window
root = Tk()
root.title("DV IDEL")
root.geometry("1280x720+150+80")
root.configure(bg="#323846")
root.resizable(False, False)

file_path = ''

def set_file_path(path):
    """Set the global file path."""
    global file_path
    file_path = path

def open_file():
    """Open a Python file and display its content in the code input area."""
    file = askopenfile(filetypes=[('Python files', '*.py')])
    if file:  # Check if a file was selected
        code_input.delete('1.0', END)
        code_input.insert('1.0', file.read())
        set_file_path(file.name)  # Use file.name to get the path

def save():
    """Save the current code to a file."""
    if file_path == '':
        path = asksaveasfilename(defaultextension=".py", filetypes=[('Python Files', '*.py')])
        if path:  # Check if a path was selected
            set_file_path(path)
    else:
        path = file_path

    with open(path, 'w') as file:
        code = code_input.get('1.0', END)
        file.write(code)  # Write the code to the file

def run():
    """Run the current Python file and display the output."""
    if file_path == '':
        messagebox.showerror("DV IDLE", "Please save your code before running.")
        return

    command = f'python "{file_path}"'  # Use quotes in case of spaces in the path
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()

    code_output.delete('1.0', END)  # Clear previous output
    code_output.insert('1.0', output.decode())  # Insert output
    if error:
        code_output.insert(END, error.decode())  # Insert error if any

# Set the window icon
try:
    image_icon = PhotoImage(file="logo.png")
    root.iconphoto(False, image_icon)
except Exception as e:
    messagebox.showerror("Error", f"Failed to load icon: {e}")

# Code input area
code_input = Text(root, font="consolas 18")
code_input.place(x=180, y=0, width=680, height=720)

# Output code area
code_output = Text(root, font="consolas 15", bg="#323846", fg="lightgreen")
code_output.place(x=680, y=0, width=420, height=720)

# Buttons
open_icon = PhotoImage(file="open1.png")
save_icon = PhotoImage(file="save1.png")
run_icon = PhotoImage(file="run1.png")

Button(root, image=open_icon, bg="#323846", bd=0, command=open_file).place(x=30, y=30)
Button(root, image=save_icon, bg="#323846", bd=0, command=save).place(x=30, y=145)
Button(root, image=run_icon, bg="#323846", bd=0, command=run).place(x=30, y=260)

# Start the Tkinter event loop
root.mainloop()