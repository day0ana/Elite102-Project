# IMPORTS
import tkinter as tk
from tkinter import ttk
import tkinter.simpledialog as simpledialog
from tkinter import messagebox

## connector
import mysql.connector

# Establishing Connection
connect = mysql.connector.connect(
    user = "root",
    password = "HUEvos72**ahUU3",
    database = "bankSchema"
)

# Making changes to database 
cursor = connect.cursor()

# Classes
## tkinterApp class
class tkinterApp(tk.Tk):
    # constructor
    def __init__(self, *args, **kwargs):
        # initialization of tkinter app
        tk.Tk.__init__(self, *args, **kwargs)

        # container frame
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)

        # dictionary for frames
        self.frames = {}

        # loop thru each frame/PAGE
        for F in (WelcomePage, LoginPage, CreateAccountPage, OptionsPage):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        # outputting WelcomePage (first page to be shown)
        self.showFrame(WelcomePage)

    # changing pages/classes
    def showFrame(self, cont):
        # get frame from dictionary
        frame = self.frames[cont]
        frame.tkraise()


## WelcomePage
class WelcomePage(tk.Frame):
    # constructor
    def __init__(self, parent, controller):
        # initilization
        tk.Frame.__init__(self,parent)

        # welcome label 
        welcomeLabel = ttk.Label(self, text="Welcome Page", font=("Arial",15))
        welcomeLabel.grid(row=0, column=6, padx=10, pady=10)
        # button to switch to loginPage
        loginPageButton = ttk.Button(self, text ="Login", command = lambda : controller.showFrame(LoginPage))
        loginPageButton.grid(row = 1, column = 6, padx = 10, pady = 10)
        # button to switch to createAccountPage
        createPageButton = ttk.Button(self, text ="Create Account", command = lambda : controller.showFrame(CreateAccountPage))
        createPageButton.grid(row = 2, column = 6, padx = 10, pady = 10)

## LoginPage
class LoginPage(tk.Frame):
    # constructor 
    def __init__(self, parent, controller):
        # intiialization
        tk.Frame.__init__(self,parent)
        self.controller = controller 
        
        # label = ttk.Label(self,text="pg1")
        # label.grid(row=0, column=4, padx=10, pady=10)

        # switch to welcomePage button
        welcomePageButtom = ttk.Button(self, text ="Welcome Page", command = lambda : controller.showFrame(WelcomePage))
        welcomePageButtom.grid(row = 1, column = 1, padx = 10, pady = 10)
        # switch to createAccountPage button
        createPageButton = ttk.Button(self, text ="Create Account", command = lambda : controller.showFrame(CreateAccountPage))
        createPageButton.grid(row = 2, column = 1, padx = 10, pady = 10)

        ## Required info
        # username 
        usernameLabel = ttk.Label(self, text="Username:")
        usernameLabel.grid(row=0, column=4, padx=10, pady=10)
        self.username_entry = ttk.Entry(self)
        self.username_entry.grid(row=1, column=4, padx=10, pady=10)
        # password 
        passwordLabel = ttk.Label(self, text="Password:")
        passwordLabel.grid(row=2, column=4, padx=10, pady=10)
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.grid(row=3, column=4, padx=10, pady=10)


        # login button
        loginButton = ttk.Button(self, text="Login", command=self.login)
        loginButton.grid(row=4, column=4, padx=10, pady=10)

    # loginButton
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        # switch to OptionsPage
        self.controller.showFrame(OptionsPage)

## CreateAccountPage
class CreateAccountPage(tk.Frame):
    # constructor
    def __init__(self, parent, controller):
        # inittialization
        tk.Frame.__init__(self,parent)
        self.controller = controller 

        # label = ttk.Label(self,text="pg1")
        # label.grid(row=0, column=4, padx=10, pady=10)

        # switch to loginPage button
        loginPageButton = ttk.Button(self, text ="Login", command = lambda : controller.showFrame(LoginPage))
        loginPageButton.grid(row = 1, column = 1, padx = 10, pady = 10)
        # switch to welcomePage button
        welcomePageButton = ttk.Button(self, text ="Welcome Page", command = lambda : controller.showFrame(WelcomePage))
        welcomePageButton.grid(row = 2, column = 1, padx = 10, pady = 10)

        # Required info to create account
        # username 
        usernameLabel = ttk.Label(self, text="Username:")
        usernameLabel.grid(row=0, column=4, padx=10, pady=10)
        self.username_entry = ttk.Entry(self)
        self.username_entry.grid(row=1, column=4, padx=10, pady=10)
        # password 
        passwordLabel = ttk.Label(self, text="Password:")
        passwordLabel.grid(row=2, column=4, padx=10, pady=10)
        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.grid(row=3, column=4, padx=10, pady=10)
        # email 
        emailLabel = ttk.Label(self, text="Email:")
        emailLabel.grid(row=4, column=4, padx=10, pady=10)
        self.email_entry = ttk.Entry(self, show="*")
        self.email_entry.grid(row=5, column=4, padx=10, pady=10)
        
        # create button
        createButton = ttk.Button(self, text="Login", command=self.createAccount)
        createButton.grid(row=6, column=4, padx=10, pady=10)

    # creating account button
    def createAccount(self):
        # setting required info
        username = self.username_entry.get()
        password = self.password_entry.get()
        email = self.email_entry.get()
        initialBalance = simpledialog.askfloat("Initial Balance", "Enter the initial balance:")

        # checking the user enters balance to continue
        if initialBalance is not None:
            # sending to database
            cursor.execute("INSERT INTO accounts (username, password, balance, email) VALUES (%s, %s, %s, %s)", (username, password, initialBalance, email))
            connect.commit()
            messagebox.showinfo("Account Created", "Account created successfully!")
            # switching to OptionsPage afterwards
            self.controller.showFrame(OptionsPage)
        else:
            # if balance is not a number then give warning
            messagebox.showwarning("Initial Balance", "Invalid initial balance OR account creation cancelled.")

        

        
# Options
class OptionsPage(tk.Frame):
    # constructor
    def __init__(self, parent, controller):
        # intialization
        tk.Frame.__init__(self,parent)
        #self.username = username

        # label = ttk.Label(self,text="pg1")
        # label.grid(row=0, column=4, padx=10, pady=10)

        # switching to welcomePage button
        welcomePageButton = ttk.Button(self, text ="Welcome Page", command = lambda : controller.showFrame(WelcomePage))
        welcomePageButton.grid(row = 1, column = 1, padx = 10, pady = 10)

        ## Required info
        # username 
        usernameLabel = ttk.Label(self, text="Username:")
        usernameLabel.grid(row=2, column=4, padx=10, pady=10)
        self.username_entry = ttk.Entry(self)
        self.username_entry.grid(row=3, column=4, padx=10, pady=10)

        ## Actions Possible
        # deposit
        depositButton = ttk.Button(self, text="Deposit", command=self.deposit)
        depositButton.grid(row=4, column=4, padx=10, pady=10)
        # withdraw
        withdrawButton = ttk.Button(self, text="Withdraw", command=self.withdraw)
        withdrawButton.grid(row=5, column=4, padx=10, pady=10)
        # check balance
        checkBalanceButton = ttk.Button(self, text="Check Balance", command=self.checkBalance)
        checkBalanceButton.grid(row=6, column=4, padx=10, pady=10)
        # delete account
        deleteAccountButton = ttk.Button(self, text="Delete Account", command=self.deleteAccount)
        deleteAccountButton.grid(row=7, column=4, padx=10, pady=10)

    # withdrawing amount from account
    def withdraw(self):
        # prompts user for amount
        amount = simpledialog.askfloat("Withdrawing Amount", "Enter the amount to withdraw: ")
        username = self.username_entry.get()
        balance = cursor.fetchone()

        # changes balance in database
        #cursor.execute("SELECT balance FROM accounts WHERE username=%s",(username,))
        
        # if there is enough money from user's balance to be withdrawn 
        if balance >= amount:
            # updating database
            cursor.execute("UPDATE accounts SET balance = balance - %s WHERE username=%s", (amount, username))
            connect.commit()
            # informs user of changes
            messagebox.showinfo("Amount Withdrawn", f"Withdrew ${amount} from {username}")
        else:
            # informs user unavainility to withdraw money
            messagebox.showinfo("Amount Unable to be Withdrawn", "Insufficient funds or other error")
    
    # depositing from amount
    def deposit(self):
        # prompts user for amount
        amount = simpledialog.askfloat("Depositing Amount", "Enter the amount to deposit: ")
        username = self.username_entry.get()
        
        # updates user's balance
        cursor.execute("UPDATE accounts SET balance = balance + %s WHERE username=%s", (amount, username))
        connect.commit()
        # informs user of changes
        messagebox.showinfo("Amount Depsoit", f"Deposited ${amount} to {username}")

    # checking balance
    def checkBalance(self):
        username = self.username_entry.get()

        # gets balance from database
        cursor.execute("SELECT balance FROM accounts WHERE username = %s", (username,))
        currentBalance = cursor.fetchone()[0]
        # informs user of balance
        messagebox.showinfo("Check Balance", f"Current balance: {currentBalance}")

    # deleting account
    def deleteAccount(self):
        username = self.username_entry.get()

        # double checking if user wants to delete account
        confirmation = messagebox.askyesno("Deleting Account", f"Do you wish to delete the account for {username}")

        if confirmation: # if yes
            # delete account
            cursor.execute("DELETE FROM accounts WHERE username = %s", (username,))
            connect.commit()
            # informs user of deletion
            messagebox.showinfo("Account Deleted", f"The account for {username} has been successfully deleted.")
        else: # if no
            # informs user of cancaletion
            messagebox.showinfo("Deletion Cancelled", "Account deletion cancelled.")

# End GUIs
if __name__ == "__main__":
    app = tkinterApp()
    app.title("Bank Account Program")
    app.geometry("500x500")  
    app.mainloop()
