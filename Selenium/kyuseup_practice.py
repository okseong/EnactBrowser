from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--disable-web-security') # flag 등록
# options.add_argument('--user-data-dir="C:/chrome"')
driver = webdriver.Chrome("C:/Users/신규섭/Downloads/chromedriver",chrome_options=options)


#자체 테스팅 페이지로 테스트
driver.get("http://localhost:3000/")
test = driver.find_element_by_xpath('/html/body/div/div/input')
test.send_keys("sad")
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))   #iframe으로 전환
loginid = driver.find_element_by_xpath('/html/body/div/main/section/div[1]/input')
loginid.send_keys("sad")



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

