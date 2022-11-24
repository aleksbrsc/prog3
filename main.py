class Account:
    def __init__(self, _bankName, _accountNumber, _accountHolderName, _rateOfInterest, _minimumSavingsBalance, _savingsBalance,  _chequingBalance, _overdraftAllowed):
        self._accountNumber = _accountNumber
        self._accountHolderName = _accountHolderName
        self._rateOfInterest = _rateOfInterest
        self._bankName = Bank(_bankName)
        self._savingsAccount = SavingsAccount(_minimumSavingsBalance, _savingsBalance)
        self._chequingAccount = ChequingAccount(_chequingBalance, _overdraftAllowed)

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

class Bank():
    def __init__(self, _bankName):
        self._bankName = _bankName

    def getBankName(self):
        return self._bankName

    def setBankName(self, x):
        self._bankName = x

    def searchAccount():
        pass

class SavingsAccount():
    def __init__(self, _minimumSavingsBalance, _savingsBalance):
        self._minimumSavingsBalance = _minimumSavingsBalance
        self._savingsBalance = _savingsBalance

    def getMinimumSavingsBalance(self):
        return self._minimumSavingsBalance

    def setMinimumSavingsBalance(self, x):
        self._minimumSavingsBalance = x

    def getSavingsBalance(self):
        return self._savingsBalance

    def setSavingsBalance(self, x):
        self._savingsBalance = x

    def deposit(self, amount):
        self._savingsBalance += amount
        return f"You deposited ${amount}, your new balance is ${self.getSavingsBalance()}."

    def withdraw(self, amount):
        self._savingsBalance -= amount
        return f"You have withdrawn ${amount}, your new balance is ${self.getSavingsBalance()}."

class ChequingAccount():
    def __init__(self, _chequingBalance, _overdraftAllowed):
        self._overdraftAllowed = _overdraftAllowed
        self._chequingBalance = _chequingBalance
    
    def getChequingBalance(self):
        return self._chequingBalance

    def setChequingBalance(self, x):
        self._chequingBalance = x

    def getOverdraftAllowed(self):
        return self._overdraftAllowed

    def setOverdraftAllowed(self, x):
        self._overdraftAllowed = x

    def deposit(self, amount):
        self._chequingBalance += amount
        return f"You deposited ${amount}, your new balance is ${self.getChequingBalance()}."

    def withdraw(self, amount):
        self._chequingBalance -= amount
        return f"You have withdrawn ${amount}, your new balance is ${self.getChequingBalance()}."

#stringBANKNAME, accountNumber, stringHOLDERNAME, rateofinterest, minimumSavingsBalance, savingsBalance, chequingBalance, overdraftAllowed
account1 = Account("Bing Chilling Bank", 1, "Holder 1", 1, 100, 1000, 1000, 100)
account2 = Account("Bing Chilling Bank", 2, "Holder 1", 1, 100, 1000, 1000, 100)
account3 = Account("Bing Chilling Bank", 3, "Holder 1", 1, 100, 1000, 1000, 100)
accounts = [account1, account2, account3]

def showAccountMenu(selectedAccount):
    print("\nSelected account:", Account.getAccountNumber(selectedAccount))
    print("Would you like to enter your Chequing or Savings account?\n")
    chequingOptions = ["chequing account", "chequing", "c"]
    savingsOptions = ["savings account", "savings", "saving", "s"]
    while True:
        savingsOrChequing = input("\u001b[245m> \u001b[0m").lower()
        if savingsOrChequing in savingsOptions:
            selectedSOC = "savings"
            break
        elif savingsOrChequing in chequingOptions:
            selectedSOC = "chequing"
            break
        else: 
            print("\nThat is not a valid option. Please try again.")
            print("Would you like to enter your Chequing or Savings account?\n")
    print("\nCheck Balance / Deposit / Withdraw / Exit Account\n")
    balanceOptions = ["check balance", "check", "c", "balance", "bal", "b"]
    depositOptions = ["deposit", "d"]
    withdrawOptions = ['withdraw', 'w']
    exitOptions = ["exit account", "exit", "e"]
    while True:
        accountMenu = input("\u001b[245m> \u001b[0m").lower()
        if accountMenu in balanceOptions:
            # change this for chequing and savings
            if selectedSOC == "savings":
                print("\nYour balance:",selectedAccount._savingsAccount.getSavingsBalance())
            elif selectedSOC == "chequing":
                print("\nYour balance:",selectedAccount._chequingAccount.getChequingBalance())
            print("\nCheck Balance / Deposit / Withdraw / Exit Account\n")
        elif accountMenu in depositOptions:
            amount = 0
            print("\nHow much would you like to deposit?\n")
            if selectedSOC == "savings":
                while True:
                    try: 
                        amount = float(input("\u001b[245m> \u001b[0m"))
                    except: pass
                    if amount > 0:
                        print("\n",selectedAccount._savingsAccount.deposit(amount))
                        print("\nCheck Balance / Deposit / Withdraw / Exit Account\n")
                        break
                    else:
                        print("\nInvalid deposit (amount must be a number greater than 0\n")
            elif selectedSOC == "chequing":
                while True:
                    try: 
                        amount = float(input("\u001b[245m> \u001b[0m"))
                    except: pass
                    if amount > 0:
                        print("\n",selectedAccount._chequingAccount.deposit(amount))
                        print("\nCheck Balance / Deposit / Withdraw / Exit Account\n")
                        break
                    else:
                        print("\nInvalid withdrawal (amount must be a number greater than 0\n")
        elif accountMenu in withdrawOptions:
            amount = 0
            print("\nHow much would you like to withdraw?\n")
            if selectedSOC == "savings":
                while True:
                    try: 
                        amount = float(input("\u001b[245m> \u001b[0m"))
                    except: pass
                    if amount > 0 and ((selectedAccount._savingsAccount.getSavingsBalance() - amount) >= selectedAccount._savingsAccount.getMinimumSavingsBalance()):
                        print("\n",selectedAccount._savingsAccount.withdraw(amount))
                        print("\nCheck Balance / Deposit / Withdraw / Exit Account\n")
                        break
                    else:
                        print("\nInvalid withdrawal (amount must be a number greater than 0 that doesn't impede on your minimum balance requirement")
                        print("[1] Try again\n[2] Exit\n")
                        while True:
                            try: 
                                tryOrExit = input("\u001b[245m> \u001b[0m")
                            except: pass
                            if tryOrExit == "1":
                                print("\nHow much would you like to withdraw?\n")
                                break
                            elif tryOrExit == "2":
                                print("")
                                showAccountMenu(selectedAccount)
                            else:
                                print("\nInvalid option")
                                print("[1] Try again\n[2] Exit\n")
            elif selectedSOC == "chequing":
                while True:
                    try: 
                        amount = float(input("\u001b[245m> \u001b[0m"))
                    except: pass
                    if amount > 0 and ((selectedAccount._chequingAccount.getChequingBalance() - amount) >= (0 - selectedAccount._chequingAccount.getOverdraftAllowed())):
                        print("\n",selectedAccount._chequingAccount.withdraw(amount))
                        print("\nCheck Balance / Deposit / Withdraw / Exit Account\n")
                        break
                    else:
                        print("\nInvalid withdrawal (amount must be a number greater than 0 that doesn't impede on your overdraft limit\n")
                        print("[1] Try again\n[2] Exit\n")
                        while True:
                            try: 
                                tryOrExit = input("\u001b[245m> \u001b[0m")
                            except: pass
                            if tryOrExit == "1":
                                print("\nHow much would you like to withdraw?\n")
                                break
                            elif tryOrExit == "2":
                                print("")
                                showAccountMenu(selectedAccount)
                            else:
                                print("\nInvalid option")
                                print("[1] Try again\n[2] Exit\n")
        elif accountMenu in exitOptions:
            print("\nVery well.\n")
            showMainMenu()
        else:
            print("\nThat is not a valid option. Please try again.")
            print("Check Balance / Deposit / Withdraw / Exit Account\n")
    
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