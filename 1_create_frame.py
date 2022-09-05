from tkinter import *

root = Tk()
root.title('나도 GUI') # 창 제목
root.geometry('640x480') # 가로 * 세로 크기 지정
# root.geometry('640x480+300+100') # 창이 나타나는 위치 x좌표 + y좌표
root.resizable(False, False) # x, y 값 변경 불가, 창 크기 변경 불가
root.mainloop() # 창이 딛히지 않도록 해줌