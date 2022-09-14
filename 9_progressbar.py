import time
import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title('나도 GUI') # 창 제목
root.geometry('640x480') # 가로 * 세로 크기 지정

# "indeterminate" 언제 끝날지 모르는 창
# "determinate" 처음부터 끝날때 까지 차는 창
# progressbar = ttk.Progressbar(root, maximum=100, mode="indeterminate")
# progressbar = ttk.Progressbar(root, maximum=100, mode="determinate")
# progressbar.start(5) # 5ms 마다 움직임
# progressbar.pack()

# def btncmd():
#     progressbar.stop() # 프로그레스바 중지
    
# btn = Button(root, text='선택', command=btncmd)
# btn.pack()

p_var2 = DoubleVar()
progressbar2 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var2)
progressbar2.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01)
        
        p_var2.set(i) # 1 ~ 100
        progressbar2.update() # ui 업데이트
        print(i)
        
btn = Button(root, text='시작', command=btncmd2)
btn.pack()

root.mainloop() # 창이 딛히지 않도록 해줌