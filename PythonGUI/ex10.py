import tkinter as tk

from tkinter import ttk
# tikinter 패키지의 서브모듈 ttk를 가져온다.
# ttk (themad tk를 의미함) : 개선된 GUI를 제공하기위한 모듈

win = tk.Tk()

win.title("파이썬 GUI ex10")

## button1은 밑에있는데도 사용 가능하다.
def clickMe():
    label1.configure(text = "버튼이 클릭되었습니다")
    button1.configure(text = "***")
    label1.configure(foreground = "blue", background = "yellow")

#윈도우창 크기 설정 geometry("너비x높이+x좌표+y좌표")
win.geometry("800x400+300+300")

#위젯이름 = ttk.Label(윈도우이름, text="내용") 지정한 윈도우창에 Label 위젯을 설정
label1 = ttk.Label(win, text="안녕하세요 반갑습니다")
#못박는다. 이런식으로 이해한다.
#label1.pack()

#pack 과 grid는 공존할 수 없다. 에러난다. geometry manager가 grid에 slave됬을 때, pack()에서 에러남.
label1.grid(column = 0, row = 0)

# 위젯이름 = ttk.Button(윈도우이름, test="내용")
button1 = ttk.Button(win, text="클릭", command=clickMe)
#button1.pack()
button1.grid(column=1, row = 0)

#기존에 사용하던 위젯 추가방식
label2 = tk.Label(win, text = "레이블")
#label2.pack()
label2.grid(column=0, row=1)

button2 = tk.Button(win, text="버튼2")
#button2.pack()

#화면에 GUI를 출력
win.mainloop()

# tkinter 패키지는 위젯이 없을 때는 기본 크기를 사용한다.
# 그런데, 위젯을 추가하면 일반적으로 위젯을 표시하는데 필요한만큼의 작은
# 공간을 사용하도록 최적화가 발생한다. (창이 위젯크기만큼으로 재설정된다)