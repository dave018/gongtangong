#Text : 여러 줄의 문자열을 출력하기 위한 텍스트를 생성할 수 있는 위젯

'''
생성방법
tkinter.Text(윈도우이름, 파라미터1, 파라미터2, ...)
Text 파라미터
    [텍스트 설정 parameter] 문단설정과 유사하다.
    wrap        : 자동 줄바꿈 방법 설정. 기본값:char. {none, char, word} word는 단어단위로 줄바꿀지, 글자로 내릴지 설정하는 것.
    tabs        : Tab키에 대한 설정. 기본값:56
    tabstyle    : Tab 간격 형식에 대한 설정. 기본값:tabular. {tabular, wordprocessor}
    startline   : 텍스트의 데이터 저장소에 저장될 startline 지정.
    endline     : 텍스트의 데이터 저장소에 저장될 endline 지정.
    spacing1    : 텍스트의 상단 수직 간격. 최상단. 기본값:0
    spacing2    : 텍스트의 줄간격. 기본값:0
    spacing3    : 텍스트의 하단 수직 간격. 최하단. 기본값:0

    [텍스트 형태 설정 parameter]
    width               : width.
    height              : height.
    relief              : 테두리의 모양.
    borderwidth=bd      : 테두리 두께.
    background=bg       : 배경색.
    forground=fg        : 폰트색.
    insertwidth         : 키보드 커서의 너비. 기본값:2
    insertborderwidth   : 커서의 테두리 두께. 기본값:0
    insertbackground    : 키보드 커서의 색상.
    selectborderwidth   : 텍스트 블록처리 했을 때의 테두리 두께
    selectbackground    : 텍스트 블록처리 배경색
    selectforground     : 텍스트 블록처리 폰트색
    inactiveselectbackground    : 다른 위젯을 선택했을 때 블록처리에 대한 배경색...
    padx, pady          : 안쪽 여백

    [텍스트 형식 설정 parameter]
    font                : 텍스트의 폰트(=글꼴) 설정
    cursor              : 텍스트의 마우스 커서 모양
    xscrollcommand      : 텍스트의 가로 스크롤 객체 적용 여부(Scrollbar위젯.set 으로 지정)
    yscrollcommand      : 텍스트의 세로 스크롤 객체 적용 여부(Scrollbar위젯.set 으로 지정)
    exportselection     : 텍스트의 선택 가능 여부. 기본값:True.
    segrid              : 텍스트에 대한 grid크기 조정설정 가능여부. 기본값:False

    [텍스트의 highlight 설정 parameter]
    highlightcolor      : 텍스트가 선택되었을 때 색상
    highlightbackground : 텍스트가 선택되지 않았을 때 색상. 기본값:system button
    highlightthickness  : 텍스트가 선택되었을 때 두께. 기본값:system window

    [텍스트의 동작 설정 parameter]
    takefocus           : Tab키로 위젯 이동 허용 여부. 기본값:False
    blockcursor         : 텍스트의 키보드 커서를 블록으로 사용할지 여부. 기본값:False. Block은 리눅스 VI에서의 커서임.
    undo                : 텍스트의 실행 취소 사용 여부. 기본값:False
    maxundo             : 텍스트 실행취소 최대 횟수.
    autoseparators      : 텍스트 실행취소했을 때 자동 저장 여부. 기본값:True

Text의 문자열 메소드
    * index 는 y.x로 사용. y줄 x번째 문자를 의미한다. ex) 1.0 = 첫번째 줄 첫번째 글자
    insert(index, "문자열") 문자열 삽입: index 위치에 문자열을 삽입
    delete(start_index, end_index) 문자열 삭제
    get(start_index, end_index) 문자열 반환
    index(index) 인덱스 반환. 인덱스가 음수일 경우, 1.0으로 반환.
    see(index) 문자열 표시 반환. index위치에 텍스트가 표시되면 True 반환

Text Mark 메소드
    tag_add(tagname, start_index, end_index) 태그 생성 : start~end까지의 tagname을 생성
    tag_remove(tagname, start_index, end_index) 태그 제거 : tagname설정을 제거
    tag_delete(tagname) 태그 삭제 : tagname의 설정 및 선언 삭제
    tag_config(tagname, 파라미터1, 파라미터2, ...) : tagname의 범위만큼 속성 설정
'''

import tkinter as tk

win = tk.Tk()
win.geometry("320x280+200+200")
win.title("Text위젯_ex19")
win.resizable(False, False)

text1 = tk.Text(win)
text1.insert(tk.CURRENT, "안녕하세요. 반갑습니다.\n") #tk.CURRENT 는 현재 위치에 문자열을 넣겠다는 뜻
text1.insert(tk.CURRENT, "파이썬 스터디\n")
text1.insert(2.3, "!!")
text1.insert(1.0, "삽입\n")
text1.insert(1.1, "삽")
text1.insert(tk.END, "ByeBye\n")
text1.pack()

text1.tag_add("강조", 3.0, 3.3) #2.0이상 2.4이하
text1.tag_config("강조", foreground="Blue", background="Red")
text1.tag_add("강조2", 3.6, 3.9) #끝 범위를 벗어나거나, end_index<=start_index인 경우, 동작안함
text1.tag_config("강조2", background="LightGreen")
text1.tag_add("강조3", 4.0, tk.END) # END는 글자가 아니라 오른쪽 끝까지 다 지정된다. 강조 3은 나중에 추가한 "BBB"에도 적용된다.
text1.tag_config("강조3", background="Yellow")
text1.insert(tk.END, "BBB")

'''
# 이럴수가 text2는 안보인다..
text2 = tk.Text(win)
text2.insert(tk.CURRENT, "안녕하세요!!")
text2.pack()
'''

win.mainloop()