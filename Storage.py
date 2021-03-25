from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#***************************login credentials********************************************************

username = "admin"
pass1 = "admin"
pass2 = "thinxtra"
pass3 = "S8ThaCGBPjcqq2L42NYhlQ=="
#*******************************************************connecting to Interface **********************************

driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
driver.get('http://192.168.0.1/auth/login.html')
driver.maximize_window()

#**********************************Login logic for Multiple users **************************************************

get_title = driver.title
print("welcome to Robustel ", get_title)
if get_title=='Router Web Manager':
    driver.find_element_by_id('id_username_val').send_keys(username)
    driver.find_element_by_id('id_password_val').send_keys(pass1)
    driver.find_element_by_id('id_login').click()
    print("authenticating credentials")
    print('Logged In as admin')
    #driver.quit()


if get_title == 'Router Web Manager':
    driver.find_element_by_id('id_username_val').send_keys(username)
    driver.find_element_by_id('id_password_val').send_keys(pass2)
    driver.find_element_by_id('id_login').click()
    #driver.quit()

else:
    driver.find_element_by_id('id_username_val').send_keys(username)
    driver.find_element_by_id('id_password_val').send_keys(pass3)
    driver.find_element_by_id('id_login').click()
    # driver.quit()
#*********************************************Capture the variables****************************************************

firmware_version = driver.find_elements_by_id('id_system-firmware_version_full_row')

for fm in firmware_version:
   title = fm.find_element_by_xpath('.//*[@id="id_system-firmware_version_full_tip"]').text
   value = fm.find_element_by_xpath('.//*[@id="id_system-firmware_version_full_val"]').text
   print(title, value)


   if value == "3.0.25 (Rev 3273)" :
       print("No upgrades required")

   else:
       driver.find_element_by_id('id_nav_system_group').click()
       driver.find_element_by_id('id_system_update_menu').click()
       print('waiting 25seconds for the element before interacting')
       time.sleep(25)
       driver.find_element(By.XPATH, "/html/body/div/div[4]/div/div[1]/div/form/div/ul/li[2]/span[1]/input").send_keys('C:\\Users\\siman\\PycharmProjects\\pythonProject1\\r3000-firmware-3.0.25.ruf')
       driver.find_element_by_id('id_input_file').click()
       print('firmware version uploading ')
       time.sleep(100)
       print('uploaded')
       reboot_sure = driver.find_element_by_id('id_comfirm_yes').click()

hardware_version = driver.find_elements_by_id('id_system-hardware_version_row')

for hv in hardware_version:
   title1 = hv.find_element_by_xpath('.//*[@id="id_system-hardware_version_tip"]').text
   value1 = hv.find_element_by_xpath('.//*[@id="id_system-hardware_version_val"]').text
   print(title1, value1)


system = driver.find_element_by_id('id_nav_system_group').click()
time.sleep(3)
app_centre = driver.find_element(By.XPATH, '/html/body/div/div[2]/dl[6]/dd[3]').click()
print('Checking for the required applications. please wait for 25secs')
time.sleep(25)



count = len(driver.find_elements_by_xpath('.//*[@id="id_sdk-app_list_list"]/div'))
print(count)


def robustvpn_update():
    driver.find_element_by_xpath(
        '/html/body/div/div[4]/div/div[1]/div[2]/form/div/ul/li[2]/span[1]/input').send_keys(
        'C:\\Users\\siman\\PycharmProjects\\pythonProject1\\applications\\RobustelVPN\\r3000-robustvpn-3.0.0.rpk')
    driver.find_element_by_id('id_input_file').click()
    time.sleep(10)
    driver.find_element_by_xpath('.//*[@id="id_comfirm_no"]').click()

def snmp_update():
    driver.find_element_by_xpath(
        '/html/body/div/div[4]/div/div[1]/div[2]/form/div/ul/li[2]/span[1]/input').send_keys(
        'C:\\Users\\siman\\PycharmProjects\\pythonProject1\\applications\\snmp\\r3000-snmp-3.0.2.rpk')
    driver.find_element_by_id('id_input_file').click()
    time.sleep(10)
    driver.find_element_by_xpath('.//*[@id="id_comfirm_no"]').click()

def rcms_update():
    driver.find_element_by_xpath(
        '/html/body/div/div[4]/div/div[1]/div[2]/form/div/ul/li[2]/span[1]/input').send_keys(
        'C:\\Users\\siman\\PycharmProjects\\pythonProject1\\applications\\rcms\\r3000-rcms-3.0.5-20201112064743.rpk')
    driver.find_element_by_id('id_input_file').click()
    time.sleep(10)
    driver.find_element_by_xpath('.//*[@id="id_comfirm_no"]').click()

def robustlink_update():
    driver.find_element_by_xpath('/html/body/div/div[4]/div/div[1]/div[2]/form/div/ul/li[2]/span[1]/input').send_keys(
        'C:\\Users\\siman\\PycharmProjects\\pythonProject1\\applications\\Robustlink\\r3000-robustlink-3.0.1.rpk')
    driver.find_element_by_id('id_input_file').click()
    time.sleep(10)
    driver.find_element_by_xpath('.//*[@id="id_comfirm_no"]').click()

if count == 1:
    robustvpn_update()
    rcms_update()
    snmp_update()
    robustlink_update()

if count == 2:
    row1 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-id_1"]').text
    print(row1)
    r1 = driver.find_elements_by_xpath('.//*[@id="id_sdk-app_list_val_1"]')
    a1 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-name_1"]').text
    a2 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-version_1"]').text
    a3 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-status_1"]').text
    a4 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-description_1"]').text
    print(a1, a2, a3, a4)

    if row1 == "1":
        if a1 == "robustvpn":
            print("Robustvpn exist")
            if a2 == "3.0.0":
                print("no upgrades is required for robustVPN")

            else:
                robustvpn_update()
                print('RobustVPN is updated')

        if a1 == 'snmp':
            print("snmp exist")
            if a2 == "3.0.2":
                print("no upgrades is required for snmp")
            else:
                snmp_update()
                print("smnp Updated")

        if a1 == 'rcms':
            print("rcms exist")
            if a2 == "3.0.5":
                print("no upgrade required for rcms")

            else:
                rcms_update()
                print("rcms Updated")

        if a1 == 'robustlink':
            print("robustlink exist")
            if a2 == "3.0.1":
                print("no upgrade required for robustlink")

            else:
                robustlink_update()
                print("robustlink Updated")
        else:
            print('Updating other required applications')

    if a1 == 'robustlink':
        rcms_update()
        snmp_update()
        robustvpn_update()

    if a1 == 'robustvpn':
        rcms_update()
        snmp_update()
        robustlink_update()

    if a1 == 'snmp':
        rcms_update()
        robustlink_update()
        robustvpn_update()


if count == 3:
    row1 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-id_1"]').text
    print(row1)
    r1 = driver.find_elements_by_xpath('.//*[@id="id_sdk-app_list_val_1"]')
    a1 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-name_1"]').text
    a2 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-version_1"]').text
    a3 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-status_1"]').text
    a4 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-description_1"]').text
    print(a1, a2, a3, a4)

    row2 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-id_2"]').text
    print(row2)
    r2 = driver.find_elements_by_xpath('.//*[@id="id_sdk-app_list_val_2"]')
    b1 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-name_2"]').text
    b2 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-version_2"]').text
    b3 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-status_2"]').text
    b4 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-description_2"]').text

    if row1 == "1":
        if a1 == "robustvpn":
            print("Robustvpn exist")
            if a2 == "3.0.0":
                print("no upgrades is required for robustVPN")

            else:
                robustvpn_update()
                print('RobustVPN is updated')

        if a1 == 'snmp':
            print("snmp exist")
            if a2 == "3.0.2":
                print("no upgrades is required for snmp")
            else:
                snmp_update()
                print("smnp Updated")

        if a1 == 'rcms':
            print("rcms exist")
            if a2 == "3.0.5":
                print("no upgrade required for rcms")

            else:
                rcms_update()
                print("rcms Updated")

        if a1 == 'robustlink':
            print("robustlink exist")
            if a2 == "3.0.1":
                print("no upgrade required for robustlink")

            else:
                robustlink_update()
                print("robustlink Updated")
        else:
            print('Updating other required applications')

    if row2 == "2":
        if b1 == "robustvpn":
            print("Robustvpn exist")
            if b2 == "3.0.0":
                print("no upgrades is required for robustVPN")

            else:
                robustvpn_update()
                print('RobustVPN is updated')

        if b1 == 'snmp':
            print("snmp exist")
            if b2 == "3.0.2":
                print("no upgrades is required for snmp")
            else:
                snmp_update()
                print("smnp Updated")

        if b1 == 'rcms':
            print("rcms exist")
            if b2 == "3.0.5":
                print("no upgrade required for rcms")

            else:
                rcms_update()
                print("rcms Updated")

        if b1 == 'robustlink':
            print("robustlink exist")
            if b2 == "3.0.1":
                print("no upgrade required for robustlink")

            else:
                robustlink_update()
                print("robustlink Updated")
        else:
            print('Updating other required applications')


    if a1 == 'robustlink':
        rcms_update()
        snmp_update()
        robustvpn_update()

    if a1 == 'robustvpn':
        rcms_update()
        snmp_update()
        robustlink_update()

    if a1 == 'snmp':
        rcms_update()
        robustlink_update()
        robustvpn_update()

    else:
        print('All the applications are up to date')
else:
    print('done')




#row2 = driver.find_elements_by_xpath('.//*[@id="id_sdk-app_list_val_1"]')
#row1 = driver.find_elements_by_xpath('.//*[@id="id_sdk-app_list_tip"]')
#index1 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-id_1"]').text
#print(index1)

#index = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-id"]').text
#print(index)



#if index == "1":
 #   if a1 == "robustvpn":
  #      print("Robustvpn exist")
   #     if a2 == "3.0.0":
    #        print("no upgrades is required for robustVPN")
     #   else:
      #      driver.find_element_by_xpath('/html/body/div/div[4]/div/div[1]/div[2]/form/div/ul/li[2]/span[1]/input').send_keys('C:\\Users\\siman\\PycharmProjects\\pythonProject1\\applications\\RobustelVPN\\r3000-robustvpn-3.0.0.rpk')
       #     driver.find_element_by_id('id_input_file').click()
        #    time.sleep(10)
         #   driver.find_element_by_xpath('.//*[@id="id_comfirm_no"]').click()
#
 #   if a1 == 'snmp':
  #      print("snmp exist")
   #     if a2 == "3.0.2":
    #        print("no upgrades is required for snmp")
     #   else:
      #      driver.find_element_by_xpath('/html/body/div/div[4]/div/div[1]/div[2]/form/div/ul/li[2]/span[1]/input').send_keys('C:\\Users\\siman\\PycharmProjects\\pythonProject1\\applications\\snmp\\r3000-snmp-3.0.2.rpk')
       #     driver.find_element_by_id('id_input_file').click()
        #    time.sleep(10)
         #   driver.find_element_by_xpath('.//*[@id="id_comfirm_no"]').click()
#
 #   if a1 == 'rcms':
  #      print("rcms exist")
   #     if a2 == "3.0.5":
    #        print("no upgrade required for rcms")
#
 #       else:
  #         driver.find_element_by_xpath('/html/body/div/div[4]/div/div[1]/div[2]/form/div/ul/li[2]/span[1]/input').send_keys('C:\\Users\\siman\\PycharmProjects\\pythonProject1\\applications\\rcms\\r3000-rcms-3.0.5-20201112064743.rpk')
   #         driver.find_element_by_id('id_input_file').click()
    #        time.sleep(10)
     #       driver.find_element_by_xpath('.//*[@id="id_comfirm_no"]').click()
      #      print('rcms is updated to 3.0.5')
#
 #   if a1 == 'robustlink':
  #      print("robustlink exist")
   ##        print("no upgrade required for robustlink")
#
 ##          driver.find_element_by_xpath('/html/body/div/div[4]/div/div[1]/div[2]/form/div/ul/li[2]/span[1]/input').send_keys('C:\\Users\\siman\\PycharmProjects\\pythonProject1\\applications\\Robustlink\\r3000-robustlink-3.0.1.rpk')
   #         driver.find_element_by_id('id_input_file').click()
    ##       driver.find_element_by_xpath('.//*[@id="id_comfirm_no"]').click()
    #else:
     #   print('All the applications are up to date')
#
#if index != 'Index':
#
 #       # robust VPN update
  #      driver.find_element_by_xpath('/html/body/div/div[4]/div/div[1]/div[2]/form/div/ul/li[2]/span[1]/input').send_keys('C:\\Users\\siman\\PycharmProjects\\pythonProject1\\applications\\RobustelVPN\\r3000-robustvpn-3.0.0.rpk')
   #     driver.find_element_by_id('id_input_file').click()
    #    time.sleep(10)
     #   driver.find_element_by_xpath('.//*[@id="id_comfirm_no"]').click()
#
 #       #   #rcms update
  #      driver.find_element_by_xpath('/html/body/div/div[4]/div/div[1]/div[2]/form/div/ul/li[2]/span[1]/input').send_keys('C:\\Users\\siman\\PycharmProjects\\pythonProject1\\applications\\rcms\\r3000-rcms-3.0.5-20201112064743.rpk')
   #     driver.find_element_by_id('id_input_file').click()
    #    time.sleep(10)
     #   driver.find_element_by_xpath('.//*[@id="id_comfirm_no"]').click()
      ###driver.find_element_by_xpath('/html/body/div/div[4]/div/div[1]/div[2]/form/div/ul/li[2]/span[1]/input').send_keys('C:\\Users\\siman\\PycharmProjects\\pythonProject1\\applications\\snmp\\r3000-snmp-3.0.2.rpk')
      #  driver.find_element_by_id('id_input_file').click()
       # time.sleep(10)
        #driver.find_element_by_xpath('.//*[@id="id_comfirm_no"]').click()

        # robustlink update
       # driver.find_element_by_xpath('/html/body/div/div[4]/div/div[1]/div[2]/form/div/ul/li[2]/span[1]/input').send_keys('C:\\Users\\siman\\PycharmProjects\\pythonProject1\\applications\\Robustlink\\r3000-robustlink-3.0.1.rpk')
        #driver.find_element_by_id('id_input_file').click()
        #time.sleep(10)
        #driver.find_element_by_xpath('.//*[@id="id_comfirm_no"]').click()


#else:
 #   print('done')

# drafts  stored :

    if a1 == 'robustlink':
        rcms_update()
        snmp_update()
        robustvpn_update()

    elif a1 == 'robustvpn':
        rcms_update()
        snmp_update()
        robustlink_update()

    elif a1 == 'snmp':
        rcms_update()
        robustlink_update()
        robustvpn_update()

    elif a1 == 'rcms':
        snmp_update()
        robustlink_update()
        robustvpn_update()

    if b1 == 'robustlink':
        rcms_update()
        snmp_update()
        robustvpn_update()

    elif b1 == 'robustvpn':
        rcms_update()
        snmp_update()
        robustlink_update()

    elif b1 == 'snmp':
        rcms_update()
        robustlink_update()
        robustvpn_update()

    elif b1 == 'rcms':
        snmp_update()
        robustlink_update()
        robustvpn_update()
    if c1 == 'robustlink':
        rcms_update()
        snmp_update()
        robustvpn_update()

    elif c1 == 'robustvpn':
        rcms_update()
        snmp_update()
        robustlink_update()

    elif c1 == 'snmp':
        rcms_update()
        robustlink_update()
        robustvpn_update()

    elif c1 == 'rcms':
        snmp_update()
        robustlink_update()
        robustvpn_update()

    if d1 == 'robustlink':
        rcms_update()
        snmp_update()
        robustvpn_update()

    elif d1 == 'robustvpn':
        rcms_update()
        snmp_update()
        robustlink_update()

    elif d1 == 'snmp':
        rcms_update()
        robustlink_update()
        robustvpn_update()

    elif d1 == 'rcms':
        snmp_update()
        robustlink_update()
        robustvpn_update()
    else:
        print('All the applications are up to date')




#****************************************
    if c == 'rcms':
        snmp_update()
        robustlink_update()
        robustvpn_update()

    if b1 == 'robustlink':
        rcms_update()
        snmp_update()
        robustvpn_update()

    if b1 == 'robustvpn':
        rcms_update()
        snmp_update()
        robustlink_update()

    if b1 == 'snmp':
        rcms_update()
        robustlink_update()
        robustvpn_update()

    if b1 == 'rcms':
        snmp_update()
        robustlink_update()
        robustvpn_update()
    if c1 == 'robustlink':
        rcms_update()
        snmp_update()
        robustvpn_update()

    if c1 == 'robustvpn':
        rcms_update()
        snmp_update()
        robustlink_update()

    if c1 == 'snmp':
        rcms_update()
        robustlink_update()
        robustvpn_update()

    if c1 == 'rcms':
        snmp_update()
        robustlink_update()
        robustvpn_update()
    else:
        print('All the applications are up to date')



#@@@@@@@login@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#logins

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#***************************login credentials********************************************************

driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
driver.get('http://192.168.0.1/auth/login.html')
driver.maximize_window()
get_title = driver.title


username = "admin"





# for i in password:
#      print(i)
#      driver.find_element_by_id('id_password_val').send_keys(i)
#      driver.find_element_by_id('id_login').click()
#
#
#      #driver.set_page_load_timeout(5)
#      dev= driver.find_element_by_xpath('.//*[@id="id_system-device_model_val"]').text
#      print(dev)
#      if dev == "R3000-L4L":
#          break
#
#     #status = await login()
driver.find_element_by_id('id_username_val').send_keys(username)
password = ["admin", "thinxtra", "S8ThaCGBPjcqq2L42NYhlQ=="]
for i in password:
    print(i)
    driver.find_element_by_id('id_password_val').send_keys(i)
    driver.find_element_by_id('id_login').click()
    #driver.set_page_load_timeout(5)
    dev = driver.find_element_by_xpath('.//*[@id="id_system-device_model_val"]').text
    print(dev)
    if dev == "R3000-L4L":
        break
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@romain@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

from future.moves import tkinter
from tkinter import *
from tkinter import ttk
import os
from tkinter.ttk import Progressbar
pop = Tk()
pop.geometry("600x400")
pop.title("ThiXtra TestBot")

label1 = Label (pop, text="Please enter the R'NB ", font = ('arial', 16,'bold')).pack()
e = Entry(pop, width=20, borderwidth = 2).pack()

#def save_rnb():
   # print("hello")

#button = Button(pop, text='submit', command= save_rnb()).pack()

progress = ttk.Progressbar(pop, style='TProgressbar',  orient=HORIZONTAL, length=500, mode='indeterminate')
progress.pack(pady=20)

def submit():
    progress.start(20)
    let = "Lets start testing Router"
    mylabel = Label(pop, text=let)
    mylabel.pack()
    os.system('robustel.py')

def stopprogram():
    progress.stop(20)
    #global pop
    quit()
label2 = Label (pop, text="Entire testing", font = ('arial', 16,'bold')).pack()

start =  Button(pop, text= "Start", command = submit)
start.pack()

stop = Button(pop, text= "Stop", command= stopprogram)
stop.pack(pady =20 )

label3 = Label (pop, text="Validate the configurations ", font = ('arial', 16,'bold')).pack(pady = 20)

def validate_config():
    os.system('validate.py')

start1 = Button(pop, text= "start", command= validate_config)
start1.pack()

pop.mainloop()





username = "admin"
driver.find_element_by_id('id_username_val').send_keys(username)

password = ["admin", "thinxtra", "S8ThaCGBPjcqq2L42NYhlQ=="]


#**********************************************



for i in password:
     print(i)
     driver.find_element_by_id('id_password_val').send_keys(i)
     driver.find_element_by_id('id_login').click()


     #driver.set_page_load_timeout(5)
     #dev= driver.find_element_by_xpath('.//*[@id="id_system-device_model_val"]').text
     #print(dev)
     #if dev == "R3000-L4L":
      #   break

    #status = await login()


from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#***************************login credentials********************************************************


username = 'admin'
password = ['admin','thinxtra']
#password = ["admin", "thinxtra", "S8ThaCGBPjcqq2L42NYhlQ=="]
# driver.set_page_load_timeout(5)

for i in password:
     print(i)
     driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
     driver.get('http://192.168.0.1/auth/login.html')
     #driver.maximize_window()
     driver.find_element_by_id('id_username_val').send_keys(username)
     driver.find_element_by_id('id_password_val').send_keys(i)
     driver.find_element_by_id('id_login').click()
     dev = driver.find_element_by_xpath('.//*[@id="id_system-device_model_tip"]').text
     print(dev)
     if dev == 'Device Model':
          break




from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
#***************************login credentials********************************************************

driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
driver.get('http://192.168.0.1/auth/login.html')
driver.maximize_window()


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



#driver.quit()


if get_title == 'Router Web Manager':
    driver.find_element_by_id('id_username_val').send_keys(username)
    driver.find_element_by_id('id_password_val').send_keys(pass2)
    driver.find_element_by_id('id_login').click()
    #driver.quit()

else:
    driver.find_element_by_id('id_username_val').send_keys(username)
    driver.find_element_by_id('id_password_val').send_keys(pass3)
    driver.find_element_by_id('id_login').click()
    # driver.quit()

#@@@@@@@@@@@@@@@@@@@@@@Connecting to sim card manager

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

print('Connecting to Optus SIM Card Manager')
driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
driver.get('https://optus.jasperwireless.com/provision/jsp/login.jsp;jsessionid=54954536A2F659DBD472B4CD880B5A75')
#driver.minimize_window()


username = "simanta"
password = "thinxtra"

driver.find_element_by_xpath('.//*[@id="j_username"]').send_keys(username)
driver.find_element_by_xpath('.//*[@id="j_password"]').send_keys(password)

driver.find_element_by_xpath('./html/body/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/input').click()

time.sleep(5)
driver.find_element_by_id('jw-searchfield-1021-inputEl').send_keys(iccid)
time.sleep(10)
driver.find_element_by_xpath('.//*[@id="jw-searchfield-1021-triggerWrap"]/tbody/tr/td[1]').click()



def conn():
    interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
    time.sleep(2)
    link_manager = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_menu"]/span[1]').click()
    time.sleep(2)
    link_status = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_status_tab"]').click()
    A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
    link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
    # ptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
    # p1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
    print(A1, 'is', link1)

    A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
    link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
    # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
    # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
    print(A2, 'is', link2)