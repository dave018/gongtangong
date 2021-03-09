import tkinter as TK
from tkinter import ttk as TTK

isBlack = 1

class Board(TK.Canvas):
    WIDTH = 500
    HEIGHT = 500
    GAP = 25
    START = 25
    MAX_LINE = 19 - 1
    OUT_SPAN = 10

    def drawBoard(self):
        gap = Board.GAP
        start_p = Board.START
        max_line = Board.MAX_LINE
        end_p = start_p + gap * max_line
        out_span = Board.OUT_SPAN
        
        rectArgs=[start_p-out_span,start_p-out_span,end_p+10,end_p+10]

        #draw outline
        self.mCanvas.create_rectangle(rectArgs, fill="gold")

        #draw horizon/vertical lines
        for i in range(19):
            self.mCanvas.create_line(start_p+i*gap, start_p, start_p+i*gap, end_p) #vertical
            self.mCanvas.create_line(start_p, start_p+i*gap, end_p, start_p+i*gap) #horizon

        # directional point only x and y in [3, 9, 15] points
        half_rad = 2
        for i in (3,9,15):
            for j in (3,9,15):
                tempOval = self.mCanvas.create_oval(start_p + (i * gap) - half_rad, 
                                                    start_p + (j * gap) - half_rad,
                                                    start_p + (i * gap) + half_rad, 
                                                    start_p + (j * gap) + half_rad, 
                                                    fill="black")

    @classmethod
    def getBrd2Cnv(cls, x, y):
        gap = Board.GAP
        start_p = Board.START
        max_line = Board.MAX_LINE
        end_p = start_p + gap * max_line
        out_span = Board.OUT_SPAN

        # I wish except 'or'.
        if max_line < x or max_line < y:
            return (-1, -1)
        
        return tuple(map(lambda X: start_p + X*gap, (x,y)))

    def pack(self, packSide):
        self.mCanvas.pack(side=packSide)
    
    # this should be in client_event
    def addStone(event):
        end_p = Board.START + Board.GAP * Board.MAX_LINE
        x = event.x
        y = event.y
        if ((x < Board.START-Board.OUT_SPAN) or 
            (x > end_p + Board.OUT_SPAN) or
            (y < Board.START-Board.OUT_SPAN) or
            (y > end_p + Board.OUT_SPAN)) :
            return
        
        # start - out_span < x < start && out_span > 0.5*gap
        if (x < Board.START): x = Board.START
        if (end_p < x) : x = end_p
        if (y < Board.START): y = Board.START
        if (end_p < y) : y = end_p

        x,y = tuple(map(lambda X: round(X / Board.GAP, 0), (x,y)))
        print(x,y)
        x,y = Board.getBrd2Cnv(x-1,y-1)

        rad = 10
        stoneColor = "black"
        tCanvas=event.widget
        global isBlack
        if isBlack == 0:
            stoneColor="white"
            isBlack = 1
        else:
            isBlack = 0
        tCanvas.create_oval(x-rad, y-rad, x+rad, y+rad, fill=stoneColor)
    
    def __init__(self, master): #check which side
        self.mCanvas = TK.Canvas(master, width=Board.WIDTH, height=Board.HEIGHT, bd=2)

        #this should be client_application
        self.mCanvas.bind("<Button-1>", Board.addStone)
    

class Stone(TK.Image):
    def __init__(self):
        self.board_x = 0
        self.board_y = 0
    
    def drawStone(x, y):
        self.board_x = x
        self.board_y = y
    
class MasterWindow(TK.Tk):
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 600
    WINDOW_OUT_SPAN_X = 100
    WINDOW_OUT_SPAN_Y = 100
    WINDOW_GEOMETRY= "%dx%d+%d+%d" % (WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_OUT_SPAN_X, WINDOW_OUT_SPAN_Y)

    def __init__(self):
        TK.Tk.__init__(self)
        if __name__ == '__main__':
            self.title("client_gui")
        else :
            self.title("gongtangong_client")
        self.geometry(MasterWindow.WINDOW_GEOMETRY)
        self.resizable(0,0)
        self._frame = GameFrame(self)
        self._frame.pack(fill='both', expand=True)

class GameFrame(TK.Frame):
    def __init__(self, master):
        TK.Frame.__init__(self, master)
        self.mBoard = Board(self)
        self.mBoard.pack('left')
        self.mBoard.drawBoard()

        #temporary user profile
        # nickname, win/lose, ...
        usersFrame = TK.Frame(self, relief="solid", bd=2)
        usersFrame.pack(side="right", fill="both",expand=True)
        label1 = TK.Label(usersFrame, text="PLAYER_1", bg="green")
        label1.pack(side="top", fill="both", expand=True)
        label2 = TK.Label(usersFrame, text="PLAYER_2", bg="pink")
        label2.pack(side="bottom", fill="both", expand=True)

if __name__ == '__main__':
    print("[client_gui] running as main")
    masterWindow = MasterWindow()
    masterWindow.mainloop()