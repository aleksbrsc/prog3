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

def showAccountMenu(selectedAccount):
    print("\nSelected account:",Bank.getBankName(selectedAccount))
    print("Check Balance / Deposit / Withdraw / Exit Account\n")
    balanceOptions = ["check balance", "check", "c", "balance", "bal", "b"]
    depositOptions = ["deposit", "d"]
    withdrawOptions = ['withdraw', 'w']
    exitOptions = ["exit account", "exit", "e"]
    while True:
        accountMenu = input("\u001b[245m> \u001b[0m").lower()
        if accountMenu in balanceOptions:
            print("\nYour balance:",Bank.getCurrentBalance(selectedAccount))
            # ERROR HERE object has no value _currentBalance
        elif accountMenu in depositOptions:
            print("\nHow much would you like to deposit?\n")
        elif accountMenu in withdrawOptions:
            print("\nHow much would you like to withdraw?\n")
        elif accountMenu in exitOptions:
            print("\nVery well.\n")
            showMainMenu()
        else:
            print("\nThat is not a valid option. Please try again.")
            print("Check Balance / Deposit / Withdraw / Exit Account\n")
            
    #	Check Balance: Display the balance of the selected account
    #	Deposit: Prompt the user for an amount to deposit and perform the deposit using the methods in account class. 
    #	Withdraw: Prompt the user for an amount to withdraw and perform the withdrawal using the methods in the account class. 
    #	Exit Account: go back to Banking Main Menu

def showMainMenu():
    print("~ MAIN MENU\n\nWould you like to select an account or exit?\n(select account / exit)\n")
    selectAccountOptions = ["select account", "select", "s"]
    exitOptions = ["exit", "e"]
    while True:
        accountOrExit = input("\u001b[245m> \u001b[0m").lower()
        if accountOrExit in selectAccountOptions:
            break
        elif accountOrExit in exitOptions:
            print("\nVery well.\n")
            quit()
        else:
            print("\nThat was not a valid option. Please try again\n(select account / exit)\n")
    print("\nVery well. Please select an account.\n\n")
    print("Account 1, Account 2, Account 3")
    account1options = ["account 1","1","one"]
    account2options = ["account 2","2","two"]
    account3options = ["account 3","3","three"]
    while True:
        selectAccount = input("\n\u001b[245m> \u001b[0m").lower()
        if selectAccount in account1options:
            selectAccount = account1
        elif selectAccount in account2options:
            selectAccount = account2
        elif selectAccount in account3options:
            selectAccount = account3
        if selectAccount in accounts:
            break
        else:
            print("\nThat is not a valid account. Please try again.")
            print("Account 1, Account 2, Account 3")
    showAccountMenu(selectAccount)

def run():
    showMainMenu()

run()