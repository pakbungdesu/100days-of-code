
from coffee_maker import *
from menu import *
from money_mac import *
from pic import *

print(logo)
print(text)

menu = Menu()
coffee_maker = CoffeeMaker()
money_mac = MoneyMachine()

want = input(f"What would you like? (espresso/latte/cappuccino): ")

while True:
  if want == "off":
    break
  elif want == "report":
    money_mac.report()
    coffee_maker.report()
  else:
    drink = menu.find_drink(want)
    sufficient = coffee_maker.resources_sufficient(drink)    
    if sufficient == True:
      user_money = 0
      payment = money_mac.make_payment(drink)
      if payment == True:
        coffee_maker.make_coffee(drink)
      else:
        pay_again = money_mac.insert_more(drink, user_money)
        if pay_again == True:
          coffee_maker.make_coffee(drink)

  want = input(f"What would you like? (espresso/latte/cappuccino): ")

