import tkinter


class Frame:

    def __init__(self):
        self.root = tkinter.Tk()
        self.root.geometry("500x500")
        self.main = tkinter.Label(self.root, height=500, width=500, bg="#FFFFFF")
        text = tkinter.Text(self.root)
        text.insert("1.0", "Right click to open the popup.")
        text.pack()
        self.main.pack()

    def window(self):
        global window
        window = tkinter.Toplevel(self.root)
        self.btn = tkinter.Button(window, text="Close", command=window.destroy).pack()
        return window

    def destroy_window(self, event):
        window.destroy()

    def open_window(self, event):
        window = self.window()
        window.grab_set()
        window.focus_force()
        window.geometry(f"+{x}+{y}")
        window.bind("<Control_L>", self.destroy_window)

    def run(self):
        self.root.bind("<Button-3>", self.open_window)
        tkinter.mainloop()


window = Frame()
window.run()
