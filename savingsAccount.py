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