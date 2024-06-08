
from words import *
from pic import *
import random

print(logo)
print("\nNote: You can guess in one time for one letter with many positions")

# random word
chosen_word = random.choice(word_list)

# random letter
letters = [letter for letter in chosen_word]
rand_letters = random.choices(letters, k = round(0.25*len(letters)))
letters_index = [index for (index, item) in enumerate(letters) if item in rand_letters]

# display
display = ["_" for x in letters]
for i in range(len(letters)):
  if i in letters_index:
    display[i] = letters[i]

# function
def check_guess():
  if guess in letters:
    if guess in display:
      return 1 # already guessed
    else:
      guess_index = [index for (index, item) in enumerate(letters) if item == guess]
      if len(guess_index) == 1:
        letters_index.append(guess_index[0])
      elif len(guess_index) > 1:
        letters_index.extend(guess_index)
      return 2 # new guess
  else:
      return 3 # wrong guess

def new_display():
  for i in range(len(letters)):
    if i in letters_index:
      display[i] = letters[i]

# declare
lives = 6
gameover = False
guess = str()

# loop
while gameover == False:
  new_display()
  print(" ".join(display))

  # check input
  guess = input("Guess a letter: ").lower()
  check_guess()

  # output
  if check_guess() == 1:
    print(f"There is {guess} already!\n")
    lives -= 1
    print(stages[lives])
  elif check_guess() == 2:
    print(f"You guessed {guess}, That's correct.\n")
  else:
    print(f"You guessed {guess}, that's not in the word. You lose a life.\n")
    lives -= 1
    print(stages[lives])

  new_display()

  # complete
  if lives != 0:
    if display == letters:
      print(" ".join(display))
      print("COMPLETED. YOU WIN!")
      gameover = True
  else:
    print(f"GAME OVER\nThe word is {chosen_word}")
    gameover = True
