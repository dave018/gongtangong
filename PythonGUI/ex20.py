# Scrolltext : 텍스트 위젯을 구현하면서 스크롤바도 구현되는 위젯
# 텍스트 위젯과 스크롤바 위젯을 조금 더 편리하게 사용하는 위젯이다.
'''
생성
    scrolledtext.ScrolledText(윈도우, 파라미터1, 파라미터2, ...)
'''

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext

win = tk.Tk()
win.geometry("320x280+200+200")
win.title("Scrolltext위젯_ex21")
win.resizable(True, True)

def selectColor():
    selectedRadio = radioColor.get()
    if selectedRadio == 0: win.config(background = "Blue")
    if selectedRadio == 1: win.config(background = "Yellow")
    if selectedRadio == 2: win.config(background = "LightGreen")

radioColor = tk.IntVar()
radio1 = tk.Radiobutton(win, text="Blue", variable=radioColor, value=0, command=selectColor)
radio1.grid(column = 0, row=0)
radio2 = tk.Radiobutton(win, text="Yelow", variable=radioColor, value=1, command=selectColor)
radio2.grid(column = 1, row=0)
radio3 = tk.Radiobutton(win, text="LightGreen", variable=radioColor, value=2, command=selectColor)
radio3.grid(column = 2, row=0)

scroll_w = 30
scroll_h = 10

scrText = scrolledtext.ScrolledText(win, width=scroll_w, height=scroll_h, wrap=tk.WORD)
scrText.grid(column = 0, columnspan = 3) # 이렇게 하면 얘 혼자 column을 3개 다 잡아먹음.

win.mainloop()