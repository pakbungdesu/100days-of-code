
from pic import logo
from replit import clear
import random as rand

def play():
  print(logo)
  # RANDOM
  
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  def rand_appd_remove(a_list, n):
    for n in range(0,n):
      new_card = rand.choice(cards)
      a_list.append(new_card)
      cards.remove(new_card)
  
  player_cards = []
  rand_appd_remove(player_cards, 2)
  
  com_cards = []
  rand_appd_remove(com_cards, 1)
  
  # FIRST OUTPUT
  
  sum_p = sum(player_cards)
  sum_c = sum(com_cards)
  blackjack_p = False
  
  if sum_p == 21:
    print(f"Your card: {player_cards}, current score: {sum_p}")
    print(f"Computer's first card: {com_cards}")
    blackjack_p = True
  else:
    print(f"Your card: {player_cards}, current score: {sum_p}")
    print(f"Computer's first card: {com_cards}")
  
  # PLAYER LOOP

  while input("Type 'y' to get another card, type 'n' to pass: ") != "n" and sum_p < 21 and blackjack_p != True:
    rand_appd_remove(player_cards, 1)
    sum_p = sum(player_cards)
    
    if sum_p > 21:
      if 11 in player_cards:
        player_cards.remove(11)
        player_cards.append(1)
        sum_p = sum(player_cards)
        print(f"Your card: {player_cards}, current score: {sum_p}")
      else:
        print(f"Your card: {player_cards}, current score: {sum_p}")
    elif sum_p == 21:
      blackjack_p = True
    else:
      print(f"Your card: {player_cards}, current score: {sum_p}")
      
  print(f"Your final hand: {player_cards}, final score: {sum_p}")
    
    # COMPUTER LOOP
    # not stop picking unless sum_c > 17

  blackjack_c = False
  while sum_c < 17 and blackjack_c != True and blackjack_p != True:
    rand_appd_remove(com_cards, 1)
    sum_c = sum(com_cards)

    if sum_c == 21:
      blackjack_c = True  
  print(f"Computer's final hand: {com_cards}, final score: {sum_c}")
  
  # COMPARE
  
  def compare(sum_ofp, sum_ofc):
    if sum_ofp > sum_ofc:
      print("You win 😃")
    elif sum_ofp < sum_ofc:
      print("You lose 😤")
    else:
      print("Draw 🙃")
  
  # FINAL OUTPUT

  if blackjack_p == True:
    print("You win with a Blackjack 😎")
  elif blackjack_c == True:
    print("Opponent got a Blackjack. You lose 😱")
  elif sum_p > 21:
    if sum_c > 21:
      print("You lose 😤")
    else:
      print("You went over. You lose 😭")
  elif sum_p < 21:
    if sum_c > 21:
      print("Opponent went over. You win 😁")
    else:
      compare(sum_p, sum_c)
  else:
    pass

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
  clear()
  play()
  
print("bye bye")

