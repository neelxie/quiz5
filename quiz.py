class BankAccount:

  def __init__(self, account_number, balance, name, type):
    self.account_number = account_number
    self.balance = balance
    self.name = name
    self.type = type

  def __repr__(self):
    return f"Account number: {self.account_number} \nBalance: {self.balance}"

class Customer:
  def __init__(self, name, accounts):
    self.name = name
    self.accounts = accounts

  def __repr__(self):
    return f"Customer Name: {self.name}"

  def add_account(self, account):
    self.accounts.append(account)
class Bank:

  def __init__(self, name, accounts):
    self.name = name
    self.accounts = accounts

  def __repr__(self):
    return f"Bank Name: {self.name}"

  def add_account(self, account):
    self.accounts.append(account)

class Transactions:
  def __init__(self, account, amount, type):
    self.account = account
    self.amount = amount
    self.type = type

  def post_transaction(self):
    if self.type == "Deposit":
      self.account.balance = self.account.balance + self.amount
    if self.type == "Withdraw" and self.account.balance >= self.amount:
      self.account.balance = self.account.balance - self.amount

my_bank = Bank("Stanbic", [])

my_customer = Customer("Derrick Sekidde", [])

my_bank_account = BankAccount("100000001", 99999.9, "Derrick Sekidde", "Fixed Deposit")

my_bank.add_account(my_bank_account)

my_customer.add_account(my_bank_account)

print(my_bank)
print(my_customer)
print(my_bank_account)

my_transaction = Transactions(my_bank_account, 90000.0, "Deposit")
my_transaction.post_transaction()