class Category:
  def __init__(self, name):
    self.name = name
    self.ledger = []

  def deposit(self, amount, description=""):
    self.ledger.append({ "amount": amount, "description": description })

  def get_balance(self):
    balance = 0

    for item in self.ledger:
      balance += item["amount"]

    return balance

  def check_funds(self, amount):
    balance = self.get_balance()

    if amount > balance:
      return False
    
    return True

  def withdraw(self, amount, description=""):
    has_funds_available = self.check_funds(amount)

    if has_funds_available:
      amount = amount * -1
      self.ledger.append({ "amount": amount, "description": description })
      return True
    
    return False

  # TODO: Implement transfer
  def transfer(self, amount, category):
    print("made transfer")

def create_spend_chart(categories):
  print("TODO: implement creating a spend chart")