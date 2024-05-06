import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import subprocess
def open_or_save_file(language):
    filepath = filedialog.askopenfilename(
        title="Open " + language + " File",
        filetypes=[("All Files", "*.*")]
    )
    if filepath:
        with open(filepath, "r") as f:
            code = f.read()
def run():
    code = text.get("1.0", tk.END)
    language = language_var.get()
    try:
        if language == "Python":
            exec(code)
        elif language == "C":
            subprocess.run(["gcc", "-o", "a.out", "code.c"])
            subprocess.run(["./a.out"])
        elif language == "JavaScript":
            subprocess.run(["node", "code.js"])
    except Exception as e:
        print("Error running " + language + " code:\n" + str(e))
root = tk.Tk()
root.title("Code Runner")
# Create a text editor widget
text = tk.Text(root)
text.pack()
# Create a language selection widget
language_var = tk.StringVar()
language_var.set("Python")
language_menu = tk.OptionMenu(root, language_var, "Python", "C", "JavaScript")
language_menu.pack()
# Create a button to run the code
run_button = tk.Button(root, text="Run", command=run)
run_button.pack()
# Run the main loop
root.mainloop()