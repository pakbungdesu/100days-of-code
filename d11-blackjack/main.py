from pic import logo
import random as rand
import os
clear = lambda: os.system('cls')

# Compare function
def compare(final_p, final_c):
    if final_p <= 21 and final_c <= 21:
        if final_p > final_c:
            print("You win 😁")
        elif final_p == final_c:
            print("It is a push 🥊")
        else:
            print("You lose 😭")
    elif final_p <= 21:
        print("Opponent went over. You win 😁")
    else:
        print("You went over. You lose 😭")

# Play function
def play():
    # Random, Append and Remove function
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    def rand_appd_remove(a_list, n):
        for n in range(0, n):
            new_card = rand.choice(cards)
            a_list.append(new_card)
            cards.remove(new_card)

    player_cards = []
    rand_appd_remove(player_cards, 2)

    com_cards = []
    rand_appd_remove(com_cards, 1)

    # First output
    sum_p = sum(player_cards)
    sum_c = sum(com_cards)
    print(f"Your card: {player_cards}, current score: {sum_p}")
    print(f"Computer's first card: {com_cards}")

    if sum_p == 21:
        return 1

    # Player Loop
    con_play = str(input("Type 'y' to get another card, type 'n' to pass: "))
    while con_play == "y" and sum_p < 21:
        rand_appd_remove(player_cards, 1)
        sum_p = sum(player_cards)

        if sum_p > 21:
            if 11 in player_cards:
                player_cards.remove(11)
                player_cards.append(1)
                sum_p = sum(player_cards)
        elif sum_p == 21:
            print(f"Your final hand: {player_cards}, final score: {sum_p}")
            return 1

        print(f"Your card: {player_cards}, current score: {sum_p}")
        con_play = str(input("Type 'y' to get another card, type 'n' to pass: "))

    print(f"Your final hand: {player_cards}, final score: {sum_p}")

    # Computer loop
    # Not stop picking unless sum_c > 17
    while sum_c < 17:
        rand_appd_remove(com_cards, 1)
        sum_c = sum(com_cards)

        if sum_c == 21:
            print(f"Computer's final hand: {com_cards}, final score: {sum_c}")
            return 2

    print(f"Computer's final hand: {com_cards}, final score: {sum_c}")
    return [sum_p, sum_c]

print(logo)
go_on = str(input("Do you want to play Blackjack? Type 'y' or 'n': ")).lower()

while go_on == "y":
    clear()
    res = play()
    if res == 1:
        print("You win with a Blackjack 😎")
    elif res == 2:
        print("Opponent got a Blackjack. You lose 😱")
    else:
        compare(res[0], res[1])
    print("")
    go_on = str(input("Do you want to go over again? Type 'y' or 'n': ")).lower()
  
