from art import logo
print(logo)

import random

player_score = 0
computer_score = 0
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

computer_card = []
player_card = []

player_card.append(cards[random.randint(0, 12)])
player_card.append(cards[random.randint(0, 12)])

for card in player_card:
    player_score += card 

computer_card.append(cards[random.randint(0, 12)])
computer_score += computer_card[0]

def card_for_computer(computer_card, player_score):
    global computer_score
    computer_score = 0 
    random_card = cards[random.randint(0, 12)]  
    if random_card == 11 and computer_score > 10:
        computer_card.append(1)
        computer_score += 1
    else:
        computer_card.append(random_card)
    for card in computer_card:
        computer_score += card
    while computer_score < 17:
        random_card = cards[random.randint(0, 12)]  
        if random_card == 11 and computer_score > 10:
            computer_card.append(1)
            computer_score += 1
        else:
            computer_card.append(random_card)
            computer_score += random_card
    print_result()

def print_current_score():
    print(f"Your cards: {player_card}, current score: {player_score}")
    print(f"Computer's first card: {computer_card[0]}")

def print_result():
    global player_score
    global computer_score
    if player_score > 21:
        print("You Lost! Computer Won!")
    elif computer_score > 21:
        print("You Won! Computer Lost!")
    elif player_score > computer_score:
        print("You Won! Computer Lost!")
    elif player_score == computer_score:
        print("It's a tie!")
    else:
        print("You Lost! Computer Won!")
    print(f"Your final hand: {player_card}, Final score: {player_score}")
    print(f"Computer's final hand: {computer_card}, Final score: {computer_score}")

print_current_score()

continue_deal = True
while continue_deal:
    want_card = input("Type 'y' to get another card, type 'n' to pass:")
    if want_card == "y":
        random_card = cards[random.randint(0, 12)]
        if random_card == 11 and player_score > 10:
            player_card.append(1)
            player_score += 1
            print_current_score()
        else:
            player_card.append(random_card)
            player_score += random_card
            print_current_score()
        if player_score > 21:
            random_card = cards[random.randint(0, 12)]  
            if random_card == 11 and computer_score > 10:
                computer_card.append(1)
                computer_score += 1
            else:
                computer_card.append(random_card)
                computer_score += random_card
            print_result()
            continue_deal = False
    elif want_card == "n":
        continue_deal = False
        card_for_computer(computer_card, player_score)