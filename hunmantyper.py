import tkinter as tk
import pyautogui
import time
import random

# Global variable to control the typing loop
stop_typing = False

def type_like_human(text):
    global stop_typing
    words = text.split()
    word_count = 0
    
    for word in words:
        if stop_typing:
            break
        for char in word:
            # Introduce a random chance of a spelling error
            if random.random() < error_rate.get() / 100:  # Adjusted by slider
                wrong_char = chr(random.randint(97, 122))  # Random lowercase letter
                pyautogui.typewrite(wrong_char)
                time.sleep(random.uniform(0.05, 0.2))
                # Adjust error correction rate by slider
                if random.random() < correction_rate.get() / 100:
                    pyautogui.press('backspace')  # Simulate correcting the error
            pyautogui.typewrite(char)
            time.sleep(random.uniform(typing_speed.get() / 1000, typing_speed.get() / 500))  # Adjusted by slider
        
        pyautogui.typewrite(' ')  # Space after each word
        word_count += 1

        # Add a random delay after a random number of words
        if word_count >= random.randint(2, int(pause_frequency.get())):
            time.sleep(random.uniform(pause_duration.get(), pause_duration.get() + 2))  # Adjusted by slider
            word_count = 0

def on_submit():
    global stop_typing
    stop_typing = False
    text = text_box.get("1.0", tk.END).strip()  # Get the text from the textbox
    time.sleep(2)  # Small delay to switch to the target application
    type_like_human(text)

def on_stop():
    global stop_typing
    stop_typing = True

# Create the main application window
root = tk.Tk()
root.title("Human-like Typing Simulator")

# Create and place the text box
text_box = tk.Text(root, height=10, width=50)
text_box.pack(pady=10)

# Create and place the submit button
submit_button = tk.Button(root, text="Type it out!", command=on_submit)
submit_button.pack(side=tk.LEFT, padx=10)

# Create and place the stop button
stop_button = tk.Button(root, text="Stop", command=on_stop)
stop_button.pack(side=tk.RIGHT, padx=10)

# Create and place the sliders
typing_speed = tk.Scale(root, from_=0.001, to_=10, label="Typing Speed (ms/keystroke)", orient=tk.HORIZONTAL)
typing_speed.set(200)
typing_speed.pack(pady=5)

error_rate = tk.Scale(root, from_=0, to_=100, label="Spelling Error Rate (%)", orient=tk.HORIZONTAL)
error_rate.set(5)
error_rate.pack(pady=5)

correction_rate = tk.Scale(root, from_=0, to_=100, label="Error Correction Rate (%)", orient=tk.HORIZONTAL)
correction_rate.set(90)
correction_rate.pack(pady=5)

pause_frequency = tk.Scale(root, from_=0, to_=10, label="Pause Frequency (words)", orient=tk.HORIZONTAL)
pause_frequency.set(5)
pause_frequency.pack(pady=5)

pause_duration = tk.Scale(root, from_=0, to_=5, label="Pause Duration (seconds)", orient=tk.HORIZONTAL)
pause_duration.set(2)
pause_duration.pack(pady=5)

# Run the application
root.mainloop()
