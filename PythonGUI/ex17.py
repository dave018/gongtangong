# Radiobutton 사용(이벤트 처리)

import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title("Radiobutton2_ex17")
win.geometry("320x280+200+200")
win.resizable(False, False)

win.config(background="pink")

def setWindowBGColor():
    radioVar = radioColor.get()
    if radioVar == 1: win.config(background=Color1)
    if radioVar == 2: win.config(background=Color2)
    if radioVar == 3: win.config(background=Color3)
    if radioVar == 4: win.config(background=Color4)
    radio5.flash() # flash가 수행중이기 때문에 re-draw가 되지 않는다. 즉, flash가 끝나야 window 배경색이 변경됨. from ex18

Color1 = "Blue"
Color2 = "Yellow"
Color3 = "Red"
Color4 = "LightGreen"

radioColor = tk.IntVar()

radio1 = tk.Radiobutton(win, text=Color1, value=1, variable = radioColor, command=setWindowBGColor)
radio1.grid(column=0, row=0, sticky="w")

radio2 = tk.Radiobutton(win, text=Color2, value=2, variable = radioColor, command=setWindowBGColor)
radio2.grid(column=1, row=0, sticky="w")

radio3 = ttk.Radiobutton(win, text=Color3, value=3, variable = radioColor, command=setWindowBGColor)
radio3.grid(column=2, row=0, sticky="w")

radio4 = ttk.Radiobutton(win, text=Color4, value=4, variable = radioColor, command=setWindowBGColor)
radio4.grid(column=3, row=0, sticky="w")

radio5 = tk.Radiobutton(win, text="flash", value=5, variable = radioColor, activebackground="Blue")
radio5.grid(column=4, row=0, sticky="w")

win.mainloop()