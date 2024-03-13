########## Blackjack Card Game ##########
#<<<<<< Our House Rules >>>>>>#
# 1. The deck is unlimited in size
# 2. There are no Jokers
# 3. The Jack/Queen/King all count as 10
# 4. The Ace can count as 11 or 1
# 5. The cards have equal probability of being drawn
# 6. cards are not removed from the deck as they are drawn

# import the random and os module
import random
import os

# creat a function to return a random card from the deck
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

# create a fuction to calculate the score 
def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        # 0 represents the blackjack
        return 0

    # if the score is over 21, then replace the 11 (ACE card) with 1
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# create a function to compare user's score and computer's score
# whoever's score is over 21, then they lose
# its a draw if both have same score
# otherwise, player with highest score wins
def compare(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over, You Lose!"
    
    if user_score == computer_score == 0:
        return "It's a Draw!"
    elif user_score == 0:
        return "Win with a Blackjack!"
    elif user_score > 21:
        return "You went over, You Lose!"
    elif computer_score > 21:
        return "Opponent went over, You Win!"
    elif user_score > computer_score:
        return "You Win!"
    else:
        return "You Lose!"

# create playing function
def play_game():
    # deal the user and computer 2 cards each
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

        # calculate and repeat till the game ends
        while not is_game_over:
            user_score = calculate_score(user_cards)
            computer_score = calculate_score(computer_cards)
            print(f"Your cards: {user_cards}, Current Score: {user_score}")
            print(f"Computer's first card: {computer_cards[0]}")

            if user_score ==0 or computer_score == 0 or user_score > 21:
                is_game_over = True
            else:
                user_should_deal = input("Type 'y' to get another card, Type 'n' to pass: ")

                if user_should_deal == "y":
                    user_cards.append(deal_card())
                else:
                    is_game_over = True

    # computer should keep drawing cards as long as its score is less than 17
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your Final Hand: {user_cards}, Final Score: {user_score}")
    print(f"Computer's Final Hand: {computer_cards}, Final Score: {computer_score}")

    print(compare(user_score, computer_score))

# function to clear the screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# to restart the game
while input("Do you want to play a game of Blackjack> Type 'y' or 'n': ") == 'y':
    clear()
    play_game()