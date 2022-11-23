class Account:
    def __init__(self, _accountNumber, _accountHolderName, _rateOfInterest, _currentBalance):
        self._accountNumber = _accountNumber
        self._accountHolderName = _accountHolderName
        self._rateOfInterest = _rateOfInterest
        self._currentBalance = _currentBalance

    def getAccountNumber(self):
        return self._accountNumber

    def setAccountNumber(self, x):
        self._accountNumber = x

    def getAccountHolderName(self):
        return self._accountHolderName

    def setAccountHolderName(self, x):
        self._accountHolderName = x

    def getRateOfInterest(self):
        return self._rateOfInterest

    def setRateofInterest(self, x):
        self._rateOfInterest = x

    def getCurrentBalance(self):
        return self._currentBalance
    
    def setCurrentBalance(self, x):
        self._currentBalance = x

    def withdraw(self, withdraw):
        self._currentBalance -= withdraw
        #check if negative
        pass

    def deposit(self, deposit):
        self._currentBalance += deposit
        return deposit
        #check if negative

class Bank(Account):
    def __init__(self, _bankName):
        self._bankName = _bankName

    def getBankName(self):
        return self._bankName

    def setBankName(self, x):
        self._bankName = x

    def openAccount():
        pass

    def searchAccount():
        pass

class SavingAccount(Bank):
    def __init__(self, _minimumBalance):
        self._minimumBalance = _minimumBalance

    def getMinimumBalance(self):
        return self._minimumBalance

    def setMinimumBalance(self, x):
        self._minimumBalance = x

    def withdraw(self, withdraw):
        self._currentBalance -= withdraw
        #check if negative
        pass

class ChequingAccount(Bank):
    def __init__(self, _overdraftAllowed):
        self._overdraftAllowed = _overdraftAllowed

    def getOverdraftAllowed(self):
        return self._overdraftAllowed

    def setOverdraftAllowed(self, x):
        self._overdraftAllowed = x

    def withdraw(self, withdraw):
        self._currentBalance -= withdraw
        #check if negative
        pass

account1 = Bank("Account 1")
account2 = Bank("Account 2")
account3 = Bank("Account 3")
accounts = [account1, account2, account3]
selectedAccount = ""

def showAccountMenu(selectedAccount):
    return selectedAccount
    #	Check Balance: Display the balance of the selected account
    #	Deposit: Prompt the user for an amount to deposit and perform the deposit using the methods in account class. 
    #	Withdraw: Prompt the user for an amount to withdraw and perform the withdrawal using the methods in the account class. 
    #	Exit Account: go back to Banking Main Menu

def showMainMenu():
    print("~ MAIN MENU\n\nWould you like to select an account or exit?\n(select account / exit)\n\n")
    while True:
        accountOrExit = input("\u001b[245m> \u001b[0m").lower()
        if accountOrExit == "select account" or "select" or "s":
            break
        elif accountOrExit == "exit":
            print("\nVery well.\n")
            quit()
    print("\nVery well. Please select an account.\n\n")
    print("Account 1, Account 2, Account 3")
    while True:
        selectAccounts = input("\n\u001b[245m> \u001b[0m").lower()
        if selectAccounts == "account 1" or "1":
            selectedAccount = account1
        elif selectAccounts == "account 2" or "2":
            selectedAccount = account2
        elif selectAccounts == "account 3" or "3":
            selectedAccount = account3
        if selectedAccount in accounts:
            print("\nYou have selected your account.")
            break
        else:
            print("\nThat is not a valid account. Please try again.")
            print("Account 1, Account 2, Account 3")
    print(showAccountMenu(selectedAccount))
    showAccountMenu(selectedAccount)

def run():
    showMainMenu()

run()




