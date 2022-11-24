import bank
import chequingAccount
import savingsAccount

class Account:
    def __init__(self, _bankName, _accountNumber, _accountHolderName, _rateOfInterest, _minimumSavingsBalance, _savingsBalance,  _chequingBalance, _overdraftAllowed):
        self._accountNumber = _accountNumber
        self._accountHolderName = _accountHolderName
        self._rateOfInterest = _rateOfInterest
        self._bankName = bank.Bank(_bankName)
        self._savingsAccount = savingsAccount.SavingsAccount(_minimumSavingsBalance, _savingsBalance)
        self._chequingAccount = chequingAccount.ChequingAccount(_chequingBalance, _overdraftAllowed)

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