from psychopy import visual, core, event
import random

# Create a window
win = visual.Window([800, 600], color="white", units="pix")

# Create a rotating merry-go-round
carousel_objects = [visual.Circle(win, radius=20, pos=(200, 0), fillColor="red", lineColor="red") for _ in range(5)]
angle_step = 360 / len(carousel_objects)

# Create tasks
math_task = "5 + 3 = ?"
chinese_characters = ["你好", "学习", "写字", "汉语"]

# Text stimuli for tasks
task_text = visual.TextStim(win, text="", color="black", pos=(0, 100))
input_text = visual.TextStim(win, text="Your answer: ", color="black", pos=(0, -100))

# Rotation speed
rotation_speed = 2  # Degrees per frame

# Main loop
clock = core.Clock()
while True:
    # Rotate carousel objects
    for i, obj in enumerate(carousel_objects):
        angle = clock.getTime() * rotation_speed + i * angle_step
        x = 200 * core.cos(angle * core.PI / 180)
        y = 200 * core.sin(angle * core.PI / 180)
        obj.pos = (x, y)
        obj.draw()

    # Display a random task
    task_text.text = random.choice([math_task, random.choice(chinese_characters)])
    task_text.draw()

    # Check for key presses
    keys = event.getKeys()
    if "escape" in keys:
        break  # Exit the loop
    elif keys:
        input_text.text = f"Your answer: {keys[-1]}"
    input_text.draw()

    # Flip the window
    win.flip()

# Close the window
win.close()
core.quit()
