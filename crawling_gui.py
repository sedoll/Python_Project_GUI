# 메세지 박스
from ast import ExceptHandler
import tkinter.messagebox as msgbox
import pyperclip
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from random import randrange as rd
from tkinter import *

root = Tk()
root.title('네이버 뉴스 라이브러리 크롤링 프로그램') # 창 제목
root.geometry('640x480') # 가로 * 세로 크기 지정

# 딜레이 시간
t_min = 3
t_max = 5

#입력 내용
input_id = ''
input_pw = ''
input_content = ''
input_syear = 1920
input_eyear = 1999
input_page = 1

def clipboard_input(browser, user_xpath, user_input): # 아이디, 비밀번호를 입력받기 위한 함수
    temp_user_input = pyperclip.paste()  # 사용자 클립보드를 따로 저장

    pyperclip.copy(user_input)
    browser.find_element("xpath", user_xpath).click()
    ActionChains(browser).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

    pyperclip.copy(temp_user_input)  # 사용자 클립보드에 저장 된 내용을 다시 가져 옴
    time.sleep(rd(t_min, t_max))
        
def webCrawling(uid, upw, search, pages, syear, eyear):
    
    filename = '학교 학과 공지사항 스크래핑.csv'
    f = open(filename, 'w', encoding='utf-8-sig', newline='') # newline은 자동 줄바꿈을 없애주기 위해 사용
    writer = csv.writer(f)
    
    options = webdriver.ChromeOptions()
    # options.headless = True # 웹페이지가 보이지 않고 프로그램 실행
    # options.add_argument("winddow-size=1920x1080") # 웹페이지 크기를 FHD로 설정
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36")

    str = ''
    
    p = 1
    url = f'https://newslibrary.naver.com/search/searchDetails.naver#%7B%22mode%22%3A1%2C%22sort%22%3A0%2C%22trans%22%3A%221%22%2C%22pageSize%22%3A10%2C%22keyword%22%3A%22{search}%22%2C%22startDate%22%3A%22{syear}-01-01%22%2C%22endDate%22%3A%22{eyear}-12-31%22%2C%22status%22%3A%22success%22%2C%22page%22%3A{p}%2C%22office%22%3A%22111111%22%2C%22pageno%22%3A%2210%22%2C%22section%22%3A%22111111111%22%2C%22type%22%3A%22111111111111111111111111111%22%2C%22scope%22%3A%2210%22%7D'
    browser = webdriver.Chrome('C:/j/chromedriver.exe', options=options)
    browser.get(url)

    b_id = uid
    b_pw = upw

    # 아이디, 비밀번호 입력
    clipboard_input(browser, '//*[@id="id"]', b_id)
    clipboard_input(browser, '//*[@id="pw"]', b_pw)
    browser.find_element(By.XPATH, '//*[@id="log.login"]').click()

    if pages > 1:
        for page in range(p, pages+1):
            url = f'https://newslibrary.naver.com/search/searchDetails.naver#%7B%22mode%22%3A1%2C%22sort%22%3A0%2C%22trans%22%3A%221%22%2C%22pageSize%22%3A10%2C%22keyword%22%3A%22{search}%22%2C%22startDate%22%3A%22{syear}-01-01%22%2C%22endDate%22%3A%22{eyear}-12-31%22%2C%22status%22%3A%22success%22%2C%22page%22%3A{page}%2C%22office%22%3A%22111111%22%2C%22pageno%22%3A%2210%22%2C%22section%22%3A%22111111111%22%2C%22type%22%3A%22111111111111111111111111111%22%2C%22scope%22%3A%2210%22%7D'
            browser.get(url)
            time.sleep(rd(t_min, t_max))
            contents = browser.find_elements(By.CLASS_NAME, 'data')
            print(str(page) + '페이지')
            for content in contents:
                # writer.writerow(content.text)
                # writer.writerow(content.find_element(By.TAG_NAME, 'a').get_attribute('href') + '\n')
                print(content.text)
                print(content.find_element(By.TAG_NAME, 'a').get_attribute('href') + '\n')

    else:
        time.sleep(rd(t_min, t_max))
        contents = browser.find_elements(By.CLASS_NAME, 'data')
        for content in contents:
                print(content.text)
                print(content.find_element(By.TAG_NAME, 'a').get_attribute('href') + '\n')
                # writer.writerow(content.text)
                # writer.writerow(content.find_element(By.TAG_NAME, 'a').get_attribute('href') + '\n')

    print('크롤링 완료')
    browser.quit()

def btncmd():
    global input_id, input_pw, input_content, input_syear, input_eyear, input_page
    try:
        if 20 >= len(text_id.get()) >= 5 and 16 >= len(text_pw.get()) >= 8 and int(text_eyear.get()) >= int(text_syear.get()) >= 1920 and int(text_eyear.get()) <= 1999 and int(text_page.get()) >= 1: 
            input_id = text_id.get()
            input_pw = text_pw.get()
            input_content = text_content.get()
            input_syear = int(text_syear.get())
            input_eyear = int(text_eyear.get())
            input_page = int(text_page.get())
            webCrawling(input_id, input_pw, input_content, input_page, input_syear, input_eyear)
        else:
            msgbox.showerror("에러", "아이디 또는 비밀번호가 잘 못 입력 되었습니다. \n아이디는 5~20자 \n비밀번호는 8~16자 입니다.")
    except Exception:
        msgbox.showerror('에러', '연도 혹은 페이지가 숫자 형식이 아닙니다.')
    finally:
        pass

# 아이디 입력
label_id = Label(root, text='아이디') # 레이블에 글자 출력
label_id.place(x=10, y=10, width=50, height=20)
text_id = Entry(root)
text_id.place(x=70, y=10, width=150, height=20)

# 비밀번호 입력
label_pw = Label(root, text='비밀번호') # 레이블에 글자 출력
label_pw.place(x=10, y=40,  width=50, height=20)
text_pw = Entry(root, width=30, show='*')
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
text_syear.insert(0, input_syear)
text_syear.place(x=70, y=100, width=150, height=20)

# 끝 연도
label_eyear = Label(root, text='끝 연도') # 레이블에 글자 출력
label_eyear.place(x=10, y=130,  width=50, height=20)
text_eyear = Entry(root, width=30)
text_eyear.insert(0, input_eyear)
text_eyear.place(x=70, y=130, width=150, height=20)

# 페이지
label_page = Label(root, text='페이지') # 레이블에 글자 출력
label_page.place(x=10, y=160,  width=50, height=20)
text_page = Entry(root, width=30)
text_page.insert(0, input_page)
text_page.place(x=70, y=160, width=150, height=20)

btn = Button(root, text='입력', command=btncmd)
btn.place(x=10, y=200, width=80, height=40)

root.resizable(width=False, height=False) # 창 크기 조절 불가
root.mainloop() # 창이 딛히지 않도록 해줌
root.quit() # gui 창이 종료되면 프로세스 종료