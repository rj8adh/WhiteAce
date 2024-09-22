from random import shuffle
import tkinter as tk
from tkinter import *
import json
from time import sleep
import os

window = tk.Tk()
window.geometry('520x520')
window.title("Welcome to White Ace")
window.config(bg="seagreen")
window.attributes('-fullscreen', True)

card_types = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
symbols = ['♠', '♥', '♦', '♣']
deck = []
card = []
plyr_index = 0
dealer_index = 1
result = ''
game_won = False
game_tied = False
player_score = 0
dealer_score = 0
powerup_used = False

with open('money.json') as m:
  money = int(m.read())
with open('powerups.json') as p:
  powerups = json.load(p)
with open('bet.json') as b:
  bet = int(b.read())
m.close()
p.close()
b.close()

lbl_plyr_cards = tk.LabelFrame(window,text='The Player\'s Cards', height=300, width=700)
lbl_plyr_points = tk.Label(text='You have 0 points')

lbl_powerups = tk.LabelFrame(window,text='Powerups:', height=100, width=150)
btn_reveal = tk.Button(lbl_powerups, text='Reveal Dealer\'s Card: ' + str(powerups['revealdeal']), state=tk.DISABLED if powerups['revealdeal'] == 0 else tk.NORMAL)
btn_add_plyr = tk.Button(lbl_powerups, text='Add 2 to Player: ' + str(powerups['player2']), state=tk.DISABLED if powerups['player2'] == 0 else tk.NORMAL)
btn_add_dealer2 = tk.Button(lbl_powerups, text='Add 2 to Dealer: ' + str(powerups['dealer2']), state=tk.DISABLED if powerups['dealer2'] == 0 else tk.NORMAL)
btn_add_dealer4 = tk.Button(lbl_powerups, text='Add 4 to Dealer: ' + str(powerups['dealer4']), state=tk.DISABLED if powerups['dealer4'] == 0 else tk.NORMAL)

btn_hit = tk.Button(text='Hit')
btn_stand = tk.Button(text='Stand')
lbl_result = tk.Label(text='Result: ', fg='blue2')

lbl_dealer_cards = tk.LabelFrame(window,text='The Dealer\'s Cards', height=300, width=700)

lbl_plyr_card1 = tk.Label(lbl_plyr_cards, text='Card 1', height=20, width=20)
lbl_plyr_card2 = tk.Label(lbl_plyr_cards, text='Card 2', height=20, width=20)
lbl_plyr_card3 = tk.Label(lbl_plyr_cards, text='Card 3', height=20, width=20)
lbl_plyr_card4 = tk.Label(lbl_plyr_cards, text='Card 4', height=20, width=20)
lbl_plyr_card5 = tk.Label(lbl_plyr_cards, text='Card 5', height=20, width=20)


lbl_deal_card1 = tk.Label(lbl_dealer_cards, text='Hidden', height=20, width=20)
lbl_deal_card2 = tk.Label(lbl_dealer_cards, text='Card 2', height=20, width=20)
lbl_deal_card3 = tk.Label(lbl_dealer_cards, text='Card 3', height=20, width=20)
lbl_deal_card4 = tk.Label(lbl_dealer_cards, text='Card 4', height=20, width=20)
lbl_deal_card5 = tk.Label(lbl_dealer_cards, text='Card 5', height=20, width=20)


lbl_plyr_cards.pack(padx=10)
lbl_plyr_points.pack(padx=10)
lbl_powerups.pack(padx=10, pady=10)
btn_reveal.pack()
btn_add_plyr.pack()
btn_add_dealer2.pack()
btn_add_dealer4.pack()
btn_add_dealer2.pack()
btn_add_dealer2.pack()
btn_stand.pack()
btn_hit.pack()
lbl_result.pack()
lbl_dealer_cards.pack(padx=10)

lbl_plyr_card1.pack(side=LEFT)
lbl_plyr_card2.pack(side=LEFT)
lbl_plyr_card3.pack(side=LEFT)
lbl_plyr_card4.pack(side=LEFT)
lbl_plyr_card5.pack(side=LEFT)

lbl_deal_card1.pack(side=LEFT)
lbl_deal_card2.pack(side=LEFT)
lbl_deal_card3.pack(side=LEFT)
lbl_deal_card4.pack(side=LEFT)
lbl_deal_card5.pack(side=LEFT)

plyr_card_lbls = [lbl_plyr_card1, lbl_plyr_card2, lbl_plyr_card3, lbl_plyr_card4, lbl_plyr_card5]
dealer_card_lbls = [lbl_deal_card1, lbl_deal_card2, lbl_deal_card3, lbl_deal_card4, lbl_deal_card5]

def disable_buttons():
  btn_reveal.config(state=tk.DISABLED)
  btn_add_dealer2.config(state=tk.DISABLED)
  btn_add_dealer4.config(state=tk.DISABLED)
  btn_add_plyr.config(state=tk.DISABLED)

def save_progress():
  with open('money.json', 'w') as m:
    m.write(str(money))
  with open('powerups.json', 'w') as p:
    json.dump(powerups, p)

  m.close()
  p.close()

def card_value(card, points=0):
  try:
    return int(card)
  except:
    if card == 'A':
      if points > 10:
        # make 2 buttons show up for this when changing to tkinter
        return 1
      else:
        return 11
    else:
      return 10

def hit(cards, points):
  sleep(1)
  points += card_value(deck[-1][0], points)
  cards.append(deck.pop())
  lbl_plyr_points.config(text='You have ' + str(points) + ' points')
  return cards, points

def end_game():
  save_progress()
  btn_hit.config(text='Go To Home Screen', bg='grey11', fg='yellow3', command=lambda: [window.destroy(), os.system('python main.py')])
  btn_stand.config(text='I love gambling', bg='grey26', fg='orange red', state = tk.DISABLED)
  print(dealer_cards[0])
  lbl_deal_card1.config(text=str(dealer_cards[0][0]) + dealer_cards[0][1], fg=set_card_color(dealer_cards[0]))
  print(result)

# making the deck with every card
for card_type in card_types:
  for symbol in symbols:
    card = card_type, symbol
    deck.append(card)
# shuffling the deck and choosing a random card
shuffle(deck)
# drawing initial cards and removing the card from the deck(so cards dont repeat)
player_cards = [deck.pop(), deck.pop()]
dealer_cards = [deck.pop(), deck.pop()]

def see_dealer_card():
  global powerup_used
  lbl_deal_card1.config(text=str(dealer_cards[0][0]) + dealer_cards[0][1], fg=set_card_color(dealer_cards[0]))
  powerups['revealdeal'] -= 1
  powerup_used = True
  disable_buttons()

  if powerups['revealdeal'] == 0:
    btn_reveal.config(state=tk.DISABLED)
  save_progress()
  
def addplayer():
  global player_score, powerup_used
  player_score += 2
  lbl_plyr_points.config(text='You have ' + str(player_score) + ' points')
  powerups['player2'] -= 1
  powerup_used = True
  disable_buttons()
  
  if powerups['player2'] == 0:
    btn_add_plyr.config(state=tk.DISABLED)
  save_progress()

def add_dealer2():
  global dealer_score, money, powerup_used
  dealer_score += 2
  powerups['dealer2'] -= 1
  powerup_used = True
  disable_buttons()
  
  if powerups['dealer2'] == 0:
    
    btn_add_dealer4.config(state=tk.DISABLED)
    
  if dealer_score > 21:
    result = 'You Win! The dealer went over 21'
    lbl_result.config(text=result)
    money += bet
    end_game()
  save_progress()

def add_dealer4():
  global dealer_score, money, powerup_used
  dealer_score += 4
  powerups['dealer4'] -= 1
  powerup_used = True
  disable_buttons()
  
  if powerups['dealer4'] == 0:
    btn_add_dealer2.config(state=tk.DISABLED)
    
  if dealer_score > 21:
    result = 'You Win! The dealer went over 21'
    money += bet
    lbl_result.config(text=result)
    end_game()
    
  save_progress()

  
btn_reveal.config(command=see_dealer_card)
btn_add_plyr.config(command=addplayer)
btn_add_dealer2.config(command=add_dealer2)
btn_add_dealer4.config(command=add_dealer4)



def set_card_color(card):
  print(card[1])
  if card[1] == '♠' or card[1] == '♣':
    return 'black'
  else:
    return 'red'
    
def show_cards(player, index):
  if player:
    print(set_card_color(player_cards[plyr_index]))
    plyr_card_lbls[index].config(text=str(player_cards[index][0]) + player_cards[index][1], fg=set_card_color(player_cards[index]))
    index += 1

  else:
    print(dealer_cards[0])
    dealer_card_lbls[index].config(text=str(dealer_cards[index][0]) + dealer_cards[index][1], fg=set_card_color(dealer_cards[index]))
    index += 1

  return index
  
def stand():
  global game_won, game_tied, money, bet, dealer_score, dealer_index, dealer_cards
  while dealer_score < 17 and dealer_score < player_score:
    new_card = deck.pop() 
    dealer_cards.append(new_card) 
    dealer_score += card_value(new_card[0], dealer_score)
    dealer_index = show_cards(False, dealer_index)
  if dealer_score > player_score and dealer_score <= 21:
    result = 'You Lost, the dealer had a higher score'
    lbl_result.config(text=result)
    print(dealer_score, dealer_cards, player_score)
    money -= bet
    end_game()

  elif dealer_score < player_score:
    result = 'You Win! You had a higher score than the dealer'
    lbl_result.config(text=result)
    money += bet
    end_game()
  elif dealer_score > 21:
    result = 'You Win! The dealer went over 21'
    lbl_result.config(text=result)
    end_game()
    money += bet
  else:
    result = 'Its a tie!'
    lbl_result.config(text=result)
    end_game()

plyr_index = show_cards(True, plyr_index)
sleep(1)
plyr_index = show_cards(True, plyr_index)
dealer_index = show_cards(False, dealer_index)
player_score = card_value(player_cards[0][0]) + card_value(player_cards[1][0])
dealer_score = card_value(dealer_cards[0][0]) + card_value(dealer_cards[1][0])

lbl_plyr_points.config(text='You have ' + str(player_score) + ' points')

if player_score == 21 and dealer_score == 21:
  result = 'Its a tie!'
  lbl_result.config(text=result)
  lbl_deal_card1.config(text=show_cards(False, 0), fg=set_card_color(dealer_cards[0]))
  end_game()
elif player_score == 21:
  result = 'YOU GOT A BLACKJACK! You got exactly 21 points and won!'
  lbl_result.config(text=result)
  money += bet
  end_game()

def hit_btn():
  
  global player_cards, player_score, plyr_index, result, dealer_score, dealer_index, money
  
  player_cards, player_score = hit(player_cards, player_score)
  plyr_index = show_cards(True, plyr_index)
  lbl_deal_card1.config(text=str(dealer_cards[0][0]) + dealer_cards[0][1], fg=set_card_color(dealer_cards[0]))
  lbl_plyr_points.config(text='You have ' + str(player_score) + ' points')
  
  if dealer_score < 17: 
    new_card = deck.pop() 
    dealer_cards.append(new_card) 
    dealer_score += card_value(new_card[0], dealer_score)
    dealer_index = show_cards(False, dealer_index)
    
    if dealer_score > 21:
      result = 'You Win! The dealer went over 21'
      lbl_result.config(text=result)
      money += bet
      end_game()

  if dealer_score > 21:
    result = 'You Win! The dealer went over 21'
    lbl_result.config(text=result)
    money += bet
    end_game()
  
  if player_score > 21:
    result = 'You Lost, you went over 21'
    lbl_result.config(text=result)
    money -= bet
    end_game()

btn_hit.config(text='Hit', command=hit_btn)
btn_stand.config(text='Stand', command=stand)

if player_score > 21:
  result = 'You lose, you went over 21'
  lbl_result.config(text=result)
  money -= bet
  end_game()

tk.mainloop()