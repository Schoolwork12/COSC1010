#Name Tony Dyer
#Date
#Final for COSC1010
#Doing a coding project rather than a 100 question test

#importing the random lib
import random

#importing the os lib since I want to clear the screen when I want instead of having a long scrolling game
import os

#importing the time function so that you can actually see the silly dialog I put!
import time

# import the ascii art file for the cards/splash screen
from card_art import card_ascii , splash

def clear_sc():  #this is the time and clear screen function so that the game stays pretty
    time.sleep(3.5)
    os.system('cls' if os.name == 'nt' else 'clear')

def create_deck(): # create the deck and shuffle it 
    values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    deck = [value for value in values for _ in range(4)]
    random.shuffle(deck)
    return deck

def deal_initial_cards(deck):  #dealing the cards aka choosing the cards for both dealer and player and getting rid of them from the current cards
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    return player_hand, dealer_hand

def calculate_hand_value(hand):  # calculating the hand value for the letter cards
    value = 0
    aces = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
            value += 10
        elif card == 'A': #value of the ace
            aces += 1
            value += 11
        else:
            value += int(card)

    while value > 21 and aces: # if the value of the player cards is greater than 21 then it replaces the value with a 1
        value -= 10
        aces -= 1

    return value

def display_hand(hand, owner="Player", hidden=False):  # displays the cards, dealers one card is hidden
    lines = [""] * 6  # each card has 6 lines of ASCII art

    if hidden:
        first_card = card_ascii['back'].splitlines()
        second_card = card_ascii[hand[1]].splitlines()
        for i in range(5):
            lines[i] = first_card[i] + " " + second_card[i]
        print(f"{owner}'s hand:")
    else:
        card_lines = [card_ascii[card].splitlines() for card in hand]
        for i in range(5):
            lines[i] = " ".join(card[i] for card in card_lines)
        print(f"{owner}'s hand (value: {calculate_hand_value(hand)}):")

    print("\n".join(lines))


def player_turn(deck, player_hand, money, bet): # displays the cards and asks the user what they want to do for their turn
    while True:
        
        display_hand(player_hand, owner="Player")
        options = "[H]it, [S]tand, [D]ouble Down" if len(player_hand) == 2 and money >= bet else "[H]it, [S]tand" # if you dont have the money for it
        print("Options:", options)                                                                              #you wont be able to double down
        choice = input("What will you do? ").lower()

        if choice == 'h':
            player_hand.append(deck.pop())
            if calculate_hand_value(player_hand) > 21: # if your hands value is over 21 then you bust
                print("Busted!")
                break
        elif choice == 'd' and len(player_hand) == 2 and money >= bet:
            player_hand.append(deck.pop())
            bet *= 2
            money -= bet // 2
            break
        elif choice == 's':
            break
        else:
            print("Dealer: You high or just bad at this? Pick a valid option.") # just in case the player wants to be goofy
            clear_sc()

    return player_hand, bet, money

def dealer_turn(deck, dealer_hand): # dealers turn if the dealer has less than 17 then he will draw again
    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())
    return dealer_hand

def evaluate_game(player_hand, dealer_hand, bet, money): # will calc the hands and check who won the hand
    clear_sc()
    print(splash)

    display_hand(dealer_hand, owner="Dealer")
    display_hand(player_hand, owner="Player")

    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if player_value > 21:
        print("Dealer: Told you you'd lose.")
    elif dealer_value > 21 or player_value > dealer_value:
        print("Dealer: Ugh, fine. You win this one...")
        money += bet * 2
    elif player_value == dealer_value:
        print("Dealer: A tie? Lucky punk. Here's your money back.")
        money += bet
    else:
        print("Dealer: Ha! Pay up!")

    clear_sc()
    return money

def place_bet(money):  #place bet function, just gets the amount of money you currently have in the main function and then asks how much you want to use then
    while True:        # minus's it from your total you specified before when asked how much money you have
        try:           # then lets you play with the money from that 
            print(splash)
            print(f"\n You currently have ${money}.")
            bet = int(input("Dealer: How much would you like to lose this hand?  $"))
            if bet > money:
                print("Dealer: You trying to scam me? You don't even *have* that much.")
                clear_sc()
            elif bet <= 0:
                print("Dealer: You can't bet nothing loser, this is a game of risk. Try again.")
                clear_sc()
            elif bet == money:
                print("Dealer: All in!? I can't wait to see you pan-handling on my way into work...")
                clear_sc()
                return bet, 0
            else:
                money -= bet
                print(f"Dealer: So you're betting ${bet}. Bold move, but it'll be mine soon. Your new balance is ${money}.")
                clear_sc()
                return bet, money
        except ValueError: # just incase the player gets cheeky
            print("Dealer: Numbers only moron!")
            clear_sc()

def main_pro(): # main function
    while True:
        try:
            print(splash)
            money = int(input("How much money would you like to gamble with? $"))
            break
        except ValueError: # incase the player decides to get cheeky
            print("Dealer: That's not even a number... come back when you know how money works.")
            clear_sc()

    if money <= 1000:
        print("Dealer: I don't think someone as poor as you should be gambling, wouldn't you be better off getting food?")
        clear_sc()
    elif money >= 20000:
        print(f"Dealer: Ahh High-Roller, don't worry, I'll clean you out! That ${money} will be mine soon, I hope you don't feel attached to it...")
        clear_sc()
    else:
        print(f"Dealer: Alright, you're starting with ${money}. Let's see how lucky you are...")
        clear_sc()

    while money > 0:
        bet, money = place_bet(money)
        deck = create_deck()
        player_hand, dealer_hand = deal_initial_cards(deck)

        display_hand(dealer_hand, owner="Dealer", hidden=True)
        player_hand, bet, money = player_turn(deck, player_hand, money, bet)
        if calculate_hand_value(player_hand) <= 21:
            dealer_hand = dealer_turn(deck, dealer_hand)
        money = evaluate_game(player_hand, dealer_hand, bet, money)

        if money == 0: # if you completely lose all your money it quits the game
            print(splash)
            print("Dealer: You're outta cash! I cant wait to see you pan-handling outside.")
            clear_sc()
            break
        else:
            print(splash) # if you still have money it'll ask if you want to play another
            cont = input("Would you like to play another hand? (y/n): ").lower()
            clear_sc()
            if cont != 'y': #if you want to quit playing after a hand 
                print(splash)
                print("Dealer: Alright, scram while you're ahead.")
                clear_sc()
                break

main_pro()