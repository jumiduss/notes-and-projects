from resources import card_deck,logo
import random
 
def deal_card():
    """Returns the key of the chosen card in card_deck""" 
    global card_deck
    return random.choice(list(card_deck.keys()))

def deal_start_hand():
    """Deals the start of the hand for the player and computer"""
    return [deal_card(),deal_card()],[deal_card(),deal_card()]

def add_aces(num_aces,hand_value):
    if hand_value <=10:
        hand_value += 11
        num_aces -= 1
        if num_aces != 0:
            add_aces(num_aces, (hand_value - 10))
    else:
        hand_value += num_aces
    return hand_value
    
def count_hand(hand):
    num_aces = 0
    hand_value = 0
    for card in hand:
        if card == "A":
            num_aces += 1
        else:
            hand_value += card_deck[card]
    if num_aces >= 1:
        hand_value = add_aces(num_aces,hand_value)
    return hand_value

def hand_string(hand):
    return ", ".join(hand)


def dealer_play(dealer_hand):
    playing = True
    while playing:
        dealer_hand_worth = count_hand(dealer_hand)
        print("The Dealer's Hand: {}\nWorth :{}".format(hand_string(dealer_hand),dealer_hand_worth))
        if dealer_hand_worth <= 16:
            print("The Dealer Wants Another Card!")
            dealer_hand.append(deal_card())
        elif dealer_hand_worth > 16 and dealer_hand_worth <= 21:
            print("The Dealer wants to stay.")
            playing = False
        elif dealer_hand_worth > 21:
            print("The dealer has busted!")
            return (dealer_hand,True)
    return dealer_hand_worth,False
    
def game(deal_hand,play_hand):
    play_busted = deal_busted = False
    playing = True
    deal_hand_value = 0
    play_hand_value = 0
    
    while playing:
        want_card = input("Would you like another card? (y/n)\n")
        if want_card == 'y':
            play_hand.append(deal_card())
            play_hand_value = count_hand(play_hand)
            print("Current Hand: {}\nOf Value: {}\n".format(hand_string(play_hand),play_hand_value))
            if play_hand_value > 21:
                print("You've Busted!")
                play_busted = True
                playing = False
        else:
            input("Press Enter to See the Dealers Turn.")
            deal_hand_value,deal_busted = dealer_play(deal_hand)
            playing = False     
    if play_busted:
        print("Dealer Wins")  
    elif deal_busted:
        print("Player Wins")
    else:
        if deal_hand_value >= play_hand_value:
            print("Dealer Wins")
        else:
            print("Player Wins")
    play_another = input("Play again?")
    if play_another in ['y','']:
        game_start()
    print(logo)
    print("Thanks for playing!")
    

def game_start():
    print(logo)
    print("Welcome to Black Jack!")
    input("Press enter to start")
    deal_hand,play_hand=deal_start_hand()
    deal_hand_hidden = ["#",deal_hand[1]]
    print("The dealer's starting hand is:\n{}".format(hand_string(deal_hand_hidden)))
    print("Your starting hand is:\n{} (worth {})\n\n".format(hand_string(play_hand),str(count_hand(play_hand))))
    game(deal_hand,play_hand)
    
game_start()