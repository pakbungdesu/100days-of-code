
from pic import logo

print(logo)

# FUNCTION
def add(num1, num2):
  return num1+num2

def subtract(num1, num2):
  return num1-num2

def multiply(num1, num2):
  return num1*num2

def divide(num1, num2):
  return num1/num2

list_operation = {"+": add, "-": subtract, "*": multiply, "/": divide}

con = "y"
first_num = float(input("What's the first number?: "))

while con != "n":
  for key in list_operation:
    print(key)
  input_operation = str(input("Pick one operation from the line above: "))
  second_num = float(input("What's is the next number?: "))

  # OUTPUT
  answer = list_operation[input_operation](first_num, second_num)
  print(f"{first_num} {input_operation} {second_num} = {answer}")

  con = str(input(f"type \"y\" to continue calculating with {answer}, type \"n\" to exit: "))
  if con == "y":
    first_num = answer
  else:
    print("bye bye.")

