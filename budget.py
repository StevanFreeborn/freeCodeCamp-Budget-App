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

  def transfer(self, amount, category):
    has_funds_available = self.check_funds(amount)

    if has_funds_available:
      self.withdraw(amount, f'Transfer to {category.name}')
      category.deposit(amount, f'Transfer from {self.name}')
      return True

    return False

  def __str__(self):
    lines_of_text = []
    
    name_len = len(self.name)
    num_of_asterisks = 30 - name_len
    left_asterisks = int(num_of_asterisks / 2)
    right_asterisks = num_of_asterisks - left_asterisks
    
    title = ("*" * left_asterisks) + self.name + ("*" * right_asterisks)
    lines_of_text.append(title)
    
    for item in self.ledger:
      item_text = ""
      
      description = item["description"]
      description_len = len(description)
      
      if description_len > 23:
        description = description[:23]

      description_len = len(description)
      
      item_text += description

      amount = str(item["amount"])
      
      if "." not in amount:
        amount += ".00"

      amount_len = len(amount)

      num_of_spaces = 30 - (description_len + amount_len)

      amount = (" " * num_of_spaces) + amount
      
      item_text += amount
      
      lines_of_text.append(item_text)

    balance = str(self.get_balance())
    total_text = f'Total: {balance}' 
    lines_of_text.append(total_text)
    
    return "\n".join(lines_of_text)

def create_spend_chart(categories):
  print("TODO: implement creating a spend chart")