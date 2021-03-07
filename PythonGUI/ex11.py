import tkinter as tk
from tkinter import ttk

#윈도우 인스턴스 생성
win = tk.Tk()
win.title("파이썬 GUI 프로그래밍 ex11")
win.geometry("800x480+100+100")
win.resizable(1,1)

'''
#width가 작으면, text가 짤린다.
# ttk에서는 height가 지원되지 않는다.
# ttk는 borderwidth를 지원하지 않는다.
# padx도 지원하지않는다.
# 그러나 ttk 디자인이 더 세련되어있다.
label1 = ttk.Label(win, text="Hello Python!!", width=5, background="yellow", foreground="red", relief="ridge",borderwidth=7)
label1.pack()

# tk.Label은 가운데정렬이다. ttk는 왼쪽정렬. 추가로 tk에서는 background, foreground를 bg, fg로 줄여사용할 수 있다.
#relief flat(기본값), groove, raised, ridge, solid, or sunken
# padx, pady속성값은 width, height보다 크면 전체 사이즈가 늘어난다.
label2 = tk.Label(win, text="Hello Tkinter!!", width=10, bg="green", fg="pink", height=5, font="arial", relief="ridge", bd=5, padx=100, pady=50)
label2.pack()
'''
label2 = tk.Label(win, text="Hello Tkinter!!", width=11, bg="green", fg="pink", height=2, font="arial", relief="ridge", bd=5, padx=3, pady=3)
label2.grid(column=3,row=3)
def clickMe():
    button1.configure(text="***")
    label3.config(text="하이") #configure 대신 config도 된다.


label3 = ttk.Label(win, text="아이디")
label3.grid(column=100, row=1000)

# 파이썬은 동적 타입언어이다. 할당된 데이터를 바탕으로 타입을 유추할 수 있다.
# name 변수에 문자열을 할당하면 string타입이 된다. name = "홍길동"
# age변수에 정수를 입력하면 integer가 된다. age = 50

# 그러나, tkinter는 파이썬이 아닌 다른 언어이다. 단지, 파이썬에서 사용할 수 있도록 한 언어이다.
# 따라서 타입을 지정할 때 파이썬처럼 동적으로 타입을 유추하지 않는다. Entry로 받아들이는 타입을 얘기하려고 함.

id = tk.StringVar()
# show를 하면 내가 입력한 모든 글자가 show로 나타난다. show에 여러개를 써도, 첫 문자 1개만 출력됨.
entry1 = ttk.Entry(win, textvariable=id, show="AB")
entry1.grid(column=1, row=0)

button1 = ttk.Button(win, text="클릭", command=clickMe)
button1.grid(column=2, row=0)

win.mainloop()