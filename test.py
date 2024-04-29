## Imports
import unittest
## accessing classes
from main import tkinterApp, WelcomePage, LoginPage, CreateAccountPage, OptionsPage

class TestBankAccountProgram(unittest.TestCase):
    # constructor
    def __init__(self):
        self.app = tkinterApp()

    ## Testing main functions
    # testing withdraw
    def testWithdraw(self):
        username = "testUser"
        amount = 100.00

        # assertions to check username and amount valid
        self.assertTrue(username)
        self.assertIsInstance(amount, (int, float)) 


    # testing deposit
    def testDeposit(self):
        username = "testUser"
        amount = 100.00

        # assertions to check username and amount valid
        self.assertTrue(username)
        self.assertIsInstance(amount, (int, float)) 


    # testing checkBalance
    def testCheckBalance(self):
        username = "testUser"

        # assertions to check username
        self.assertTrue(username)

    # testing deleteAccount
    def testCheckBalance(self):
        username = "testUser"

        # assertions to check username
        self.assertTrue(username)
    

    # testing login
    def testLogin(self):
        username = "testUser"
        password = "testPassword"

        # assertiosn to check username y password not empty
        self.assertTrue(username)
        self.assertTrue(password)

    # testing creating account
    def testCreateAccount(self):
        username = "testUser"
        password = "testPassword"
        email = "testUser@gmail.com"
        initialBalance = 100.00

        # assertions to check all variables have values
        self.assertTrue(username) # checking not empty
        self.assertTrue(password) ##
        self.assertTrue(email) ###
        self.assertIsInstance(initialBalance, (int, float)) # checking it a num

if __name__ == '__main__':
    unittest.main()