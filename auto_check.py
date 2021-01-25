import selenium
import schedule
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from pyperclip import copy

MyName = Mybirthday = MyPassWord = None


def init():
    global MyName
    global Mybirthday
    global MyPassWord

    MyName = input("이름: ")
    Mybirthday = input("생년월일: ")
    MyPassWord = input("패스워드: ")
    
def auto_check() -> None:
    global MyName
    global Mybirthday
    global MyPassWord

    URL = 'https://hcs.eduro.go.kr/#/loginHome'

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])

    driver = webdriver.Chrome(executable_path='C:\\Users\\user\\Downloads\\chromedriver_win32\\chromedriver.exe', options=options)
    driver.implicitly_wait(10)
    driver.get(url=URL)

    MainPage = driver.find_element_by_id("btnConfirm2")
    MainPage.click()

    schul_name_input = driver.find_element_by_id("schul_name_input")
    user_name_input = driver.find_element_by_id("user_name_input")
    birthday_input = driver.find_element_by_id("birthday_input")
    btnConfirm = driver.find_element_by_id("btnConfirm")

    schul_name_input.click()
    orgname = driver.find_element_by_id("orgname")
    orgname.click()

    layerFullBtn = driver.find_element_by_class_name("layerFullBtn")
    sidolabel = driver.find_element_by_id("sidolabel")
    crseScCode = driver.find_element_by_id("crseScCode")

    sidolabel.click()
    sido_select = Select(sidolabel)
    sido_select.select_by_visible_text('서울특별시')
    sido_select.select_by_value('01')

    crseScCode.click()
    crse_select  = Select(crseScCode)
    crse_select.select_by_visible_text('고등학교')

    crse_select.select_by_value('4')

    orgname.click()
    copy("세명컴퓨터고등학교")
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

    Search = driver.find_element_by_class_name("searchBtn")
    Search.click()

    layerSchoolArea = driver.find_element_by_class_name("layerSchoolArea")
    layerSchoolArea.click()
    time.sleep(0.5)
    checked = driver.execute_script(("return document.getElementsByClassName('layerSchoolArea')[0].getElementsByTagName('li')[0].getElementsByTagName('a')[0].click()"))
    layerFullBtn.click()

    user_name_input.click()
    copy(MyName)
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

    birthday_input.click()
    copy(Mybirthday)
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

    btnConfirm = driver.find_element_by_id('btnConfirm')
    btnConfirm.click()

    time.sleep(0.3)

    input_text_common = driver.find_element_by_class_name("input_text_common")
    input_text_common.click()

    copy(MyPassWord)
    ActionChains(driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()

    btnConfirm = driver.find_element_by_id("btnConfirm")
    btnConfirm.click()

    time.sleep(0.6)

    btnCheck = driver.find_element_by_class_name("btn")

    if btnCheck.text == "미참여":
        print('자가진단 시작')
        btnCheck.click()
        time.sleep(0.5)

        radioList = driver.find_elements_by_class_name("radioList")
        print(len(radioList))

        for i in range(1,len(radioList)+1):
            survey = driver.find_element_by_id(f"survey_q{i}a1")
            survey.click()

        btnConfirm = driver.find_element_by_id("btnConfirm")
        btnConfirm.click()
    else:
        print('이미 완료되었습니다. ')

    driver.quit()


init()

schedule.every().day.at("10:48").do(auto_check)

while True:
    schedule.run_pending()
    time.sleep(1)