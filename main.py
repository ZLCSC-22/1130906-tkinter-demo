import tkinter as tk
import random

window = tk.Tk()
window.title('周奕宇我愛你')
window.geometry('380x400')

v = tk.StringVar()
v.set("輸入數字按下猜按鈕")
tk.Label(textvariable=v).pack(side="bottom")

random_number = random.randint(0, 2)

entry = tk.Entry()

def button_command():
    if (int(entry.get()) == random_number):
        v.set("恭喜猜對了")
        return
    v.set("猜錯了")

tk.Button(text="猜!", command=button_command).pack(side="top")
entry.pack()

window.mainloop()

