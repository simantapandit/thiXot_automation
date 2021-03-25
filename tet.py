from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import selenium.webdriver.support.expected_conditions as ec
import time
driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
driver.get('http://192.168.0.1/auth/login.html')
#driver.get('http://10.6.20.50/auth/login.html')
#driver.maximize_window()

def login():
    user = 'admin'
    pas = ('thinxtra', 'admin', "S8ThaCGBPjcqq2L42NYhlQ==",)

    try:
        for i in pas:
            driver.find_element_by_id('id_username_val').send_keys(user)
            driver.find_element_by_id('id_password_val').send_keys(i)
            driver.find_element_by_id('id_login').click()
    except:
        print()



def reduce_wait_time(el):

    wait = WebDriverWait(driver, 25)

    wait.until(ec.visibility_of_element_located((By.ID, el)))

login()
system = driver.find_element_by_id('id_nav_system_group').click()
time.sleep(3)
app_centre = driver.find_element(By.XPATH, '/html/body/div/div[2]/dl[6]/dd[3]').click()
print('Removing non essential applications. please wait for 25secs')

el = "id_sdk-app_list-status_4"
reduce_wait_time()



