
class MoneyMachine():
  def __init__(self):
    self.profit = 0

  def report(self):
    print(f"Profit: {self.profit}")

  def make_payment(self, drink):
    global user_money
    print("Please insert coins.")
    user_money = float()
    user_money += int(input("How many quarters?: "))*0.25
    user_money += int(input("How many dimes?: "))*0.1
    user_money += int(input("How many nickles?: "))*0.05
    user_money += int(input("How many pennies?: "))*0.01
    
    if user_money == drink.cost:
      self.profit += drink.cost
      return True
    elif user_money > drink.cost:
      self.profit += drink.cost
      change = round(user_money - drink.cost, 2)
      print(f"There is ${change} in change.")
      return True
    else:
      return False

  
  def insert_more(self, drink, user_money):
    more_money = round(drink.cost - user_money, 2)
    while more_money != 0:
      print(f"Please insert more ${more_money}")
      new_add = float()
      new_add += int(input("How many quarters?: "))*0.25
      new_add += int(input("How many dimes?: "))*0.1
      new_add += int(input("How many nickles?: "))*0.05
      new_add += int(input("How many pennies?: "))*0.01
      user_money += new_add

      if user_money == drink.cost:
        self.profit += drink.cost
        return True
      elif user_money > drink.cost:
        self.profit += drink.cost
        change = round(user_money - drink.cost, 2)
        print(f"There is ${change} in change.")
        return True
      else:
        more_money = round(drink.cost - user_money, 2)

