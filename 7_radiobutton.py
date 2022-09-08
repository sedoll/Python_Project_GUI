from tkinter import *

root = Tk()
root.title('나도 GUI') # 창 제목
root.geometry('640x480') # 가로 * 세로 크기 지정

Label(root, text='메뉴를 선택하세요').pack()

rdbchk = IntVar() # 정수형으로 값을 받을 경우
btn_food1 = Radiobutton(root, text='햄버거', value=1, variable=rdbchk)
btn_food1.select()
btn_food1.pack()

btn_food2 = Radiobutton(root, text='치킨', value=2, variable=rdbchk)
btn_food2.pack()

btn_food3 = Radiobutton(root, text='피자', value=3, variable=rdbchk)
btn_food3.pack()

Label(root, text='음료를 선택하세요').pack()

rdbchk2 = StringVar() # 문자열로 값을 받을 경우
btn_drink1 = Radiobutton(root, text='콜라', value='콜라', variable=rdbchk2)
btn_drink1.select()
btn_drink1.pack()

btn_drink2 = Radiobutton(root, text='사이다', value='사이다', variable=rdbchk2)
btn_drink2.pack()

btn_drink3 = Radiobutton(root, text='제로', value='제로', variable=rdbchk2)
btn_drink3.pack()

def btncmd():
    print('음식: {}'.format(rdbchk.get())) # 1햄버거, 2치킨, 3피자
    print('음료: {}'.format(rdbchk2.get()))
    
btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop() # 창이 딛히지 않도록 해줌