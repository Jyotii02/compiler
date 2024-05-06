import tkinter as tk
import subprocess
import time
import webbrowser

class CodeCompilerApp:
    def __init__(self, root):
        self.root = root
        root.title("Code Compiler")

        # Language selection buttons
        self.language_label = tk.Label(root, text="Select a language:")
        self.language_label.pack()
        self.language_buttons = []
        languages = ["Python", "C", "JavaScript"]
        for lang in languages:
            button = tk.Button(root, text=lang, command=lambda l=lang: self.select_language(l))
            self.language_buttons.append(button)
            button.pack()

        # Code input
        self.code_label = tk.Label(root, text="Write your code:")
        self.code_label.pack()
        self.code_text = tk.Text(root, width=50, height=10)
        self.code_text.pack()

        # Compile and run button
        self.compile_button = tk.Button(root, text="Compile and Run", command=self.compile_and_run)
        self.compile_button.pack()

        # Output
        self.output_label = tk.Label(root, text="Output:")
        self.output_label.pack()
        self.output_text = tk.Text(root, width=50, height=10)
        self.output_text.pack()

    def select_language(self, lang):
        self.selected_language = lang

    def compile_and_run(self):
        code = self.code_text.get("1.0", "end-1c")
        self.output_text.delete("1.0", "end")
        if hasattr(self, "selected_language"):
            if self.selected_language == "Python":
                self.run_python_code(code)
            elif self.selected_language == "C":
                self.compile_and_run_c(code)
            elif self.selected_language == "JavaScript":
                self.run_javascript_code(code)
        else:
            self.output_text.insert("end", "Please select a language.")

    def run_python_code(self, code):
        try:
            start_time = time.time()
            exec(code)
            end_time = time.time()
            execution_time = end_time - start_time
            self.output_text.insert("end", f"Execution Time: {execution_time} seconds\n")
        except Exception as e:
            self.output_text.insert("end", f"Error: {str(e)}")

    def compile_and_run_c(self, code):
        try:
            with open("temp.c", "w") as file:
                file.write(code)
            compilation_result = subprocess.run(["gcc", "temp.c", "-o", "temp"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            if compilation_result.returncode == 0:
                execution_result = subprocess.run(["./temp"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                self.output_text.insert("end", "Compilation Successful\n")
                self.output_text.insert("end", execution_result.stdout)
            else:
                self.output_text.insert("end", "Compilation Error:\n")
                self.output_text.insert("end", compilation_result.stderr)
        except Exception as e:
            self.output_text.insert("end", f"Error: {str(e)}")

    def run_javascript_code(self, code):
        try:
            with open("temp.html", "w") as file:
                html_code = f"""
                <html>
                <body>
                    <script>
                    {code}
                    </script>
                </body>
                </html>
                """
                file.write(html_code)
            webbrowser.open('temp.html')
        except Exception as e:
            self.output_text.insert("end", f"Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = CodeCompilerApp(root)
    root.mainloop()
