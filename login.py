from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#***************************login credentials********************************************************

driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
driver.get('http://192.168.0.1/auth/login.html')
driver.maximize_window()
#driver.implicitly_wait(10)

username = "admin"
pass1 = "thinxtra"
pass2 = "admin"
pass3 = "S8ThaCGBPjcqq2L42NYhlQ=="

get_title = driver.title
print("welcome to Robustel ", get_title)
if get_title=='Router Web Manager':
    driver.find_element_by_id('id_username_val').send_keys(username)
    driver.find_element_by_id('id_password_val').send_keys(pass1)
    driver.find_element_by_id('id_login').click()


driver.execute_script("window.open('http://192.168.0.1/auth/login.html', 'tab2');")
driver.switch_to.window('tab2')
driver.get('http://192.168.0.1/auth/login.html')

get_title = driver.title
print("welcome to Robustel ", get_title)
if get_title=='Router Web Manager':
    driver.find_element_by_id('id_username_val').send_keys(username)
    driver.find_element_by_id('id_password_val').send_keys(pass2)
    driver.find_element_by_id('id_login').click()
