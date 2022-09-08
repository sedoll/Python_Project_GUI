import tkinter.ttk as ttk
from tkinter import *

root = Tk()
root.title('나도 GUI') # 창 제목
root.geometry('640x480') # 가로 * 세로 크기 지정

values = [str(i) + '일' for i in range(1, 32)] # 1~31까지의 숫자 반환
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set('카드 결제일') # 최초 목록의 제목

# 읽기만 되는 combobox
readonly_combobox = ttk.Combobox(root, height=10, values=values, state='readonly')
readonly_combobox.current(0) # 0번째 인덱스값 선택
readonly_combobox.pack()

def btncmd():
    print(combobox.get()) # 선택된 값 출력
    print(readonly_combobox.get())
    
btn = Button(root, text='선택', command=btncmd)
btn.pack()

root.mainloop() # 창이 딛히지 않도록 해줌