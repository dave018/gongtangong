'''
위젯 파라미터
    [문자열 설정 parameter]
    text            : 체크버튼 옆에 표시할 문자열
    textvariable    : 체크버튼(안?밖?)에 표시할 문자열을 가져올 변수
    anchor          : 체크버튼 내의 문자열이나 체크버튼 자체의 이미지의 위치를 지정(기본값:center)
                        8방위다. North, South의 앞글자만 따서 n(북), ne(북동), sw(남서), 등 + center
    justify         : 체크버튼 안의 문자열이 여러 줄일 경우에 정렬 방법 (기본값 : center)
    wraplength      : 자동 줄내림 설정 너비. 일정 너비를 벗어나면 줄바꿈을 하겠다. (기본값 : 0)

    [모양 설정 parameter]
    width           : 체크버튼의 너비
    height          : 체크버튼의 높이
    relief          : 체크버튼의 테두리 모양 (기본값: flat)0
    overrelief      : 체크버튼에 마우스를 올렸을 때 체크버튼의 테두리모양 (기본값: raised)
    background(bg)  : 문자열의 백그라운드 색상 (기본값 : SystemButtonFace)
    foreground(fg)  : 문자열의 색상 (기본값 : SystemButtonFace)
    selectcolor     : 체크버튼 상태의 배경 색 (기본값: SystemWindow)
    padx, pady      : 내용물의 안쪽 여백.

    [상태 설정 parameter]
    state            : 상태 설정(기본값 : normal) active, disabled.
    activebackground : active 상태일 때 체크버튼의 background색 (기본값 : SystemButtonFace)
    activeforeground : active 상태일 때 체크버튼의 문자열 색 (기본값 : SystemButtonFace)
    disabledforground : disabled상태일 때 체크버튼의 문자열 색상(SystemDisabledText)

    [동작 설정 parameter]
    takefocus       : tab키를 통해 위젯 focus를 이동 허용 여부 결정 (기본값 : True), False
    command         : active상태일 때 실행할 메소드를 지정. 이벤트함수겠지?
    variable        : 체크버튼의 상태를 저장할 제어 변수(tkinter.IntVar(), tkinter.StringVar())
    onvalue         : 체크버튼이 체크된 상태일 때, 연결된 제어변수의 값 (기본값: True), False
    offvalue        : 체크버튼이 해제된 상태일 때, 연결된 제어변수의 값 (기본값: False), True
    indicatoron     : 설명안해줌 ㅠㅠ
    하이라이트 : 버튼이 선택됬을 때의 색상, 안선택됬을떄의 색상
'''

# Checkbutton
# 여러개의 항목을 다중 선택할 때 사용 <-> radio button
# 생성방법
# tkiner.Checkbutton(윈도우, 파라미터1, 파라미터2, ...) #ttk가 아니라 tk기준으로 설명.
# ? 체크버튼 옆과 내부에 있는 문자열은 서로 다른것 아닌가??
'''
체크버튼
    [체크버튼의 method]
    select()        : 체크상태
    deselect()      : 해제 상태
    toggle()        : 토글. 체크버튼을 체크->해제, 해제->체크 되게 만들어줌.
    invoke()        : 체크버튼 실행.....? 읭?
    flash()         : 깜빡거림. Normal과 Active색이 서로 다를 때, flash()하면 깜빡이나봐.
    
    [체크버튼의 형식 설정]
    bitmap          : 체크버튼에 포함할 기본 이미지
    image           : 체크버튼에 포함할 임의의 이미지
    selectimage     : 체크상태일 때 표시할 임의의 이미지
    compound        : 체크버튼에 문자열과 이미지를 동시에 표시할 때, 이미지의 위치 (기본값은: none) bottom, center, left, right
    font            : 체크버튼의 문자열 글꼴 설정 (TkDefaultFont)
    cursor          : 체크버튼의 마우스 커서 모양
'''

# 16강에서 가져왔다.
import tkinter as tk
from tkinter import ttk

win = tk.Tk()
win.title("ex15_체크버튼")
win.geometry("480x240+300+300")

ent1 = tk.Entry(win)
ent1.grid(column=0, row=0)

ent2 = tk.Entry(win)
ent2.grid(column=1, row=0)

chkBtn1 = tk.Checkbutton(win, text="독서", state="disabled")
chkBtn1.select()
chkBtn1.grid(column=0,row=1, sticky = tk.W)
#sticky는 방향과 관련이 있다. tk.E는 East이다. 우측정렬이 된다. 안주면 center가되는데, center속성은 없다.
# 추가로, tk.E 대신 string으로 설정할 수 있다..

chkBtn2 = tk.Checkbutton(win, text="운동")
chkBtn2.select()
chkBtn2.grid(column=1,row=1, sticky = "e")

chkBtn3 = tk.Checkbutton(win, text="영화감상")
chkBtn3.grid(column=2, row=1)


win.mainloop()