import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pyperclip

#네이버 자동 로그인
url="https://nid.naver.com/nidlogin.login?mode=form&url=https://www.naver.com/"
options = Options()
options.add_experimental_option("excludeSwitches",["enable-automation"])
driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get(url)
time.sleep(25)

#네이버 아이디 비밀번호
#user_id='id'
#user_pw='pw'

#네이버 아이디 입력
#log_ID=driver.find_element(by=By.ID,value="id_line")
#log_ID.click()
#pyperclip.copy(user_id)
#log_ID.send_keys(Keys.CONTROL,'v')
#time.sleep(3)

#네이버 비밀번호 입력
#log_PID=driver.find_element(by=By.ID,value="pw_line")
#log_PID.click()
#pyperclip.copy(user_pw)
#log_PID.send_keys(Keys.CONTROL,'v')
#time.sleep(3)

#로그인 클릭
#log_ENT=driver.find_element(by=By.ID,value="log.login")
#log_ENT.click()
#time.sleep(40)