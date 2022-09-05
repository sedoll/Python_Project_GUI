from tkinter import *

n = 1 # 동적 변경을 위한 변수

root = Tk()
root.title('나도 GUI') # 창 제목
root.geometry('640x480') # 가로 * 세로 크기 지정

label1 = Label(root, text='안녕하세요') # 레이블에 글자 출력
label1.pack()

photo1 = PhotoImage(file='img.png') # 레이블에 이미지 출력
photo2 = PhotoImage(file='img2.png') # 레이블에 이미지 출력
label2 = Label(root, image=photo1)
label2.pack()

def change():
    global n
    if(n):
        label1.config(text='또 만나요')
        label2.config(image=photo2)
        n=0
    else:
        label1.config(text='안녕하세요')
        label2.config(image=photo1)
        n=1

btn = Button(root, text='클릭', command=change)
btn.pack()

root.mainloop() # 창이 딛히지 않도록 해줌