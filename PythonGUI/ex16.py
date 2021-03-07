# Radiobutton : 단일 선택을 하기 위해 사용하는 위젯

import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("ex16_Radiobutton 위젯")
win.geometry("320x240+300+300")
win.resizable(False, False)

radioVar1 = tk.IntVar()
radioVar2 = tk.IntVar()

def check():
    label1.configure(text="RadioVariety_1 = " + str(radioVar1.get()) + "\n" +
                        "RadioVariety_2 = " + str(radioVar2.get()) + "\n\n" +
                        "Total = " + str(radioVar1.get() + radioVar2.get()))
                        # get() 으로 더해야 한다. tk.IntVar 끼리는 더할 수 없다.

radBtn1 = tk.Radiobutton(win, text="1번", value=1, variable=radioVar1, command=check)
radBtn1.pack()

radBtn2 = tk.Radiobutton(win, text="2번", value=2, variable=radioVar2, command=check)
radBtn2.pack()

radBtn3 = tk.Radiobutton(win, text="3번", value=3, variable=radioVar1, command=check)
radBtn3.pack()

radBtn4 = tk.Radiobutton(win, text="4번", value=4, variable=radioVar2, command=check)
radBtn4.pack()

radBtn5 = tk.Radiobutton(win, text="3번", value=5, variable=radioVar2, command=check)
radBtn5.pack()

label1 = tk.Label(win, text="None", height=5)
label1.pack()

label2 = tk.Label(win, text="None2", height=5)
label2.pack()

win.mainloop()