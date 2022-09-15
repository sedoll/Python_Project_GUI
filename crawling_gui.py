# 메세지 박스
import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title('네이버 뉴스 라이브러리 크롤링 프로그램') # 창 제목
root.geometry('640x480') # 가로 * 세로 크기 지정

def btncmd():
    if 20 >= len(text_id.get()) >= 5 and 16 >= len(text_pw.get()) >= 8: 
        print(text_id.get(), len(text_id.get()))
        print(text_pw.get(), len(text_pw.get()))
        print(text_pw.get(), len(text_pw.get()))
    else:
        msgbox.showerror("에러", "아이디 또는 비밀번호가 잘 못 입력 되었습니다. \n아이디는 5~20자 \n비밀번호는 8~16자 입니다.")

input_id = ''
input_pw = ''
input_content = ''
input_syear = 1920
input_eyear = 1999
input_page = 1

# 아이디 입력
label_id = Label(root, text='아이디') # 레이블에 글자 출력
label_id.place(x=10, y=10, width=50, height=20)
text_id = Entry(root)
text_id.place(x=70, y=10, width=150, height=20)

# 비밀번호 입력
label_pw = Label(root, text='비밀번호') # 레이블에 글자 출력
label_pw.place(x=10, y=40,  width=50, height=20)
text_pw = Entry(root, width=30)
text_pw.place(x=70, y=40, width=150, height=20)

# 주제 입력
label_content = Label(root, text='주제') # 레이블에 글자 출력
label_content.place(x=10, y=70,  width=50, height=20)
text_content = Entry(root, width=30)
text_content.place(x=70, y=70, width=150, height=20)

# 시작 연도
label_syear = Label(root, text='시작 연도') # 레이블에 글자 출력
label_syear.place(x=10, y=100,  width=50, height=20)
text_syear = Entry(root, width=30)
text_syear.insert(0, 1920)
text_syear.place(x=70, y=100, width=150, height=20)

# 끝 연도
label_eyear = Label(root, text='끝 연도') # 레이블에 글자 출력
label_eyear.place(x=10, y=130,  width=50, height=20)
text_eyear = Entry(root, width=30)
text_eyear.insert(0, 1999)
text_eyear.place(x=70, y=130, width=150, height=20)

# 페이지
label_page = Label(root, text='페이지') # 레이블에 글자 출력
label_page.place(x=10, y=160,  width=50, height=20)
text_page = Entry(root, width=30)
text_page.insert(0, 1)
text_page.place(x=70, y=160, width=150, height=20)

btn = Button(root, text='입력', command=btncmd)
btn.place(x=10, y=200, width=80, height=40)

root.resizable(width=False, height=False) # 창 크기 조절 불가
root.mainloop() # 창이 딛히지 않도록 해줌