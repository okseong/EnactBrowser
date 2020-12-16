from selenium import webdriver
import tkinter
from time import sleep
import smtplib
from datetime import datetime
import threading
from email.mime.text import MIMEText
import time



window=tkinter.Tk()
def start():
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login('robinshins674@gmail.com', 'cvvisaucrucbcvwu')
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    #options.add_argument('--disable-web-security') # flag 등록
    # options.add_argument('--user-data-dir="C:/chrome"')
    driver = webdriver.Chrome("C:/dev/chromedriver.exe",chrome_options=options)
    driver.get("https://enactparent.web.app")
    checkbtn1 =  driver.find_element_by_id("parent_dom")
    checkbtn1.click()
    sleep(0.1)
    result1 =  driver.find_element_by_xpath("/html/body/div/div[1]/div/p[2]")
    errorimage = tkinter.PhotoImage(file="error.png")
    errorcount = 0
    log = ""
    print(result1.text)
    if result1.text == '실패' :
        errorcount+=1
        log = log + "\n" + "부모사이트에서 자식사이트 dom 접근 가능"
        textlabel = tkinter.Label(window, text = '부모사이트에서 자식사이트 dom 접근 가능') # 라벨 위젯
        #imagelabel = tkinter.Label(window,image=errorimage, width=5)
        textlabel.pack() # 위젯 위치를 적당한 곳에 위치시킨다.(auto)

    else:
        log = log + "\n" + "부모사이트에서 자식사이트 dom 접근 불가능"
        textlabel = tkinter.Label(window, text = '부모사이트에서 자식사이트 dom 접근 불가능') # 라벨 위젯
        #imagelabel = tkinter.Label(window,image=errorimage, width=5)
        textlabel.pack() # 위젯 위치를 적당한 곳에 위치시킨다.(auto)
    testbtn2 =  driver.find_element_by_id("parent_xml")
    testbtn2.click()
    sleep(0.1)
    result2 =  driver.find_element_by_xpath("/html/body/div/div[1]/div/p[4]")
    # driver.switch_to.parent_frame()
   

    if result2.text == '실패':
        errorcount+=1
        log = log + "\n" + "부모사이트에서 자식사이트로 XMLHttpRequest 가능"
        textlabel = tkinter.Label(window, text = '부모사이트에서 자식사이트로 XMLHttpRequest 가능') # 라벨 위젯
        textlabel.pack() 
    else:
        log = log + "\n" + "부모사이트에서 자식사이트로 XMLHttpRequest 불가능"
        textlabel = tkinter.Label(window, text = '부모사이트에서 자식사이트로 XMLHttpRequest 불가능') # 라벨 위젯
        textlabel.pack() 

    testbtn3 =  driver.find_element_by_id("parent_cookie")
    testbtn3.click()
    sleep(0.1)
    result3 =  driver.find_element_by_xpath("/html/body/div/div[1]/div/p[6]")
    

    if result3.text == '실패':
        errorcount+=1
        log = log + "\n" + "부모사이트에서 자식사이트의 cookie 접근 가능"
        textlabel = tkinter.Label(window, text = '부모사이트에서 자식사이트의 cookie 접근 가능') # 라벨 위젯
        textlabel.pack() 
    else:
        log = log + "\n" + "부모사이트에서 자식사이트의 cookie 접근 불가능"
        textlabel = tkinter.Label(window, text = '부모사이트에서 자식사이트의 cookie 접근 불가능') # 라벨 위젯
        textlabel.pack() 
    
    testbtn4 =  driver.find_element_by_id("parent_xss")
    testbtn4.click()
    sleep(0.1)
    result4 =  driver.find_element_by_xpath("/html/body/div/div[1]/div/p[8]")
    

    if result4.text == '실패':
        errorcount+=1
        log = log + "\n" + "부모사이트에서 자식사이트로 XSS 공격 가능"
        textlabel = tkinter.Label(window, text = '부모사이트에서 자식사이트로 XSS 공격 가능') # 라벨 위젯
        textlabel.pack() 
    else:
        log = log + "\n" + "부모사이트에서 자식사이트로 XSS 공격 불가능"
        textlabel = tkinter.Label(window, text = '부모사이트에서 자식사이트로 XSS 공격 불가능') # 라벨 위젯
        textlabel.pack() 
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))   #iframe으로 전환
    checkbtn5 =  driver.find_element_by_id("child_dom")
    checkbtn5.click()
    sleep(0.1)
    result5 =  driver.find_element_by_xpath("/html/body/div/div/p[1]")
    errorimage = tkinter.PhotoImage(file="error.png")
    if result5.text == '실패' :
        errorcount+=1
        log = log + "\n" + "자식사이트에서 부모사이트 dom 접근 가능"
        textlabel = tkinter.Label(window, text = '자식사이트에서 부모사이트 dom 접근 가능') # 라벨 위젯
        textlabel.pack() # 위젯 위치를 적당한 곳에 위치시킨다.(auto)

    else:
        log = log + "\n" + "자식사이트에서 부모사이트 dom 접근 불가능"
        textlabel = tkinter.Label(window, text = '자식사이트에서 부모사이트 dom 접근 불가능') # 라벨 위젯
        #imagelabel = tkinter.Label(window,image=errorimage, width=5)
        textlabel.pack() # 위젯 위치를 적당한 곳에 위치시킨다.(auto)
    testbtn6 =  driver.find_element_by_id("child_xml")
    testbtn6.click()
    sleep(0.1)
    result6 =  driver.find_element_by_xpath("/html/body/div/div/p[3]")
    # driver.switch_to.parent_frame()
  

    if result6.text == '실패':
        errorcount = errorcount +1
        print(errorcount)
        log = log + "\n" + "부모사이트에서 자식사이트로 XMLHttpRequest 가능"
        textlabel = tkinter.Label(window, text = '부모사이트에서 자식사이트로 XMLHttpRequest 가능') # 라벨 위젯
        textlabel.pack() 
    else:
        log = log + "\n" + "부모사이트에서 자식사이트로 XMLHttpRequest 불가능"
        textlabel = tkinter.Label(window, text = '부모사이트에서 자식사이트로 XMLHttpRequest 불가능') # 라벨 위젯
        textlabel.pack() 

    testbtn7 =  driver.find_element_by_id("child_cookie")
    testbtn7.click()
    sleep(0.1)
    result7 =  driver.find_element_by_xpath("/html/body/div/div/p[5]")
  

    if result7.text == '실패':
        errorcount = errorcount +1
        log = log + "\n" + "자식사이트에서 부모사이트의 cookie 접근 가능"
        textlabel = tkinter.Label(window, text = '자식사이트에서 부모사이트의 cookie 접근 가능') # 라벨 위젯
        textlabel.pack() 
    else:
        log = log + "\n" + "자식사이트에서 부모사이트의 cookie 접근 불가능"
        textlabel = tkinter.Label(window, text = '자식사이트에서 부모사이트의 cookie 접근 불가능') # 라벨 위젯
        textlabel.pack() 
    
    testbtn8 =  driver.find_element_by_id("child_xss")
    testbtn8.click()
    sleep(0.1)
    result8 =  driver.find_element_by_xpath("/html/body/div/div/p[7]")
    

    if result8.text == '실패':
        errorcount+=1
        log = log + "\n" + "부모사이트에서 자식사이트로 XSS 공격 가능"
        textlabel = tkinter.Label(window, text = '부모사이트에서 자식사이트로 XSS 공격 가능') # 라벨 위젯
        textlabel.pack() 
    else:
        log = log + "\n" + "부모사이트에서 자식사이트로 XSS 공격 불가능"
        textlabel = tkinter.Label(window, text = '부모사이트에서 자식사이트로 XSS 공격 불가능') # 라벨 위젯
        textlabel.pack() 


    resultlabel = tkinter.Label(window,font=("ariel",15),fg="red" ,text = '총' + str(errorcount) +"개의 취약점 발견") # 라벨 위젯
    resultlabel.pack() 
    msg = MIMEText('검사결과 총 ' + str(errorcount) + "개의 취약점이 발견되었습니다." + '\n' +"\n" +"*상세로그" +"\n" +log)
    msg['Subject'] = str(datetime.today()) +'날짜의 브라우저 보안취약점 검사 결과입니다.'
    s.sendmail("robinshins674@gmail.com", "robinshins674@gmail.com", msg.as_string())
    s.quit()
    textlabel = tkinter.Label(window, text = '결과를 메일로 발송했습니다!') # 라벨 위젯
    textlabel.pack() 
    sleep(1)
    threading.Timer(5, start).start()





window.geometry("400x800")
window.title("Enact 보안 점검")
button = tkinter.Button(window, text="점검시작", command=start)
button.pack()


window.mainloop()

















#자체 테스팅 페이지로 테스트

# loginid = driver.find_element_by_xpath('/html/body/div/main/section/div[1]/input')
# loginid.send_keys("sad")



# iframe이 많은 w3schools로 테스트
# driver.get("https://www.w3schools.com/html/html_iframe.asp")   
# iframe = driver.find_element_by_tag_name("iframe")
# loginBtn = driver.find_element_by_xpath('/html/body/div[1]/div[1]/a')
# #driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))   
# loginBtn.click()
# #driver.close()




# iframe으로 이루어진 경마사이트로 테스트
# driver.get("http://www.krj.co.kr/")   
#driver.switch_to.frame("krjmain")    # krjmain Frame으로 스위칭 
#popup = driver.find_element_by_class_name("popupwin")
# input_id = driver.find_element_by_name("userid")   # ID 입력창 
# input_pw = driver.find_element_by_name("password") # PW 입력창 
# login_btn = driver.find_element_by_name("image")   # Login 버튼 
 
# input_id.send_keys("__ID__")                      # ID 엘리먼트에 입력 
# input_pw.send_keys("__PW__")                      # PW 엘리먼트에 입력 
# login_btn.click()                                 # Login 버튼 클릭 





# 탭간 변경 테스팅
# driver.get("https://google.com")

# driver.title # 'Google'

# # Get parent window
# parent_window = driver.current_window_handle 

# # Open "Bing" page in child window
# driver.execute_script("window.open('https://bing.com')") 

# # Get list of all windows currently opened (parent + child)
# all_windows = driver.window_handles 
# print(all_windows)

# # Get child window
# child_window = [window for window in all_windows if window != parent_window][0] 
# print(child_window)


# # Switch to child window
# driver.switch_to.window(child_window) 

# driver.title # 'Bing'

# # Close child window
# #driver.close() 

# # Switch back to parent window
# driver.switch_to.window(parent_window) 

# driver.title # 'Google'

