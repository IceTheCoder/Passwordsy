import tkinter as tk

def open_first_window():
    # Create the first window
    first_window = tk.Toplevel(root)
    first_window.title("First Window")
    first_window.geometry("300x200")

    # Add a button to open the second window and hide the first window
    open_second_button = tk.Button(first_window, text="Open Second Window", command=lambda: open_second_window(first_window))
    open_second_button.pack(pady=20)

def open_second_window(first_window):
    # Hide the first window
    first_window.withdraw()

    # Create the second window
    second_window = tk.Toplevel(root)
    second_window.title("Second Window")
    second_window.geometry("300x200")

    # Bind the close event to destroy the second window and show the first window again
    def close_second_window():
        second_window.destroy()
        first_window.deiconify()
    second_window.protocol("WM_DELETE_WINDOW", close_second_window)

# Create the root window
root = tk.Tk()

# Add a button to open the first window
button = tk.Button(root, text="Open First Window", command=open_first_window)
button.pack(pady=20)

# Start the main event loop
root.mainloop()
