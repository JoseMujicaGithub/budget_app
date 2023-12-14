class Category:

  def __init__(self, name):
    self.name = name
    self.balance = 0
    self.ledger = []

  def __str__(self):
    title = f"{self.name:*^30}\n"
    items=""
    total=0
    for i in self.ledger:
      items+=f"{i['description'][0:23]:23}" + f"{i['amount']:>7.2f}"+"\n"
      total+=i['amount']
    return title+items+"Total: "+str(total)

  def deposit(self,amount,description=""):
    self.balance += amount
    self.ledger.append({"amount": amount, "description": description})


  def withdraw(self,amount,description=""):
    if (self.check_funds(amount)):
      self.ledger.append({"amount": - amount, "description": description})
      self.balance -= amount
      return True
    else:
      return False


  def get_balance(self):
    return self.balance

  def transfer(self,amount,another_budget):
    if (self.check_funds(amount)):
      self.withdraw(amount,"Transfer to " + another_budget.name)
      another_budget.deposit(amount,"Transfer from " + self.name)
      return True
    else:      
      return False

  
  def check_funds(self,amount):
    if self.balance < amount:
      return False
    else:
      return True  

def create_spend_chart(categories):
  spent_amounts = []
# Get total spent in each category
  for category in categories:
    spent = 0
    for item in category.ledger:
      if item["amount"] < 0:
        spent += abs(item["amount"])
    spent_amounts.append(round(spent, 2))

# Calculate percentage rounded down to the nearest 10
  total = round(sum(spent_amounts), 2)
  spent_percentage = list(map(lambda amount: int((((amount / total) * 10) // 1) * 10), spent_amounts))

# Create the bar chart substrings
  header = "Percentage spent by category\n"

  chart = ""
  for value in reversed(range(0, 101, 10)):
      chart += str(value).rjust(3) + '|'
      for percent in spent_percentage:
        if percent >= value:
          chart += " o "
        else:
          chart += "   "
      chart += " \n"

  footer = "    " + "-" * ((3 * len(categories)) + 1) + "\n"
  descriptions = list(map(lambda category: category.name, categories))
  max_length = max(map(lambda description: len(description), descriptions))
  descriptions = list(map(lambda description: description.ljust(max_length), descriptions))
  for x in zip(*descriptions):
    footer += "    " + "".join(map(lambda s: s.center(3), x)) + " \n"

  return (header + chart + footer).rstrip("\n")

def validate_input_num(input_description=": "): 
    while True:
        try:
            variable=float(input(str(input_description)))
        except:
            print('===Invalid Input===')
            continue
        if type(variable)==float:
            break
    return variable

def validate_option(message="",max_option=1):
  while True:
    option_=input(message)
    try: 
      if int(option_)<=max_option and int(option_)>0:
        break
    except:
      print("===Input a valid option===")
  return option_

while True:
  print("Chose your options from the menu:")
  option=validate_option("1 for deposit. \n2 for withdraw.\n3 for tranfer.\n4 EXIT.\n: ",4)

  if option=="1":
    option2=validate_option("Select an account to deposit\n1 for account 001.\n2 for account 002.\n3 for account 003.\n: ",3)
    if option2=="1":
      try:
        if account_001.get_balance()>0:
          balance=True
      except:
        account_001 = Category("Account 001")
      amount=validate_input_num("Enter a valid amount: ")
      account_001.deposit(amount, "initial deposit")
      print(f"Current category balance: {account_001.get_balance()}$")
    if option2=="2":
      try:
        if account_002.get_balance()>0:
          balance=True
      except:
        account_002 = Category("Account 002")
      amount=validate_input_num("Enter a valid amount: ")
      account_002.deposit(amount, "initial deposit")
      print(f"Current category balance: {account_002.get_balance()}$")
    if option2=="3":
      try:
        if account_003.get_balance()>0:
          balance=True
      except:
        account_003 = Category("Account 003")
      amount=validate_input_num("Enter a valid amount: ")
      account_003.deposit(amount, "initial deposit")
      print(f"Current category balance: {account_003.get_balance()}$")

  if option=="2":
    option2=validate_option("Select an acount to withdraw \n1 for acount 001.\n2 for acount 002.\n3 for acount 003.\n: ",3)
    if option2=="1":#------------------withdraw for acount 1------------------
      try:
        if account_001.get_balance()>0:
          balance=True
      except:
        account_001 = Category("Account 001")
      option3=validate_option("Select a category\n1 for groceries.\n2 for restaurant \n3 for Clothing \n4 for Auto.\n: ",3)
      if option3=="1":
        amount=validate_input_num("Enter a valid amount: ")
        account_001.withdraw(amount, "groceries")
        print(f"Current category balance: {account_001.get_balance()}$")
      print(f"Current category balance: {account_001.get_balance()}$")
      if option3=="2":
        amount=validate_input_num("Enter a valid amount: ")
        account_001.withdraw(amount, "restaurant and more food for dessert")
        print(f"Current category balance: {account_001.get_balance()}$")
      if option3=="3":
        amount=validate_input_num("Enter a valid amount: ")
        account_001.withdraw(amount)
        print(f"Current category balance: {account_001.get_balance()}$")
      if option3=="4":
        amount=validate_input_num("Enter a valid amount: ")
        account_001.withdraw(amount)
        print(f"Current category balance: {account_001.get_balance()}$")
    if option2=="2":#------------------withdraw for acount 2------------------
      try:
        if account_002.get_balance()>0:
          balance=True
      except:
        account_002 = Category("Account 002")
      option3=validate_input_num("Select a category\n1 for groceries.\n2 for restaurant \n3 for Clothing \n4 for Auto.\n: ")
      if option3=="1":
        amount=validate_input_num("Enter a valid amount: ")
        account_002.withdraw(amount, "groceries")
        print(f"Current category balance: {account_002.get_balance()}$")
      if option3=="2":
        amount=validate_input_num("Enter a valid amount: ")
        account_002.withdraw(amount, "restaurant and more food for dessert")
        print(f"Current category balance: {account_002.get_balance()}$")
      if option3=="3":
        amount=validate_input_num("Enter a valid amount: ")
        account_002.withdraw(amount)
        print(f"Current category balance: {account_002.get_balance()}$")
      if option3=="4":
        amount=validate_input_num("Enter a valid amount: ")
        account_001.withdraw(amount)
        print(f"Current category balance: {account_002.get_balance()}$")
    if option2=="3":#------------------withdraw for acount 3------------------
      try:
        if account_003.get_balance()>0:
          balance=True
      except:
        account_003 = Category("Account 003")
      option3=validate_option("Select a category\n1 for groceries.\n2 for restaurant \n3 for Clothing \n4 for Auto.\n: ",4)
      if option3=="1":
        amount=validate_input_num("Enter a valid amount: ")
        account_003.withdraw(amount, "groceries")
        print(f"Current category balance: {account_003.get_balance()}$")
      if option3=="2":
        amount=validate_input_num("Enter a valid amount: ")
        account_003.withdraw(amount, "restaurant and more food for dessert")
        print(f"Current category balance: {account_003.get_balance()}$")
      if option3=="3":
        amount=validate_input_num("Enter a valid amount: ")
        account_003.withdraw(amount)
        print(f"Current category balance: {account_003.get_balance()}$")
      if option3=="4":
        amount=validate_input_num("Enter a valid amount: ")
        account_003.withdraw(amount)
        print(f"Current category balance: {account_003.get_balance()}$")

  if option=="3":
    
    transfer_from=validate_option("Select an account to transfer from: \n1 for account 001.\n2 for account 002.\n3 for account 003.\n: ",3)   
    transfert_to=validate_option("Select an account to transfer to: \n1 for account 001.\n2 for account 002.\n3 for account 003.\n: ",3)
    
    if transfer_from=="1":
      try:
          if account_001.get_balance()>0:
            balance=True
      except:
        print("===Not enogh founds in this account===")
        break
      if transfert_to=="1":
        print("ERROR: Can't tranfer to the same account")
      if transfert_to=="2":
        try:
          if account_002.get_balance()>0:
            balance=True
        except:
          account_002 = Category("Account 002")
        
        amount=validate_input_num("Enter a valid amount: ")
        account_001.transfer(amount, account_002)
        print(f"Current category balance: {account_002.get_balance()}$")
      if transfert_to=="3":
        try:
          if account_003.get_balance()>0:
            balance=True
        except:
          account_003 = Category("Account 003")
        
        amount=validate_input_num("Enter a valid amount: ")
        account_001.transfer(amount, account_003)
        print(f"Current category balance: {account_003.get_balance()}$")
      
    if transfer_from=="2":
      try:
          if account_002.get_balance()>0:
            balance=True
      except:
        print("===Not enogh founds in this account===")
        break
      if transfert_to=="1":
        try:
          if account_001.get_balance()>0:
            balance=True
        except:
          account_001 = Category("Account 001")
       
        amount=validate_input_num("Enter a valid amount: ")
        account_002.transfer(amount, account_001)
        print(f"Current category balance: {account_001.get_balance()}$")
      if transfert_to=="2":
        print("ERROR: Can't tranfer to the same acount")
      if transfert_to=="3":
        try:
          if account_003.get_balance()>0:
            balance=True
        except:
          account_003 = Category("Account 003")

        amount=validate_input_num("Enter a valid amount: ")
        account_002.transfer(amount, account_003)
        print(f"Current category balance: {account_003.get_balance()}$")

    if transfer_from=="3":
      try:
          if account_003.get_balance()>0:
            balance=True
      except:
        print("===Not enogh founds in this acount===")
        break
      if transfert_to=="1":
        try:
          if account_001.get_balance()>0:
            balance=True
        except:
          account_001 = Category("Account 001")

        amount=validate_input_num("Enter a valid amount: ")
        account_003.transfer(amount, account_001)
        print(f"Current category balance: {account_001.get_balance()}$")
      if transfert_to=="2":
        try:
          if account_002.get_balance()>0:
            balance=True
        except:
          account_002 = Category("Account 002")

        amount=validate_input_num("Enter a valid amount: ")
        account_003.transfer(amount, account_002)
        print(f"Current category balance: {account_002.get_balance()}$")
      if transfert_to=="3":
        print("ERROR: Can't tranfer to the same acount")
      
  if option=="4":
    break

try:
  print(create_spend_chart([account_001, account_002, account_003]))
except:
  print('Not enough data to build a chart.')
