class ChequingAccount():
    def __init__(self, _chequingBalance, _overdraftAllowed):
        self._chequingBalance = _chequingBalance
        self._overdraftAllowed = _overdraftAllowed
        
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