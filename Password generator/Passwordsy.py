import random
from tkinter import *

root = Tk()

characterList = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','0','1','2','3','4','5','6','7','8','9','~','`','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}',']','|',':',';','<','>',',','.','?','/']
global password
password = ""

root.minsize(854, 240)
root.maxsize(854, 240)
root.grid_rowconfigure(7, weight = 1)
root.grid_columnconfigure(0, weight = 1)
root.resizable(0,0)
root.iconphoto(False, PhotoImage(file="logo.png"))
root.title("Passwordsy")

Welcome = Label(root, text = "Passwordsy", font = 'Helvetica 24')
Welcome.grid(row = 1)
Welcome.grid_rowconfigure(1, weight = 1)
Welcome.grid_columnconfigure(1, weight = 1)

Question = Label(root, text = "(up to 100) Number of characters:", font = 'Helvetica 12')
Question.grid(row = 3)
Question.grid_rowconfigure(1, weight = 1)
Question.grid_columnconfigure(1, weight = 1)

Input = Entry(root, width = 10, borderwidth = 2)
Input.grid(row = 4)
Input.grid_rowconfigure(1, weight = 1)
Input.grid_columnconfigure(1, weight = 1)

Tip = Label(root, text = "CTRL + C to copy \nCTRL + V to paste", font = 'Helvetica 12')
Tip.grid(row = 2)
Tip.grid_rowconfigure(1, weight = 1)
Tip.grid_columnconfigure(1, weight = 1)

def Click():
    '''After clicking on the done button,
        it generates a password,
        and shows it on the screen.
    '''
    lengthStr = Input.get()
    lengthFloat = float(lengthStr)
    lengthInt = int(lengthFloat) # Gets the length the user requested.
    if lengthInt > 100:
        lengthInt = 100 # Maxes it out at 100.
    while lengthInt > 0:
        global password 
        password = password + characterList[random.randint(0, 90)]
        lengthInt = lengthInt- 1 # Chooses random random characters

    passwordLabel = Text(root, width=100, height = 1, borderwidth = 0, font = 'Consolas 11')
    passwordLabel.insert(1.0, password)
    passwordLabel.grid(row = 6, pady = 10) # Shows the password.
    passwordLabel.configure(state = "disabled") # Makes it uneditable.
    passwordLabel.grid_rowconfigure(1, weight = 1)
    passwordLabel.grid_columnconfigure(1, weight = 1)

    password = ""

done_btn = PhotoImage(file="doneButton.png")

doneBtn = Button(root, image = done_btn, command=Click, borderwidth = 0)
doneBtn.grid(row = 5, column = 0, pady = 10, sticky="nsew")
doneBtn.grid_rowconfigure(0, weight = 1)
doneBtn.grid_columnconfigure(0, weight = 1)

root.mainloop()
