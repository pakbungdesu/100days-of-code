
from Blackjack import *
from pic import logo

def compare(final_p, final_b):
  if final_p == 21:
    print("You win with a Blackjack 😎")
  elif final_b == 21:
    print("Opponent got a Blackjack. You lose 😱")
  elif final_p < 21 and final_b < 21:
    if final_p > final_b:
      print("You win 😁")
    elif final_p == final_b:
      print("It is a push 🥊")
    else:
      print("You lose 😭")
  elif final_p < 21:
    print("Opponent went over. You win 😁")
  else:
    print("You went over. You lose 😭")

print(logo)
go_on = input("Do you want to play Blackjack? Type 'y' or 'n': ")

while go_on == "y":
  mycard = AllCards()
  player = Blackjack(mycard)
  bot = Blackjack(mycard)

  # First random
  player.draw()
  player.draw()
  bot.draw()
  print(f"Your card: {player.curr}, current score: {sum(player.curr)}")
  print(f"Computer's first card: {bot.curr}")

  while True:
    # Ask player to draw more or not
    draw_or_not = input("Type 'y' to get another card, type 'n' to pass: ")
    if draw_or_not == "y":
      player.draw()
      if player.check21():
        break
      player.check11()
      print(f"Your card: {player.curr}, current score: {sum(player.curr)}")
    else:
      break

  print(f"Your final hand: {player.curr}, final score: {sum(player.curr)}")

  while sum(bot.curr) < 17:  # Bot draw repeatly if sum < 17
    bot.draw()
    if bot.check21():
      break
    bot.check11()
    print(f"Bot's hand: {bot.curr}, current score: {sum(bot.curr)}")

  print(f"Bot's final hand: {bot.curr}, final score: {sum(bot.curr)}")
  compare(sum(player.curr), sum(bot.curr))

  go_on = input("\nDo you want to go over again? Type 'y' or 'n': ")
