# 메세지 박스
import tkinter.messagebox as msgbox
from tkinter import *

root = Tk()
root.title('웹 크롤링 GUI') # 창 제목
root.geometry('640x480') # 가로 * 세로 크기 지정

# 기차 예매 시스템
def info():
    msgbox.showinfo("알림", "정상적으로 예매 완료되었습니다.")

def warn():
    msgbox.showwarning("경고", "해당 좌석은 매진되었습니다.")

def error():
    msgbox.showerror("에러", "에러가 발생했습니다.")

def okcancel():
    i = msgbox.askokcancel("확인 / 취소", "해당 좌석은 유아동반석입니다. 예매하시겠습니까?")
    if i:
        print("유아 동반석을 예매하였습니다.")
    else:
        print("유아 동반석 예매가 취소되었습니다.")
        
def retrycancel():
    msgbox.askretrycancel("재시도 / 취소", "일시적인 오류 입니다. 다시 시도하시겠습니까?")

def yesno():
    msgbox.askyesno("예 / 아니오", "해당 좌석은 역방향 입니다. 예매하시겠습니까?")

def yesnocancel():
    response = msgbox.askyesnocancel("예 / 아니오 / 취소", "예매 내역이 저장되지 않았습니다. \n저장 후 프로그램을 종료하시겠습니까?")
    # 네 : 저장 후 종료 / True
    # 아니오 : 저장하지 않고 종료 / False
    # 취소 : 프로그램 종료 취소 (현재 화면에서 계속 작업) / None
    print("응답", response)
    if response == True:
        print("예")
    elif response == False:
        print("아니오")
    else:
        print("취소")
    
Button(root, command=info, text="알림").pack()
Button(root, command=warn, text="경고").pack()
Button(root, command=error, text="에러").pack()

Button(root, command=okcancel, text="확인 취소").pack()
Button(root, command=retrycancel, text="재시도 취소").pack()
Button(root, command=yesno, text="예 아니오").pack()
Button(root, command=yesnocancel, text="예 아니오 취소").pack()

root.mainloop() # 창이 딛히지 않도록 해줌