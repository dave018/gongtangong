import tkinter as TK
from tkinter import ttk as TTK

def myEnter(event):
    event.widget.configure(bg="green")
def myLeave(event):
    event.widget.configure(bg="white")

GO_BOARD_WIDTH=500
GO_BOARD_HEIGHT=500
GO_BOARD_BD=3
GO_BOARD_BG="brown"

win = TK.Tk()
win.title("오목_client")
win.geometry("800x500+100+100")
win.resizable(0,0)

goBoard = TK.Canvas(win, width=GO_BOARD_WIDTH, height=GO_BOARD_HEIGHT,
                    bd=GO_BOARD_BD)
goBoard.pack(side="left")

START_X=25
START_Y=25
END_X=475
END_Y=475
GAP=25

pointList = []
for i in range(19):
    for j in range(19):
        tempPoint = TK.Label(win, width=1, height=1)
        tempPoint.bind("<Enter>", myEnter)
        tempPoint.bind("<Leave>", myLeave)
        tempPoint.place(x=START_X + GAP*i-1, y=START_Y + GAP*j-1)
        pointList.append(tempPoint)

# board lines
goBoard_rectArgs=[15,15,485,485]
goBoard.create_rectangle(goBoard_rectArgs, fill="gold")
for i in range(19):
    goBoard.create_line(START_X+i*GAP, START_Y, START_X+i*GAP, END_Y) #vertical
    goBoard.create_line(START_X, START_Y+i*GAP, END_X, START_Y+i*GAP) #horizon
'''
    for j in range(19):
        goBoard.create_oval(START_X+GAP*i-2, START_Y+GAP*j-2,
                            START_X+GAP*i+2, START_Y+GAP*j+2, fill="black")
'''

# directional point
for i in range(3):
    for j in range(3):
        jumpXGap = (3+i*6) *GAP
        jumpYGap = (3+j*6) *GAP
        tempOval = goBoard.create_oval(START_X+jumpXGap-2, START_Y+jumpYGap-2,
                            START_X+jumpXGap+2, START_Y+jumpYGap+2, fill="black")

#각 점들에 대해 마우스 호버링 event 달기
'''
        self.l1.bind("<Enter>", self.on_enter)
        self.l1.bind("<Leave>", self.on_leave)

    def on_enter(self, event):
        self.l2.configure(text="Hello world")

    def on_leave(self, enter):
        https://stackoverflow.com/questions/20399243/display-message-when-hovering-over-something-with-mouse-cursor-in-python
    
    note: canvas에서 그린 객체에 대해서는 bind할 수 없음(위젯에만 가능)
            '''

        

#panedWin = TK.PanedWindow(win, orient="vertical", bd=3, bg="cyan", fill="both")
#panedWin.grid(column=1,row=0)
usersFrame = TK.Frame(win, relief="solid", bd=2)
usersFrame.pack(side="right", fill="both",expand=True)
label1 = TK.Label(usersFrame, text="BLACK", bg="green")
label1.pack(side="top", fill="both", expand=True)
label2 = TK.Label(usersFrame, text="WHITE", bg="pink")
label2.pack(side="bottom", fill="both", expand=True)

win.mainloop()