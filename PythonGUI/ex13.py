import tkinter as tk
from tkinter import ttk

# 참고로 Button에 command를 설정할 때, 함수는 더 위쪽에 설정되어 있어야 한다.
def select():
    label2.config(text=fruitName.get() + "를 "+ amount.get()+"개 선택하셨습니다")

win = tk.Tk()

win.title("ex13  콤보박스 위젯")

win.geometry("320x240+50+50")

ttk.Label(win, text="과일명 입력").grid(column=0, row=0) #이렇게 한줄로도 사용할 수 있다. 대신 나중에 수정이 안되겠지..? grid로되나?
# 그러고보니 win은 Tk()라서, tk위젯, ttk위젯 동시에 사용이 가능하다.

ttk.Label(win, text="개수를 입력하세요 : ").grid(column=1, row=0)

fruitName = tk.StringVar()
fruitEntry = ttk.Entry(win, textvariable = fruitName, width=9)
fruitEntry.grid(column=0, row=1)

# 참고로, Entry, Combobox 모두 state="disable" 가 가능하다.

amount = tk.StringVar()
combo1 = ttk.Combobox(win, textvariable = amount, width=5)
combo1.grid(column=1, row=1)
combo1['values'] = (5,10,15,20) #['values'] = (튜플) 로 콤보박스 아이템을 설정할 수 있다. 즉, combobox는 dic(string, tuple)이다.

button1 = ttk.Button(win, text="확인", command=select)
button1.grid(column=2, row=1)

label2 = ttk.Label(win, text="", background="yellow")
label2.grid(column=0, row=2)

fruitEntry.focus()

win.mainloop()