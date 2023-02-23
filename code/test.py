import tkinter as tk

def popup(event):
    if menu.posted:
        menu.unpost()
    else:
        menu.post(event.x_root, event.y_root)
        menu.posted = True

root = tk.Tk()

# Create a popup menu
menu = tk.Menu(root, tearoff=0)
menu.add_command(label="Cut")
menu.add_command(label="Copy")
menu.add_command(label="Paste")
menu.posted = False

# Bind the popup menu to the Ctrl key
root.bind("<Control_L>", popup)

# Create a text widget
text = tk.Text(root)
text.pack()

root.mainloop()
