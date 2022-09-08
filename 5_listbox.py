from tkinter import *

root = Tk()
root.title('나도 GUI') # 창 제목
root.geometry('640x480') # 가로 * 세로 크기 지정

# height는 리스트 값을 몇 개를 보여줄 건지 선택, 0이면 전체를 보여줌
listbox = Listbox(root, selectmode='extended', height=0) # 'single' 하나씩 선택 / 'extended' 여러개 선택
listbox.insert(0, '사과')
listbox.insert(1, '딸기')
listbox.insert(2, '바나나')
listbox.insert(END, '수박')
listbox.insert(END, '포도')
listbox.pack()

def btncmd():
    # listbox.delete(END) # 맨 뒤의 항목을 삭제
    listbox.delete(0) # 맨 앞의 항목을 삭제
    
    print(listbox.size()) # 리스트의 개수 확인
    
    if listbox.size() == 0: # 리스트의 개수가 0이면 종료
        root.quit()
        
    print(listbox.get(0, 2)) # 리스트 박스의 값 출력 
    
    print(listbox.curselection()) # 선택된 항목 출력
    
btn = Button(root, text='클릭', command=btncmd)
btn.pack()

root.mainloop() # 창이 딛히지 않도록 해줌