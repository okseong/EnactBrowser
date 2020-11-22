from selenium import webdriver
import tkinter
from time import sleep


window=tkinter.Tk()

def start():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--disable-web-security') # flag 등록
    # options.add_argument('--user-data-dir="C:/chrome"')
    driver = webdriver.Chrome("C:/Users/신규섭/Downloads/chromedriver",chrome_options=options)
    driver.get("http://localhost:3000/")
    testbtn1 = driver.find_element_by_xpath('/html/body/div/div/button[1]')
    testbtn1.click()
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))   #iframe으로 전환
    checkbtn1 =  driver.find_element_by_id("fromparent")
    errorimage = tkinter.PhotoImage(file="error.png")
    errorcount = 0
    if checkbtn1 :
        errorcount+=1
        textlabel = tkinter.Label(window, text = '부모사이트에서 자식사이트에 새로운 element 생성 가능') # 라벨 위젯
        #imagelabel = tkinter.Label(window,image=errorimage, width=5)
        textlabel.pack() # 위젯 위치를 적당한 곳에 위치시킨다.(auto)
        #imagelabel.grid(column=1,row=1)
        #print("dsadad")
    else:
        textlabel = tkinter.Label(window, text = '부모사이트에서 새로운 element 생성 불가능') # 라벨 위젯
        #imagelabel = tkinter.Label(window,image=errorimage, width=5)
        textlabel.pack() # 위젯 위치를 적당한 곳에 위치시킨다.(auto)
    testbtn2 =  driver.find_element_by_id("child_testbtn1")
    testbtn2.click()
    driver.switch_to.parent_frame()
    sleep(0.1)
    alert = driver.switch_to.alert

    if alert:
        errorcount+=1
        textlabel = tkinter.Label(window, text = '자식사이트에서 부모사이트에 스크립트 실행 가능') # 라벨 위젯
        textlabel.pack() 
        alert.dismiss()
        driver.refresh()
    else:
        textlabel = tkinter.Label(window, text = '자식사이트에서 부모사이트에 스크립트 실행 불가능') # 라벨 위젯
        textlabel.pack() 
    
    
    driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))   #iframe으로 전환
    testbtn3 =  driver.find_element_by_id("child_testbtn2")
    testbtn3.click()
    driver.switch_to.parent_frame()
    sleep(0.1)
    checkbtn2=driver.find_element_by_id("fromchild")
    if checkbtn2 :
        errorcount+=1
        textlabel = tkinter.Label(window, text = '자식사이트에서 부모사이트에 새로운 element 생성 가능') # 라벨 위젯
        #imagelabel = tkinter.Label(window,image=errorimage, width=5)
        textlabel.pack() # 위젯 위치를 적당한 곳에 위치시킨다.(auto)
        #imagelabel.grid(column=1,row=1)
        #print("dsadad")
    else:
        textlabel = tkinter.Label(window, text = '자식사이트에서 부모사이트에 새로운 element 생성 불가능') # 라벨 위젯
        #imagelabel = tkinter.Label(window,image=errorimage, width=5)
        textlabel.pack() # 위젯 위치를 적당한 곳에 위치시킨다.(auto)
    resultlabel = tkinter.Label(window,font=("ariel",15),fg="red" ,text = '총' + str(errorcount) +"개의 취약점 발견") # 라벨 위젯
    resultlabel.pack() 





window.geometry("400x200")
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

