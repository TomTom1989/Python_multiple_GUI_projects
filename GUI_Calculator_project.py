import tkinter as tk

# Define the calculator class (this time with OOP style and not procedurial)
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        self.root.resizable(True, True)  # Allow resizing

        # Entry widget for displaying input/output
        self.entry = tk.Entry(root, font=("Arial", 20), justify="right", bd=10, insertwidth=2)
        self.entry.grid(row=0, column=0, columnspan=4, sticky="nsew")
        self.entry.bind("<Key>", lambda e: "break")  # Disable keyboard input

        # Configure rows and columns to scale with resizing
        self.root.rowconfigure(0, weight=1)
        for i in range(1, 6):  # Total rows for buttons
            self.root.rowconfigure(i, weight=1)
        for i in range(4):  # Total columns for buttons
            self.root.columnconfigure(i, weight=1)

        # Buttons and layout
        self.create_buttons()

    def create_buttons(self):
        button_texts = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "C", "0", ".", "+",
            "="
        ]

        row = 1
        col = 0

        for text in button_texts:
            if text == "=":
                btn = tk.Button(self.root, text=text, padx=20, pady=20, font=("Arial", 14), bg="lightblue", command=self.calculate)
                btn.grid(row=row, column=col, columnspan=4, sticky="nsew")
            elif text == "C":
                btn = tk.Button(self.root, text=text, padx=20, pady=20, font=("Arial", 14), bg="red", fg="white", command=self.clear)
                btn.grid(row=row, column=col, sticky="nsew")
            else:
                btn = tk.Button(self.root, text=text, padx=20, pady=20, font=("Arial", 14), command=lambda t=text: self.append_text(t))
                btn.grid(row=row, column=col, sticky="nsew")

            col += 1
            if col > 3:
                col = 0
                row += 1

    def append_text(self, text):
        current = self.entry.get()
        if len(current) < 10:
            self.entry.insert(tk.END, text)

    def clear(self):
        self.entry.delete(0, tk.END)

    def calculate(self):
        try:
            expression = self.entry.get()
            result = eval(expression)  # Evaluate the mathematical expression
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, str(round(result, 5)))  # Show result with max 5 decimal places
        except ZeroDivisionError:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")
        except Exception:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")

# Main application
if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
