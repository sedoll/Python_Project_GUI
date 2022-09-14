from tkinter import *

root = Tk()
root.title('웹 크롤링 GUI') # 창 제목
root.geometry('640x480') # 가로 * 세로 크기 지정

def create_new_file():
    print("새 파일을 만듭니다.")

menu = Menu(root)

# file 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label="New FIle", command=create_new_file)
menu_file.add_command(label="New Window", command=create_new_file)
menu_file.add_separator() # 구분자
menu_file.add_command(label="Open File...")
menu_file.add_separator()
menu_file.add_command(label="Save All", state="disable") # 비 활성화
menu_file.add_command(label="Exit", command=root.quit)
menu.add_cascade(label="File", menu=menu_file)

# Edit 메뉴 
menu.add_cascade(label="Edit")

# Language 메뉴 추가 (radio 버튼)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label="Python")
menu_lang.add_radiobutton(label="Java")
menu_lang.add_radiobutton(label="C++")
menu.add_cascade(label="Language", menu=menu_lang)

# View 메뉴
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label="Show Minimap")
menu.add_cascade(label="View", menu=menu_view)

root.config(menu=menu)
root.mainloop() # 창이 딛히지 않도록 해줌