
from data import *
from pic import *

print(logo)
print(text)

def check_coins(coins, user_want):
  global more
  if coins == MENU[user_want]["cost"]:
    print(f"Here is your {user_want} ☕\nNo change. Have a nice day!")
  elif coins > MENU[user_want]["cost"]:
    change = round(coins - MENU[user_want]["cost"], 2)
    print(f"Here is your {user_want} ☕\nThere are ${change} in change.\nEnjoy!")
  else:
    more = round(MENU[user_want]["cost"] - coins, 2)

def insert_more(coins, user_want, more_money):
  if more_money != 0:
    while more_money != 0:
      print(f"Please insert more ${more_money}")
      new_add = float()
      new_add += int(input("How many quarters?: "))*0.25
      new_add += int(input("How many dimes?: "))*0.1
      new_add += int(input("How many nickles?: "))*0.05
      new_add += int(input("How many pennies?: "))*0.01
      coins += new_add
      
      if coins == MENU[user_want]["cost"]:
        print(f"Here is your {user_want} ☕\nNo change. Have a nice day!")
        break
      elif coins > MENU[user_want]["cost"]:
        change = round(coins - MENU[user_want]["cost"], 2)
        print(f"Here is your {user_want} ☕\nThere are ${change} in change.\nEnjoy!")
        break
      else:
        more_money = round(MENU[user_want]["cost"] - coins, 2)


def check_enough(user_want):
  dict_ingre = MENU[user_want]["ingredients"]
  check_list = list()
  
  for ingre in dict_ingre:
    for item in resources:
      if ingre == item:
        check_list.append(resources[item] >= dict_ingre[ingre])

  element = check_list[0]
  same = True
  for member in check_list:
    if element != member:
        same = False
        break

  if same == True:
    return 1
  else:
    return 0

def update_data(user_want):
  dict_ingre = MENU[user_want]["ingredients"]
  for ingre in dict_ingre:
    if ingre == "water":
      resources["water"] = resources["water"] - dict_ingre[ingre]
    elif ingre == "milk":
      resources["milk"] = resources["milk"] - dict_ingre[ingre]
    else:
      resources["coffee"] = resources["coffee"] - dict_ingre[ingre]
  global profit
  profit += MENU[user_want]["cost"]
      

want = input("What would you like? (espresso/latte/cappuccino): ")

while want != "":
  if want == "report":
    for key in resources:
      print(f"{key}: {resources[key]}")
  elif want == "off":
    break
  else:
    check_enough(want)
    if check_enough(want) == 0:
      print("Sorry. There are not enough ingredients.")
    else:
      print("Please insert coins.")
      user_money = float()
      user_money += int(input("How many quarters?: "))*0.25
      user_money += int(input("How many dimes?: "))*0.1
      user_money += int(input("How many nickles?: "))*0.05
      user_money += int(input("How many pennies?: "))*0.01

      more = 0
      check_coins(user_money, want)
      insert_more(user_money, want, more)
      update_data(want)
  
  want = input("What would you like? (espresso/latte/cappuccino): ")

print(f"Profit: ${profit}\nRemaining resources")
for key in resources:
  print(f"{key}: {resources[key]}")
print("Bye Bye.")

