# ScrollBar 위젯
'''
생성
    tkinter.Scrollbar(윈도우이름, 파라미터1, 파라미터2, ...)
    : 스크롤바 객체를 생성해서 적용할 위젯을 연결한다.
    : 스크롤바와 연결된 위젯은 각각의 개체이므로, '프레임'을 활용한다

Scrollbar 파라미터 (tkinter 기준)
    width           : 기본값은 17
    relief          : 스크롤바의 테두리 모양(기본값:flat)
    borderwidth
    background==bg
    elementborderwidth  : 스크롤 요소의 테두리 두께(기본값: -1)
    orient              : 스크롤의 표시 방향. 기본값:vertical. {vertical, horizontal}

Scrollbar 형식 설정
    cursor              : 스크롤바의 마우스 커섬 오야

Scrollbar상태 설정
    activebackground    : ative상태일 때 스크롤바의 배경 색상
    activerelief        : active상태일 때 스크롤바의 테두리 모양

Scrollbar 하이라이트 설정
    highlightcolor
    highlightbackground
    highlightthickess

Scrollbar 동작 설ㅈ어
    tabkeyfocus
    command
    jump                : 스크롤이 동작할 때마다 command callback 호출 (기본값: False)
    repeatdelay         : 버튼이 눌러진 상태에서 command가 호출될 떄까지의 대기시간(기본값: 300ms)
    repeatinterval      : 버튼이 눌러진 상태에서 command의 호출이 반복되는 시간(기본값: 100ms)

Scrollbar 메소드
    set                     : 스크롤 부착 - 위젯에 스크롤바를 적용
    set(좌측상단, 우측하단)    : 스크롤 부착 - 좌측상단, 우측하단에 고정시키겠다는 의미.
    get                     : 좌측상단 좌표와 우측 하단 좌표를 리턴한다.
'''