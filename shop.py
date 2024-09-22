import tkinter as tk
import json
import os

window = tk.Tk()
window.geometry('520x520')
window.title("Welcome to the Shop")
window.config(bg="seagreen")
window.attributes('-fullscreen', True)

# Load powerups from powerups.json
with open('powerups.json') as p:
    powerups = json.load(p)

# Load player's money from money.json file
with open('money.json') as m:
    money = int(m.read())

# Function to update money label
def show_money():
    lbl_money.config(text="Money: " + str(money))

# Function to update powerups label
def show_powerups():
    powerup_text = 'Powerups:\nReveal Dealer Card: ' + str(powerups['revealdeal']) + '\Add 2 to player score: ' + str(powerups['player2']) + '\nAdd 2 To Dealer: ' + str(powerups['dealer2']) + '\nAdd 4 To Dealer: ' + str(powerups['dealer4'])
    lbl_powerups.config(text=powerup_text)

# Function to update powerups dictionary and money label
def update_powerups_and_money(cost, powerupchosen):
    global money
    global powerups
    if money >= cost:
        money -= cost
        powerups[powerupchosen] += 1
        
        with open('money.json', 'w') as m:
            m.write(str(money))
            
        with open('powerups.json', 'w') as p:
            json.dump(powerups, p)
            
        show_money()  # Update money label after deduction
        show_powerups()  # Update powerups label after deduction

def run_core_py():
    window.destroy()
    os.system("python core.py")

lbl_money = tk.Label(window, text="Money: ", font=("Arial", 12), bg='seagreen', fg='white')
lbl_money.pack()

lbl_powerups = tk.Label(window, text="", font=("Arial", 9), bg='seagreen', fg='white')
lbl_powerups.pack()

show_money()  # Initial display of money
show_powerups()  # Initial display of powerups

Shop = tk.Label(text="POWERUPS:", font=("Comic Sans MS", 20), bg='seagreen', fg='ghost white')
Shop.pack()

Shop_but = tk.Button(text='Reveal Dealer Card --- $320', font=("Arial", 9), bg='dark green', fg='white', state=tk.NORMAL if money >= 320 else tk.DISABLED, command=lambda: update_powerups_and_money(320, 'revealdeal'))
Shop_but.pack(pady=30)

Shop_but2 = tk.Button(text='Add 2 to your points --- $200', font=("Arial", 9), bg='dark green', fg='white', state=tk.NORMAL if money >= 200 else tk.DISABLED, command=lambda: update_powerups_and_money(200, 'player2'))
Shop_but2.pack(pady=30)

Shop_but3 = tk.Button(text='Dealer gets +2 to total --- $450', font=("Arial", 9), bg='dark green', fg='white', state=tk.NORMAL if money >= 450 else tk.DISABLED, command=lambda: update_powerups_and_money(450, 'dealer2'))
Shop_but3.pack(pady=30)

Shop_but4 = tk.Button(text='Dealer gets +4 to total --- $800', font=("Arial", 9), bg='dark green', fg='white', state=tk.NORMAL if money >= 800 else tk.DISABLED, command=lambda: update_powerups_and_money(800, 'dealer4'))
Shop_but4.pack(pady=30)

btn_run_core = tk.Button(window, text="Back!", command=run_core_py, font=("Helvetica"), bg='dark green', fg='ghost white')

btn_run_core.pack()

blackjack_image = tk.PhotoImage(file='Blackjack.gif')
btn_blackjack = tk.Label(window, image=blackjack_image, bg='seagreen')
btn_blackjack.pack()


    




window.mainloop()
