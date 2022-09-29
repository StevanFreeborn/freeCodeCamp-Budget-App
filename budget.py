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

def get_border_text(categories):
  border_text = "    "
  
  for category in categories:
    border_text += "-" * 3

  border_text += "-"

  return border_text

def get_total(categories):
  categories_total = 0
  
  for category in categories:
    for item in category.ledger:
      amount = item["amount"]
      if amount < 0:
        categories_total += amount

  return int(categories_total * -1)

def get_category_totals(categories):
  category_totals = []
  
  for category in categories:
    category_total = 0
    
    for item in category.ledger:
      amount = item["amount"]
      if amount < 0:
        category_total += amount

    category_total = int(category_total * -1)
    category_totals.append(category_total)

  return category_totals

def get_bar_text(categories):
  value_text = ""
  
  categories_total = get_total(categories)
  category_totals = get_category_totals(categories)
  
  i = 100

  while i >= 0:
    i_as_str = str(i)
    i_len = len(i_as_str)
    i_diff = 3 - i_len
    
    value_text += (" " * i_diff) + i_as_str + "|"
    
    for total in category_totals:
      category_percentage = int((total / categories_total) * 100)
      if category_percentage >= i:
        value_text += " o "
      else:
        value_text += "   "

    if i != 0:
      value_text += " \n"
    else:
      value_text += " "
    
    i-=10

  return value_text

def get_labels_text(categories):
  labels_text = ""
  
  # build a list of all the labels
  labels = []

  for category in categories:
    labels.append(category.name)

  # get the longest label in the list of labels
  longest_label = max(labels, key=len)

  # get the length of the longest label
  longest_label_len = len(longest_label)

  # create a list of index values for the longest label
  # and peform a loop for each index value in the list
  # for example if longest label is 5 characters in length
  # we will create a list of numbers (0,1,2,3,4) and perform
  # a loop for each value.
  for index in range(longest_label_len):

    # at the begging of each label text there
    # should be four spaces
    labels_text += "    "

    # perform a loop over the list of labels
    for label in labels:

      # for each label check if the current index
      # value is greater than the length of the label.
      # this would indicate that we've already iterated
      # over each character in the current label.
      # therefore there is no character in the current label at the
      # current index value.
      # so we just need to add three spaces to the label text
      if index >= len(label):
        labels_text += "   "
      # otherwise it is safe to get the character at the current index
      # from the current label and append it to the label text
      # with a space on each side
      else:
        labels_text += " " + label[index] + " "

    # before we move on to the next index value
    # we want to check if we've reached the last
    # index value which would be the number we get
    # when we subtract one from the longest labels
    # length. if we haven't reached that point then
    # we want to add a new line character or else
    # just an empty space before begining
    # the next loop and building the next line of label text.
    if index != longest_label_len - 1:
      labels_text += " \n"
    else:
      labels_text += " "

  return labels_text

def create_spend_chart(categories):
  lines_of_text = []

  chart_title = "Percentage spent by category"
  lines_of_text.append(chart_title)

  bar_text = get_bar_text(categories)
  lines_of_text.append(bar_text)
  
  border_text = get_border_text(categories)
  lines_of_text.append(border_text)

  labels_text = get_labels_text(categories)
  lines_of_text.append(labels_text)
  
  return "\n".join(lines_of_text)