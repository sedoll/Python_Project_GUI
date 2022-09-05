from tkinter import *

root = Tk()
root.title('나도 GUI') # 창 제목
root.geometry('640x480') # 가로 * 세로 크기 지정

# 여러 줄의 입력을 받을 때에는 text / ex) 게시글
txt = Text(root, width=30, height=5) # text창 추가
txt.pack()

txt.insert(END, '글자를 입력하세요') # text창에 글자 추가

# 한줄로 입력을 받을 때 에는 entry / ex) 아이디, 비밀번호
e = Entry(root, width=30)
e.pack()
e.insert(0, '한 줄만 입력해요')

def btncmd():
    print(txt.get('1.0', END)) # 1 부터 끝까지 모든 텍스트를 가져옴 / 1: 첫번째 라인, 0: 0번째 col 위치
    print(e.get())
    
    txt.delete('1.0', END)
    e.delete(0, END)
    
btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop() # 창이 딛히지 않도록 해줌