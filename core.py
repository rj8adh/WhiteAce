import tkinter as tk
import json
import time
import random
import os

with open('money.json') as m:
  money = int(m.read())
    
m.close()

bet = 0
window = tk.Tk()
window.geometry('520x520')
window.title("Welcome to White Ace")
window.config(bg="seagreen")
window.attributes('-fullscreen', True)

# Run the shop
def run_Shop_py():
    window.destroy()
    os.system("python shop.py")

btn_run_Shop = tk.Button(window, text="Shop!", command=run_Shop_py, bg='dark green', fg='ghost white')
lbl_money = tk.Label(text='You have $' + str(money), bg='dark green', fg='ghost white')

btn_run_Shop.pack(pady=10)
lbl_money.pack(pady=10)

# Open instructions
lbl_cardslot = tk.Label()
bet_entry = tk.Entry(window)
bet_entry.pack(pady=10)

def save_bet():
    bet = int(bet_entry.get())
    with open('bet.json', 'w') as file:
        json.dump(bet, file)
        
def play_game():
    save_bet()
    window.destroy()
    os.system("python card_chooser.py")

hello23 = tk.Button(text="Start", state=tk.DISABLED if bet <= 0 and bet >= money else tk.NORMAL, command=play_game,bg='dark green', fg='ghost white')

hello23.pack(pady=10)

# Saving the bet amount entered by the user

tk.mainloop()