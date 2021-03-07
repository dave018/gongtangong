# Checkbutton 사용 (이벤트 처리)

import tkinter as tk
from tkinter import ttk

win = tk.Tk()

win.title("Checkbutton2_ex18")
win.geometry("320x280+200+200")
win.resizable(False, False)

def flash() :
    checkbutton1.flash()
    # 깜빡임을 잠시 수행해줌 (normal상태의 배경색상과 active상태의 배경색을 깜빡임)

checkVar1 = tk.IntVar()
checkVar2 = tk.IntVar()
checkVar3 = tk.IntVar()

checkbutton1 = tk.Checkbutton(win, text="o", variable=checkVar1, activebackground="Blue", command=flash)
# activebackground는 클릭중일 때의 배경색이다.
checkbutton2 = ttk.Checkbutton(win, text="△", variable=checkVar2)
checkbutton3 = tk.Checkbutton(win, text="X", variable=checkVar3, activebackground="Yellow", command=flash)
#ttk는 activebackground가 없다.
# variable로 같은 변수를 사용하면, 체크할 때 같이 체크된다.

checkbutton1.pack()
checkbutton2.pack()
checkbutton3.pack()

win.mainloop()