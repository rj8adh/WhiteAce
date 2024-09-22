import tkinter as tk
import json
import os

window = tk.Tk()
window.geometry('520x520')
window.title("Rules and advice")
window.attributes('-fullscreen', True)

objective = tk.Label(text='Your objective is to beat the dealer by getting a count as close to 21 as possible,without going over 21.' , font=("Arial", 9))
objective.pack(pady=30)
rules = tk.Label(text='Rules: The player is dealt two cards. The dealer is dealt two cards, with one of the dealer\'s cards face down and one face up.The player can choose to hit or stand.')
rules.pack(pady=30)
rules2 = tk.Label(text='If the player hits, they are dealt a random card from the deck. Cards 2-10 are worth their face value. Jacks, Queens, and Kings are worth 10. Aces are worth 1 or 11, whatever is more benefical for the player.', font=('Arial', 9))
rules2.pack(pady=30)
advice = tk.Label(text='Advice: If you have less than 10 points, you should hit. If you have more than 10 points, you should probably stand.', font=('Arial', 9))
advice.pack(pady=30)
window.config(bg="seagreen")

def run_core_py():
  window.destroy()
  os.system("python core.py")
    
btn_run_core = tk.Button(window, text="Back!", command=run_core_py, font=("Helvetica"), bg='dark green', fg='ghost white')
btn_run_core.pack(pady=30)

window.mainloop()
