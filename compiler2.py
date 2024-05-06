import tkinter as tk
import os
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
def compile_and_run(language, code):
    if language == "Python":
        exec(code)
    elif language == "C":
        # Create a temporary file to store the code
        with open("temp.c", "w") as f:
            f.write(code)
        # Compile the code
        try:
            subprocess.call(["gcc", "temp.c", "-o", "temp"])
        except Exception as e:
            # Display the error message
            messagebox.showerror("Error", str(e))
        # Delete the temporary file
        os.remove("temp.c")
        # Run the compiled code
        subprocess.call(["./temp"])
    elif language == "JavaScript":
        # Create a temporary file to store the code
        with open("temp.js", "w") as f:
            f.write(code)
        # Run the code
        subprocess.call(["node", "temp.js"])
def run():
    code = text.get("1.0", tk.END)
    language = language_var.get()
    compile_and_run(language, code)
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
