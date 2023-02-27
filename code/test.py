import tkinter as tk

root = tk.Tk()

# check if the window exists before calling winfo_width
if root.winfo_exists():
    width = root.winfo_width()
    print(f"Window width is {width}.")
else:
    print("Window does not exist.")

# destroy the window
root.destroy()

# check if the window exists before calling winfo_height
try:
    if root.winfo_exists():
        height = root.winfo_height()
        print(f"Window height is {height}.")
    else:
        print("Window does not exist.")
except:
    print("Window does not exist.")
