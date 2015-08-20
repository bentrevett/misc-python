from random import choice
import time

def hit_or_stick():
    while sum(your_cards)<22:
        response = input("Would you like to hit or stick? ")
        if response.lower() == "hit":
            your_cards.append(choice(cards))
            print("Drawing...")
            time.sleep(0.5)
            print("Your hand {}. Total: {}".format(your_cards,sum(your_cards)))
            if sum(your_cards)>21:
                if 11 in your_cards:
                    your_cards.pop(your_cards.index(11))
                    your_cards.append(1)
                    print("Swapped 11 for 1, your hand {}. Total: {}".format(your_cards,sum(your_cards)))
                if sum(your_cards)>21:
                    print("You bust!")
                    break
        elif response.lower() =="stick":
            break
        else:
            print("Please type hit or stick!")
    
            
def dealer_draw():
    while sum(dealer_cards)<sum(your_cards) and sum(dealer_cards)<21:
            dealer_cards.append(choice(cards))
            print("Drawing...")
            time.sleep(0.5)
            print("Dealer hand {}. Total: {}".format(dealer_cards,sum(dealer_cards)))
            if sum(dealer_cards)>21:
                if 11 in dealer_cards:
                    dealer_cards.pop(dealer_cards.index(11))
                    dealer_cards.append(1)
                    print("Swapped 11 for 1, dealer hand {}. Total: {}".format(dealer_cards,sum(dealer_cards)))
                if sum(dealer_cards)>21:
                    print("Dealer bust! You win!")
    if sum(dealer_cards)>=sum(your_cards) and sum(dealer_cards)<=21:
        print("Dealer wins!")
        
money = 100
cards = [2,3,4,5,6,7,8,9,10,10,10,10,11]
your_cards = []
dealer_cards = []

while money>0:
    print("You have ${}".format(money))
    while True:
        bet = int(input("How much would you like to bet? "))
        if bet>money:
            print("Cannot bet more money than you have!")
        else:
            money = money - bet
            break
    print("You have ${} remaining".format(money))
    your_cards.append(choice(cards))
    your_cards.append(choice(cards))
    print("Your hand {}. Total: {}".format(your_cards,sum(your_cards)))
    hit_or_stick()
    if sum(your_cards)<=21:
        dealer_draw()
    if sum(your_cards)<=21 and sum(dealer_cards)>21:
        money = money+(bet*2)
    your_cards = []
    dealer_cards = []
    
print("Out of money! Game over!")
