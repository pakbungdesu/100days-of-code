
from pic import logo
import random as rand

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# CHOOSE LEVEL
level = str(input("Choose a difficulty. Type 'easy' or 'hard': "))
if level == "easy":
  turns = 10
else:
  turns = 5

# RANDOM NUMBER
a_num = rand.randint(1,100)

# CHECK THE GUESS
x = int()
def check_guess(a_guess):
  global x
  global turns
  if a_guess == a_num:
    x = 1
    turns = turns
  elif a_guess > a_num:
    x = 2
    turns -= 1
  else:
    x = 3
    turns -= 1

# LOOP
while turns > 0 and x != 1:
  
  print(f"You have {turns} attempts remaining to guess the number.")
  make_guess = int(input("Make a guess: "))
  
  while make_guess not in range(0,101):
    turns -= 1
    print("You are out of range between 1 and 100")
    print(f"You have {turns} attempts remaining to guess the number.")
    make_guess = int(input("Make a guess again: "))
  
  
  check_guess(make_guess)
  if x == 1:
    print(f"You got it! The answer was {a_num}.")
  elif x == 2:
    print("Too high.\nGuess again.")
  else:
    print("Too low.\nGuess again.")

if turns == 0:
  print(f"Pssst, the correct answer is {a_num}")
  print("You've run out of guesses, you lose.")

