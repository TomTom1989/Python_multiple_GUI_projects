from tkinter import Tk, Button, Canvas

# Procedurial Style (not OOP)
# Define the traffic light phases
phases = [
    (True, False, False),  # Red
    (True, True, False),   # Red and Yellow
    (False, False, True),  # Green
    (False, True, False)   # Yellow
]

# Initialize the current phase index
current_phase = 0


def update_traffic_light():
   # canvas.delete("all")  # Clear the canvas but here it's optional as it is overwritten with new pos and color each time (gray or not)
    lights = phases[current_phase]

    # Define positions and colors of the lights
    colors = ['red', 'yellow', 'green']
    positions = [(50, 50, 150, 150), (50, 170, 150, 270), (50, 290, 150, 390)]

    for i, (pos, color) in enumerate(zip(positions, colors)):
        if lights[i]:
            canvas.create_oval(pos, fill=color)  # Light is on
        else:
            canvas.create_oval(pos, fill="gray")  # Light is off


def next_phase():
    global current_phase
    current_phase = (current_phase + 1) % len(phases)  # Cycle through phases
    update_traffic_light()

# Create the main window
root = Tk()
root.title("Traffic Light Simulation")

# Create a canvas for the traffic light
canvas = Canvas(root, width=200, height=400, bg="black")
canvas.pack()

# Create buttons
next_button = Button(root, text="Next", command=next_phase)
next_button.pack(side="left", padx=10, pady=10)

quit_button = Button(root, text="Quit", command=root.destroy)
quit_button.pack(side="right", padx=10, pady=10)

# Initialize the traffic light display
update_traffic_light()


root.mainloop()
