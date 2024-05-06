import tkinter as tk
from tkinter import filedialog
def open_or_save_file(mode):
    """Opens or saves a file.
    Args:
        mode: The mode to open or save the file in. Must be either "open" or "save".
    Returns:
        The path to the file.
    """
    if mode not in ["open", "save"]:
        raise ValueError("Invalid mode: {}".format(mode))
    if mode == "open":
        return filedialog.askopenfilename()
    else:
        return filedialog.asksaveasfilename()
def compile_and_run(language, code):
    """Compiles and runs the code.
    Args:
        language: The language to compile the code in.
        code: The code to compile and run.
    """
    if language not in ["python", "javascript", "c++"]:
        raise ValueError("Invalid language: {}".format(language))
    if language == "python":
        exec(code)
    elif language == "javascript":
        exec(code)
    elif language == "c++":
        os.system("g++ -o a.out {} && ./a.out".format(code))
def run():
    """Runs the code."""
    # Get the user-provided code
    code = editor.get()
    # Validate the user-provided code
    if not validate_code(code):
        return
    # Compile and run the code
    compile_and_run(language, code)
# Create the main window
root = tk.Tk()
# Set the title of the window
root.title("Code Runner")
# Create the editor
editor = tk.Text(root)
editor.pack()
# Create the run button
run_button = tk.Button(root, text="Run", command=run)
run_button.pack()
# Start the main loop
root.mainloop()