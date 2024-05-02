

from words import word_list
from pic import stages, logo
import random

print(logo)
print("\nNote: Even if one letter has many positions, you can guess in one time")
# RANDOM WORD
chosen_word = random.choice(word_list)

# RANDOM LETTERS
letters = []
for letter in chosen_word:
  letters.append(letter)

rand_letters = random.choices(letters, k = round(0.25*len(letters)))
letters_index = [index for (index, item) in enumerate(letters) if item in rand_letters]

# DISPLAY
display = ["_" for x in letters]
for i in range(len(letters)):
  if i in letters_index:
    display[i] = letters[i]

# VARIABLE ANNOUNCEMENT
lives = 6
gameover = False
guess = str()

# FUNCTION
def check_guess():
  if guess in letters:
    if guess in display:
      return 1 # ALREADY GUESSED
    else:
      guess_index = [index for (index, item) in enumerate(letters) if item == guess]
      if len(guess_index) == 1:
        letters_index.append(guess_index[0])
      elif len(guess_index) > 1:
        letters_index.extend(guess_index)
      return 2 # NEW GUESS
  else:
    return 3 # WRONG GUESS

def new_display():
  for i in range(len(letters)):
    if i in letters_index:
      display[i] = letters[i]

# LOOP
while gameover == False:
  new_display()
  print(" ".join(display))

  # INPUT GUESS AND CHECK
  guess = input("Guess a letter: ").lower()
  check_guess()

  # OUTPUT
  if check_guess() == 1:
    print(f"You have guessed {guess} already!")
    lives -= 1
    print(stages[lives])
  elif check_guess() == 2:
    print(f"You guessed {guess}, That's correct.\n")
  else:
    print(f"You guessed {guess}, that's not in the word. You lose a life.")
    lives -= 1
    print(stages[lives])

  new_display()

  # BEFORE NEW ROUND OR NOT
  if lives != 0:
    if display == letters:
      print(" ".join(display))
      print("COMPLETED. YOU WIN!")
      gameover = True
    else:
      pass
  else:
    print(f"GAME OVER\nThe word is {chosen_word}")
    gameover = True


