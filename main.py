# imports
#import mysql.connector
## GUIS
import tkinter as tk
from tkinter import messagebox

# Functions
def exitProgram():
    root.destroy()

def displayOption1():
    messagebox.showinfo("Option 1", "One one")

def displayOption2():
    messagebox.showinfo("Option 2", "Two two")

def displayOption3():
    messagebox.showinfo("Option 3", "Three three")

# GUI
root = tk.Tk()
root.title("BankAccount Program")
root.geometry("300x300")

# Menu Bar
menuBar= tk.Menu(root)

# Menu Options
menuOne = tk.Menu(menuBar, tearoff=0)
menuOne.add_command(label="Option 1", command=displayOption1)
menuOne.add_command(label="Option 2", command=displayOption2)
menuOne.add_command(label="Option 3", command=displayOption3)

menuBar.add_cascade(label="Options", menu=menuOne)

# Display Menu
root.config(menu=menuBar)

# Welcoming Users
welcomeLabel = tk.Label(root, text="Welcome to Bank Program!", font=("Arial", 15))
welcomeLabel.pack(pady=20)

# Exit Window
exitButton = tk.Button(root, text="Exit", command=exitProgram)
exitButton.pack(pady=10)

root.mainloop()
