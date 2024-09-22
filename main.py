import tkinter as tk
import os

window = tk.Tk()

def run_core_py():
    window.destroy()
    os.system("python core.py")

def run_instructions_py():
    window.destroy()
    os.system("python instructions.py")

def exit_game():
    window.destroy()

window.config(bg="seagreen")
window.attributes('-fullscreen', True)
window.geometry('600x500')
window.title("Main Menu")
tk.Label(text='Welcome to BlackJack')

btn_run_main = tk.Button(window, text="Play!", command=run_core_py)

btn_run_inst = tk.Button(window, text="Rules", command=run_instructions_py)

btn_exit = tk.Button(window, text="Exit", command=exit_game, bg='red')

btn_run_main.pack(pady=10)
btn_run_inst.pack(pady=10)
btn_exit.pack(pady=10)


window.mainloop()