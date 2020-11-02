# -*- coding: utf-8 -*-
"""
Created on Mon Oct 26 21:13:10 2020
Black jack game in Python
@author: Marcin
"""
import random
suites = ["Clubs","Hearts","Diamonds","Spades"]
ranks = ['Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
values = {"Two":2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10,
              "Jack":10, "Queen":10, "King":10, "Ace":11}
min_chips = 100
max_chips = 1000
dealers_treshold = 17

# Card class
class Card:
    def __init__(self,suite,rank):
        self.suite = suite
        self.rank = rank
        self.value = values[rank]
    def __str__(self):
        return self.rank + ' of ' + self.suite
   
class Deck:
    def __init__(self):
        self.all_cards = []
        for suite in suites:
            for rank in ranks:
                self.all_cards.append(Card(suite,rank))
    def shuffle(self):
        random.shuffle(self.all_cards)
    def deal_one(self):
        return self.all_cards.pop()
class Player:
    def __init__(self, name, bankroll):
        self.name = name
        self.bankroll = bankroll
    def __str__(self):
        return self.name + ' has ' + self.bankroll + "$"
def ask_for_bet(max_bet):
    bet = 0
    while bet == 0:
        try:
            bet = int(input(f"Provide the bet amount (available: {max_bet}): "))
        except:
            print("Provide an integer value!")
            bet = 0
        else:
            if bet > max_bet:
                print(f"Provided amount is to high. Value need to be less or equal to {max_bet}")
                bet = 0
            else:
                return bet
def hit_or_stand():
    decision = ''
    while decision == '':
        decistion = input("Hit or stay? (H/S): ")
        if decistion.lower() in ['h','s']:
            return decistion.lower()
        else:
            decistion = ''
def play_again():
    decision = ''
    while decision == '':
        decistion = input("Do you wan to play again? (y/n): ")
        if decistion.lower() in ['y','n']:
            return decistion.lower()
        else:
            decistion = ''    
            
        
            
    
# game logic implementation
username = input("Provide your username: ")
bankroll = 0
while bankroll not in range(min_chips,max_chips+1):
    bankroll = int(input(f"Provide the bankroll (not more than {max_chips}$):"))
player = Player(username, bankroll)
deck = Deck()
deck.shuffle()
      
while True:
    # as for bet
    round_busted = False 
    dealer_cards = []
    player_cards = []
    player_points = 0
    dealer_points = 0
    in_game = 0
    in_game = ask_for_bet(player.bankroll)    # runs unitil provided value is correct
    player.bankroll = player.bankroll - in_game
    in_game = 2*in_game
    # give two cards for player and dealer
    dealer_cards.append(deck.deal_one())
    dealer_cards.append(deck.deal_one())
    player_cards.append(deck.deal_one())
    player_cards.append(deck.deal_one())    
    #show player one of the dealers card
    #add dealers points
    dealer_points += dealer_cards[-1].value
    print(f"Dealers first card is: {dealer_cards.pop()} with {dealer_points} points")
    #show players cards and add points
    for card in player_cards:
        player_points += card.value
    print(f"Yours cards are: {player_cards.pop()} and {player_cards.pop()} with {player_points} points total")
    decision = hit_or_stand()
    while decision == 'h':
        # get a card from the deck
        card = deck.deal_one()
        if card.rank == "Ace" and player_points > 10:
            player_points += 1
          #  print(f"You got {card} with 1 point. Your total points: {player_points}")
        else:
            player_points += card.value
         #   print(f"You got {card} with {card.value} points. Your total points: {player_points}")
        if player_points > 21:
            print("You are busted!!!")
            round_busted = True
            break            
        print(f"You got {card} and your points are {player_points}")
        decision = hit_or_stand()
    
    # computer get card
    while dealer_points < dealers_treshold and not round_busted:
        card = deck.deal_one()
        if card.rank == "Ace" and dealer_points > 10:
            dealer_points += 1
            print(f"Dealer got {card} with {1} point. Total points {dealer_points}")
        else:
            dealer_points += card.value
            print(f"Dealer got {card} with {card.value} points. Total points {dealer_points}")
    if dealer_points > 21:
        print("Dealer got busted!!!")
        round_busted = True
        player.bankroll += in_game
        print(f"Congratulations, you won this round and {in_game} points")
        print(f"Total {player.bankroll} points")
    
    
    if not round_busted:
        # Compare who has more points
        print(f"Your points: {player_points} and Dealer's points {dealer_points}")
        if player_points > dealer_points:
            print(f"Congratulations, you won this round and {in_game} points")
            player.bankroll += in_game
            print(f"Total {player.bankroll} points")
        elif player_points < dealer_points:
            print(f"You lost this round. Your total points: {player.bankroll}")
        else: 
            #tie
            print("It was a tie!")
            player.bankroll += in_game/2
    
    decision = play_again()
    if decision == 'n':
        break
        
    
    
    
    
    
    



