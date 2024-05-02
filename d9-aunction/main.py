
from pic import logo
from replit import clear

print(logo)

other = "yes"
info = []
bid_money = []

while other != "no":

  input_name = input("What is your name?: ")
  input_bid = input("What is your bit?: $")

  # NEW PERSON
  def addinfo(func_name, func_bid):
    new_person = dict(name = func_name, bid = func_bid)
    info.append(new_person)  

  addinfo(input_name, input_bid)

  # END OR NOT
  other = str(input("Are there any other bidders? Type 'yes or 'no'.\n"))
  clear()

# COMPARE
for person in info:
  for key in person:
    if key == "bid":
      bid_money.append(person["bid"])
    else:
      pass

max = bid_money[0]
for money in bid_money:
  if money > max:
    max = money
  else:
    max = max

# MAX PERSON
index = bid_money.index(max)
person = info[index]
name_final = person["name"]
bid_final = person["bid"]

# OUTPUT FINAL
print(logo)
print(f"The winner is {name_final} with a bid of ${bid_final}")

