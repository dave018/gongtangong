# Tkinter 주요 위젯

'''
Button      버튼
Label       텍스트 또는 '이미지' 표시
CheckButton 체크박스
RadioButton 옵션버튼(라디오버튼) 상호배제 선택
Entry       단순한 라인 텍스트 박스
ListBox     목록
Message     Label과 비슷한데, 자동으로 wrapping 가능
Scale       슬라이스 바
Scrollbar   스크롤 바
Text        멀티라인을 제공하는 텍스트 박스
Menu        상단 메뉴 패널. (메뉴 패널 안에 메뉴(파일(F), 편집(E) 등)가 있는것이다)
Menubutton  메뉴 버튼
Toplevel    Top Level은 새로운 윈도우, 새로운 dialog를 만들 때 사용한다. win = Tk()할 때 Tk가 윈도우를 자동으로 생성하는 클래스.
Combobox    드롭다운 콤보박스
Frame       Container 위젯. 다른 위젯을 그룹화할 때 사용
Canvas      그래프, 점들로 그림을 그릴 수 있는 위젯. custom 위젯을 만들 때 사용
'''

# Tkinter 라이브러리 구조

'''
Window 안에 Label, Entry, Frame, Button 등의 라이브러리?가 있다.
Frame은 내부에 다시 위젯이 있다.
Tkinter는 따로 설치 없이 바로 사용할 수 있다.
'''

# tkinter가 GUI 모듈이다.
import tkinter as tk

# 인스턴스 생성. win은 윈도우 이름.
win = tk.Tk()

win.title("파이썬 GUI")

# 이 사이에 내가 만들 위젯을 윈도우에 적용시키면 된다.

# 윈도우의 사이즈 조정을 막기위한 메소드 : 윈도우.resizeable(좌우, 상하)
# 상하 좌우의 크기 조정 여부를 설정할 경우 True = 1, False = 0
# 0,0으로 하면 최대화 버튼이 잠긴다.
win.resizable(0, 0)

win.mainloop() # 화면에 GUI를 보이도록 한다. 윈도우가 종료될 때까지 실행된다. 이벤트가 들어오면 처리하는 등...
