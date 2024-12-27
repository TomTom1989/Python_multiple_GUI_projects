import tkinter as tk
from tkinter import messagebox
import random


class TheClicker:
    def __init__(self, root):
        self.root = root
        self.root.title("The Clicker")
        self.timer = 0
        self.buttons = []
        self.numbers = []
        self.current_index = 0
        self.timer_running = False

        self.create_buttons()

        # Timer Label
        self.timer_label = tk.Label(self.root, text="Time: 0", font=("Arial", 14))
        self.timer_label.grid(row=6, column=0, columnspan=5, pady=10)

    def create_buttons(self):
        """Create a 5x5 grid of buttons with unique random numbers."""
        self.numbers = random.sample(range(1, 1000), 25)  # 25 unique random numbers
        sorted_numbers = sorted(self.numbers)

        for i in range(5):
            for j in range(5):
                num = self.numbers.pop(0)
                button = tk.Button(
                    self.root,
                    text=num,
                    width=8,
                    height=2,
                    command=lambda n=num: self.button_click(n),
                )
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons.append((button, num))

        self.numbers = sorted_numbers

    def button_click(self, number):
        if not self.timer_running:
            self.start_timer()

        # Check if the clicked number is the correct one in the sequence
        if number == self.numbers[self.current_index]:
            for button, num in self.buttons:
                if num == number:
                    button.config(state=tk.DISABLED)
                    break
            self.current_index += 1

            # Check if the game is over
            if self.current_index == len(self.numbers):
                self.stop_timer()
                tk.messagebox.showinfo("Congratulations!", f"You finished in {self.timer} seconds!")
        else:
            pass

    def start_timer(self):
        self.timer_running = True
        self.update_timer()

    def stop_timer(self):
        self.timer_running = False

    def update_timer(self):
        if self.timer_running:
            self.timer += 1
            self.timer_label.config(text=f"Time: {self.timer}")
            self.root.after(1000, self.update_timer)


root = tk.Tk()
game = TheClicker(root)
root.mainloop()
