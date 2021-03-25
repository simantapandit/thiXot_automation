from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

import selenium.webdriver.support.expected_conditions as ec
import os
#***************************login credentials********************************************************
import subprocess
import platform
import smtplib
import time
from tkinter import messagebox
from email.message import EmailMessage

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
    wait = WebDriverWait(driver, 600)
    wait.until(ec.visibility_of_element_located((By.ID, el)))

def reduce_wait_time_xml(cl):
    wait = WebDriverWait(driver, 600)
    wait.until(ec.presence_of_element_located((By.CLASS_NAME,cl)))

def save():
    print('Saving changes')
    driver.find_element_by_xpath('.//*[@id="id_save"]').click()

def ping_router():

    def ping_ip(current_ip_address):
        try:
            output = subprocess.check_output("ping -{} 1 {}".format('n' if platform.system().lower(
            ) == "windows" else 'c', current_ip_address), shell=True, universal_newlines=True)
            if 'unreachable' in output:
                return False
            else:
                return True
        except Exception:
            return False

    if __name__ == '__main__':
        times = 10
        router_ipadd = '192.168.0.1'
        for i in range(times):
            #for each in current_ip_address:
                if ping_ip(router_ipadd):
                    print(f"{router_ipadd} is connected")
                    break

                else:
                    print('Trying to connect', router_ipadd)
                    time.sleep(30)
                    print(f"{router_ipadd} is not reachable")




        else:
            #times == 6:
            print(f'Router cannot connect to the {router_ipadd}')
            print('Router looses the connection after  6 tries')
            quit()

def countdown(t):
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer,'',end='')

        time.sleep(3)
        t -= 1

# def email():
#    msg = EmailMessage()
#    msg['Subject'] = ("ThinXot : Robustel R3000-L4L Test result for R'NB"+ str(rnb.get()))
#    msg['From'] = 'no-reply@thinxtra.com'
#    msg['To'] = ['simanta100pandit@gmail.com']
#
#    msg.set_content('Please find the attached rest result')
#
#    # with open('logs.txt') as email:  # message.txt  is the file for the body parts
#    #    message = email.read()
#    #    msg.set_content(message)
#
#    with open('C:\\Users\\siman\\PycharmProjects\\pythonProject1\\logs .txt',
#              'rb') as file:  # actual attachment to be sent
#       file_data = file.read()
#       file_name = file.name
#       msg.add_attachment(file_data, maintype='application', subtype='txt', filename=file_name)
#       print(file_data)
#       print(file_name)
#    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
#       server.login('no-reply@thinxtra.com', 'mjdpvhovhxhprkhm')
#       server.send_message(msg)
#
#    print('The test is completed and the report has been emailed to', msg['To'], 'please check the report')
#
# rnb = input('Please insert the RNB:' )
ping_router()

driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
driver.get('http://192.168.0.1/auth/login.html')
#driver.get('http://10.6.20.50/auth/login.html')
#driver.maximize_window()

login()
firmware_version = driver.find_elements_by_id('id_system-firmware_version_full_row')
title = driver.find_element_by_xpath('.//*[@id="id_system-firmware_version_full_tip"]').text
value = driver.find_element_by_xpath('.//*[@id="id_system-firmware_version_full_val"]').text
print(title, value)

hardware_version = driver.find_elements_by_id('id_system-hardware_version_row')
title1 = driver.find_element_by_xpath('.//*[@id="id_system-hardware_version_tip"]').text
value1 = driver.find_element_by_xpath('.//*[@id="id_system-hardware_version_val"]').text
print(title1, value1)

if value1 == '1.2':
    if value == "3.0.25 (Rev 3273)":
        print("No frimware update requires")

    else:
        print('Updating frimware')
        driver.find_element_by_xpath('.//*[@id="id_nav_system_group"]').click()
        driver.find_element_by_xpath('.//*[@id="id_system_update_menu"]').click()
        time.sleep(25)
        driver.find_element(By.XPATH, "/html/body/div/div[4]/div/div[1]/div/form/div/ul/li[2]/span[1]/input").send_keys(
            'C:\\Users\\siman\\PycharmProjects\\pythonProject1\\firmware\\r3000-firmware-3.0.25.ruf')
        driver.find_element_by_id('id_input_file').click()
        print('firmware version uploading ')
        time.sleep(120)
        print('firmware updated')
        reboot_sure = driver.find_element_by_id('id_comfirm_yes').click()
        print('Rebooting......')
        time.sleep(180)


if value1 == '1.3':
    if value == "3.0.26 (Rev 3491)":
        print("No frimware update requires")

    else:
        print('Updating frimware')
        driver.find_element_by_xpath('.//*[@id="id_nav_system_group"]').click()
        driver.find_element_by_xpath('.//*[@id="id_system_update_menu"]').click()

        time.sleep(25)
        driver.find_element(By.XPATH, "/html/body/div/div[4]/div/div[1]/div/form/div/ul/li[2]/span[1]/input").send_keys(
            'C:\\Users\\siman\\PycharmProjects\\pythonProject1\\firmware\\r3000-firmware-3.0.26.ruf')
        driver.find_element_by_id('id_input_file').click()
        print('firmware version uploading ')
        time.sleep(120)
        print('frimware updated')
        reboot_sure = driver.find_element_by_id('id_comfirm_yes').click()
        print('Rebooting......')
        time.sleep(180)



login()

system = driver.find_element_by_id('id_nav_system_group').click()
time.sleep(3)
app_centre = driver.find_element(By.XPATH, '/html/body/div/div[2]/dl[6]/dd[3]').click()
# print('Removing non essential applications. please wait for 25secs')

reduce_wait_time("id_sdk-app_list_list")

# t= 25
# countdown(int(t))


#print( "count = ", count)



def robustvpn_update():
    driver.find_element_by_xpath(
        '/html/body/div/div[4]/div/div[1]/div[2]/form/div/ul/li[2]/span[1]/input').send_keys(
        'C:\\Users\\siman\\PycharmProjects\\pythonProject1\\applications\\RobustelVPN\\r3000-robustvpn-3.0.0.rpk')
    driver.find_element_by_id('id_input_file').click()
    reduce_wait_time("id_comfirm_no")
    driver.find_element_by_xpath('.//*[@id="id_comfirm_no"]').click()

def snmp_update():
    driver.find_element_by_xpath(
        '/html/body/div/div[4]/div/div[1]/div[2]/form/div/ul/li[2]/span[1]/input').send_keys(
        'C:\\Users\\siman\\PycharmProjects\\pythonProject1\\applications\\snmp\\r3000-snmp-3.0.0.rpk')
    driver.find_element_by_id('id_input_file').click()
    reduce_wait_time("id_comfirm_no")
    driver.find_element_by_xpath('.//*[@id="id_comfirm_no"]').click()

def rcms_update():
    driver.find_element_by_xpath(
        '/html/body/div/div[4]/div/div[1]/div[2]/form/div/ul/li[2]/span[1]/input').send_keys(
        'C:\\Users\\siman\\PycharmProjects\\pythonProject1\\applications\\rcms\\r3000-rcms-3.0.5-20201112064743.rpk')
    driver.find_element_by_id('id_input_file').click()
    reduce_wait_time("id_comfirm_no")
    driver.find_element_by_xpath('.//*[@id="id_comfirm_no"]').click()

def robustlink_update():
    driver.find_element_by_xpath('/html/body/div/div[4]/div/div[1]/div[2]/form/div/ul/li[2]/span[1]/input').send_keys(
        'C:\\Users\\siman\\PycharmProjects\\pythonProject1\\applications\\Robustlink\\r3000-robustlink-3.0.1.rpk')
    driver.find_element_by_id('id_input_file').click()
    reduce_wait_time("id_comfirm_no")
    driver.find_element_by_xpath('.//*[@id="id_comfirm_no"]').click()


def remove_apps():
    print(app_name, 'exist')
    print(app_name, 'removing. Please wait')
    rmv = './/*[@id="id_sdk-app_list_val_' + str(i) + '_del"]'
    driver.find_element_by_xpath(rmv).click()
    reduce_wait_time("id_comfirm_no")
    driver.find_element_by_xpath('.//*[@id="id_comfirm_no"]').click()
    time.sleep(10)
    print(app_name, 'removed')

count_remove = len(driver.find_elements_by_xpath('.//*[@id="id_sdk-app_list_list"]/div'))
count_rmv_apps = count_remove #4  ( 0,1,2,3)

for i in range(count_rmv_apps):
     try:
         element = './/*[@id="id_sdk-app_list-name_' + str(i) + '"]'
         app_name = driver.find_element_by_xpath(element).text
         if app_name == "data_guardv2":
             remove_apps()
             print(app_name, 'is removed')

         else:

             print('Non essential application address do not exist')
     except:
         print()
#"data_guardv2"

status = driver.find_element_by_xpath('.//*[@id="id_nav_status_group"]')
status.click()
system = driver.find_element_by_id('id_nav_system_group').click()
time.sleep(3)
app_centre = driver.find_element(By.XPATH, '/html/body/div/div[2]/dl[6]/dd[3]').click()
# print('Checking for the essential applications. please wait for 25secs')
reduce_wait_time("id_sdk-app_list_list")
count = len(driver.find_elements_by_xpath('.//*[@id="id_sdk-app_list_list"]/div'))
if count == 1:
    print('No applications exist.')
    print('Installing robustvpn ')
    robustvpn_update()
    print('robustvpn installed')

    print('Installing rcms')
    rcms_update()
    print('rcms installed')

    print('Installing snmp')
    snmp_update()
    print('snmp installed')

    print('Installing robustlink')
    robustlink_update()
    print('robustlink installed')

    print('All the applications are installed')


elif count == 2:
    print('Scannig for Applications')
    row1 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-id_1"]').text
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

        elif a1 == 'snmp':
            print("snmp exist")
            if a2 == "3.0.0":
                print("no upgrades is required for snmp")
            else:
                snmp_update()
                print("smnp Updated")

        elif a1 == 'rcms':
            print("rcms exist")
            if a2 == "3.0.5":
                print("no upgrade required for rcms")

            else:
                rcms_update()
                print("rcms Updated")

        elif a1 == 'robustlink':
            print("robustlink exist")
            if a2 == "3.0.1":
                print("no upgrade required for robustlink")

            else:
                robustlink_update()
                print("robustlink Updated")
        else:
            print('Updating other required applications')

    print('Installing other required applications')
    if a1 != 'robustlink':
        print('Installing robustlink ')
        robustlink_update()
        print('robustlink installed ')

    if a1 != 'rcms':
        print('Installing rcms')
        rcms_update()
        print('rcms installed')

    if a1 != 'snmp':
        print('Installing snmp')
        snmp_update()
        print('snmp installed')

    if a1 != 'robustvpn':
        print('Installing robustvpn')
        robustvpn_update()
        print('robustvpn installed')

    else:
        print('All the applications are Installed')

elif count == 3:
    print('Scanning for Applications')
    row1 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-id_1"]').text
    r1 = driver.find_elements_by_xpath('.//*[@id="id_sdk-app_list_val_1"]')
    a1 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-name_1"]').text
    a2 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-version_1"]').text
    a3 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-status_1"]').text
    a4 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-description_1"]').text
    print(a1, a2, a3, a4)

    row2 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-id_2"]').text
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

        elif a1 == 'snmp':
            print("snmp exist")
            if a2 == "3.0.0":
                print("no upgrades is required for snmp")
            else:
                snmp_update()
                print("smnp Updated")

        elif a1 == 'rcms':
            print("rcms exist")
            if a2 == "3.0.5":
                print("no upgrade required for rcms")

            else:
                rcms_update()
                print("rcms Updated")

        elif a1 == 'robustlink':
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

        elif b1 == 'snmp':
            print("snmp exist")
            if b2 == "3.0.0":
                print("no upgrades is required for snmp")
            else:
                snmp_update()
                print("smnp Updated")

        elif b1 == 'rcms':
            print("rcms exist")
            if b2 == "3.0.5":
                print("no upgrade required for rcms")

            else:
                rcms_update()
                print("rcms Updated")

        elif b1 == 'robustlink':
            print("robustlink exist")
            if b2 == "3.0.1":
                print("no upgrade required for robustlink")

            else:
                robustlink_update()
                print("robustlink Updated")
        else:
            print('Updating other required applications')

    if a1 != 'robustlink' and b1 != 'robustlink':
        print('Installing robustlink')
        robustlink_update()
        print('robustlink installed ')


    if a1 != 'rcms' and b1 != 'rcms':
        print('Installing rcms')
        rcms_update()
        print('rcms installed')


    if a1 != 'snmp' and b1 != 'snmp':
        print('Installing snmp')
        snmp_update()
        print('snmp installed')


    if a1 != 'robustvpn' and b1 != 'robustvpn':
        print('Installing robustvpn')
        robustvpn_update()
        print('robustvpn installed')


    else:
        print('All the applications are installed')


elif count == 4:
    print('Scanning for Applications')
    row1 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-id_1"]').text
    r1 = driver.find_elements_by_xpath('.//*[@id="id_sdk-app_list_val_1"]')
    a1 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-name_1"]').text
    a2 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-version_1"]').text
    a3 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-status_1"]').text
    a4 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-description_1"]').text
    print(a1, a2, a3, a4)



    row2 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-id_2"]').text
    r2 = driver.find_elements_by_xpath('.//*[@id="id_sdk-app_list_val_2"]')
    b1 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-name_2"]').text
    b2 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-version_2"]').text
    b3 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-status_2"]').text
    b4 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-description_2"]').text
    print(b1, b2, b3, b4)

    row3 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-id_3"]').text
    c1 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-name_3"]').text
    c2 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-version_3"]').text
    c3 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-status_3"]').text
    c4 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-description_3"]').text
    print(c1, c2, c3, c4)
    print('Installing other required ')

    if row1 == "1":
        if a1 == "robustvpn":
            print("Robustvpn exist")
            if a2 == "3.0.0":
                print("no upgrades is required for robustVPN")

            else:
                robustvpn_update()
                print('RobustVPN is updated')

        elif a1 == 'snmp':
            print("snmp exist")
            if a2 == "3.0.0":
                print("no upgrades is required for snmp")
            else:
                snmp_update()
                print("smnp Updated")

        elif a1 == 'rcms':
            print("rcms exist")
            if a2 == "3.0.5":
                print("no upgrade required for rcms")

            else:
                rcms_update()
                print("rcms Updated")

        elif a1 == 'robustlink':
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

        elif b1 == 'snmp':
            print("snmp exist")
            if b2 == "3.0.0":
                print("no upgrades is required for snmp")
            else:
                snmp_update()
                print("smnp Updated")

        elif b1 == 'rcms':
            print("rcms exist")
            if b2 == "3.0.5":
                print("no upgrade required for rcms")

            else:
                rcms_update()
                print("rcms Updated")

        elif b1 == 'robustlink':
            print("robustlink exist")
            if b2 == "3.0.1":
                print("no upgrade required for robustlink")

            else:
                robustlink_update()
                print("robustlink Updated")
        else:
            print('Updating other required applications')

    if row3 == "3":
        if c1 == "robustvpn":
            print("Robustvpn exist")
            if c2 == "3.0.0":
                print("no upgrades is required for robustVPN")

            else:
                robustvpn_update()
                print('RobustVPN is updated')

        elif c1 == 'snmp':
            print("snmp exist")
            if c2 == "3.0.0":
                print("no upgrades is required for snmp")
            else:
                snmp_update()
                print("smnp Updated")

        elif c1 == 'rcms':
            print("rcms exist")
            if c2 == "3.0.5":
                print("no upgrade required for rcms")

            else:
                rcms_update()
                print("rcms Updated")

        elif c1 == 'robustlink':
            print("robustlink exist")
            if c2 == "3.0.1":
                print("no upgrade required for robustlink")

            else:
                robustlink_update()
                print("robustlink Updated")
        else:
            print('Updating other required applications')



    if a1 != 'robustlink' and b1 != 'robustlink' and c1 != 'robustlink':
        print('Installing robustlink')
        robustlink_update()
        print('robustlink installed ')

    elif a1 != 'rcms' and b1 != 'rcms'and c1 != 'rcms':
        print('Installing rcms')
        rcms_update()
        print('rcms installed')


    elif a1 != 'snmp' and b1 != 'snmp' and c1 != 'snmp':
        print('Installing snmp')
        snmp_update()
        print('snmp installed')


    elif a1 != 'robustvpn' and b1 != 'robustvpn' and c1 != 'robustvpn':
        print('Installing robustvpn')
        robustvpn_update()
        print('robustvpn installed')






elif count == 5:
    print('Scanning for applications')

    row1 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-id_1"]').text
    r1 = driver.find_elements_by_xpath('.//*[@id="id_sdk-app_list_val_1"]')
    a1 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-name_1"]').text
    a2 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-version_1"]').text
    a3 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-status_1"]').text
    a4 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-description_1"]').text
    print(a1, a2, a3, a4)

    row2 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-id_2"]').text
    r2 = driver.find_elements_by_xpath('.//*[@id="id_sdk-app_list_val_2"]')
    b1 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-name_2"]').text
    b2 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-version_2"]').text
    b3 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-status_2"]').text
    b4 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-description_2"]').text
    print(b1, b2, b3, b4)

    row3 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-id_3"]').text
    c1 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-name_3"]').text
    c2 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-version_3"]').text
    c3 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-status_3"]').text
    c4 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-description_3"]').text
    print(c1, c2, c3, c4)

    row4 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-id_4"]').text
    d1 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-name_4"]').text
    d2 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-version_4"]').text
    d3 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-status_4"]').text
    d4 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-description_4"]').text
    print(d1, d2, d3, d4)
    if row1 == "1":
        if a1 == "robustvpn":
            print("Robustvpn exist")
            if a2 == "3.0.0":
                print("no upgrades is required for robustVPN")

            else:
                robustvpn_update()
                print('RobustVPN is updated')

        elif a1 == 'snmp':
            print("snmp exist")
            if a2 == "3.0.0":
                print("no upgrades is required for snmp")
            else:
                snmp_update()
                print("smnp Updated")

        elif a1 == 'rcms':
            print("rcms exist")
            if a2 == "3.0.5":
                print("no upgrade required for rcms")

            else:
                rcms_update()
                print("rcms Updated")

        elif a1 == 'robustlink':
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

        elif b1 == 'snmp':
            print("snmp exist")
            if b2 == "3.0.0":
                print("no upgrades is required for snmp")
            else:
                snmp_update()
                print("smnp Updated")

        elif b1 == 'rcms':
            print("rcms exist")
            if b2 == "3.0.5":
                print("no upgrade required for rcms")

            else:
                rcms_update()
                print("rcms Updated")

        elif b1 == 'robustlink':
            print("robustlink exist")
            if b2 == "3.0.1":
                print("no upgrade required for robustlink")

            else:
                robustlink_update()
                print("robustlink Updated")
        else:
            print('Updating other required applications')


    if row3 == "3":
        if c1 == "robustvpn":
            print("Robustvpn exist")
            if c2 == "3.0.0":
                print("no upgrades is required for robustVPN")

            else:
                robustvpn_update()
                print('RobustVPN is updated')

        elif c1 == 'snmp':
            print("snmp exist")
            if c2 == "3.0.0":
                print("no upgrades is required for snmp")
            else:
                snmp_update()
                print("smnp Updated")

        elif c1 == 'rcms':
            print("rcms exist")
            if c2 == "3.0.5":
                print("no upgrade required for rcms")

            else:
                rcms_update()
                print("rcms Updated")

        elif c1 == 'robustlink':
            print("robustlink exist")
            if c2 == "3.0.1":
                print("no upgrade required for robustlink")

            else:
                robustlink_update()
                print("robustlink Updated")
        else:
            print('Updating other required applications')

    if row4 == "4":
        if d1 == "robustvpn":
            print("Robustvpn exist")
            if d2 == "3.0.0":
                print("no upgrades is required for robustVPN")

            else:
                robustvpn_update()
                print('RobustVPN is updated')

        elif d1 == 'snmp':
            print("snmp exist")
            if d2 == "3.0.0":
                print("no upgrades is required for snmp")
            else:
                snmp_update()
                print("smnp Updated")

        elif d1 == 'rcms':
            print("rcms exist")
            if d2 == "3.0.5":
                print("no upgrade required for rcms")

            else:
                rcms_update()
                print("rcms Updated")

        elif d1 == 'robustlink':
            print("robustlink exist")
            if d2 == "3.0.1":
                print("no upgrade required for robustlink")

            else:
                robustlink_update()
                print("robustlink Updated")
        else:
            print('Checking for other required applications')

    if a1 != 'robustlink' and b1 != 'robustlink' and c1 != 'robustlink'and d1 != 'robustlink':
        print('Installing robustlink')
        robustlink_update()
        print('robustlink installed ')

    elif a1 != 'rcms' and b1 != 'rcms'and c1 != 'rcms' and d1 != 'rcms':
        print('Installing rcms')
        rcms_update()
        print('rcms installed')


    elif a1 != 'snmp' and b1 != 'snmp' and c1 != 'snmp'and d1 != 'snmp':
        print('Installing snmp')
        snmp_update()
        print('snmp installed')


    elif a1 != 'robustvpn' and b1 != 'robustvpn' and c1 != 'robustvpn'and d1 != 'robustvpn':
        print('Installing robustvpn')
        robustvpn_update()
        print('robustvpn installed')


elif count == 6:
    print('Scanning for applications')

    row1 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-id_1"]').text
    r1 = driver.find_elements_by_xpath('.//*[@id="id_sdk-app_list_val_1"]')
    a1 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-name_1"]').text
    a2 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-version_1"]').text
    a3 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-status_1"]').text
    a4 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-description_1"]').text
    print(a1, a2, a3, a4)

    row2 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-id_2"]').text
    r2 = driver.find_elements_by_xpath('.//*[@id="id_sdk-app_list_val_2"]')
    b1 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-name_2"]').text
    b2 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-version_2"]').text
    b3 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-status_2"]').text
    b4 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-description_2"]').text
    print(b1, b2, b3, b4)

    row3 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-id_3"]').text
    c1 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-name_3"]').text
    c2 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-version_3"]').text
    c3 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-status_3"]').text
    c4 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-description_3"]').text
    print(c1, c2, c3, c4)

    row4 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-id_4"]').text
    d1 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-name_4"]').text
    d2 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-version_4"]').text
    d3 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-status_4"]').text
    d4 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-description_4"]').text
    print(d1, d2, d3, d4)


    row5 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-id_5"]').text
    e1 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-name_5"]').text
    e2 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-version_5"]').text
    e3 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-status_5"]').text
    e4 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-description_5"]').text
    print(e1, e2, e3, e4)

    if row1 == "1":
        if a1 == "robustvpn":
            print("Robustvpn exist")
            if a2 == "3.0.0":
                print("no upgrades is required for robustVPN")

            else:
                robustvpn_update()
                print('RobustVPN is updated')

        elif a1 == 'snmp':
            print("snmp exist")
            if a2 == "3.0.0":
                print("no upgrades is required for snmp")
            else:
                snmp_update()
                print("smnp Updated")

        elif a1 == 'rcms':
            print("rcms exist")
            if a2 == "3.0.5":
                print("no upgrade required for rcms")

            else:
                rcms_update()
                print("rcms Updated")

        elif a1 == 'robustlink':
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

        elif b1 == 'snmp':
            print("snmp exist")
            if b2 == "3.0.0":
                print("no upgrades is required for snmp")
            else:
                snmp_update()
                print("smnp Updated")

        elif b1 == 'rcms':
            print("rcms exist")
            if b2 == "3.0.5":
                print("no upgrade required for rcms")

            else:
                rcms_update()
                print("rcms Updated")

        elif b1 == 'robustlink':
            print("robustlink exist")
            if b2 == "3.0.1":
                print("no upgrade required for robustlink")

            else:
                robustlink_update()
                print("robustlink Updated")
        else:
            print('Updating other required applications')


    if row3 == "3":
        if c1 == "robustvpn":
            print("Robustvpn exist")
            if c2 == "3.0.0":
                print("no upgrades is required for robustVPN")

            else:
                robustvpn_update()
                print('RobustVPN is updated')

        elif c1 == 'snmp':
            print("snmp exist")
            if c2 == "3.0.0":
                print("no upgrades is required for snmp")
            else:
                snmp_update()
                print("smnp Updated")

        elif c1 == 'rcms':
            print("rcms exist")
            if c2 == "3.0.5":
                print("no upgrade required for rcms")

            else:
                rcms_update()
                print("rcms Updated")

        elif c1 == 'robustlink':
            print("robustlink exist")
            if c2 == "3.0.1":
                print("no upgrade required for robustlink")

            else:
                robustlink_update()
                print("robustlink Updated")
        else:
            print('Updating other required applications')

    if row4 == "4":
        if d1 == "robustvpn":
            print("Robustvpn exist")
            if d2 == "3.0.0":
                print("no upgrades is required for robustVPN")

            else:
                robustvpn_update()
                print('RobustVPN is updated')

        elif d1 == 'snmp':
            print("snmp exist")
            if d2 == "3.0.0":
                print("no upgrades is required for snmp")
            else:
                snmp_update()
                print("smnp Updated")

        elif d1 == 'rcms':
            print("rcms exist")
            if d2 == "3.0.5":
                print("no upgrade required for rcms")

            else:
                rcms_update()
                print("rcms Updated")

        elif d1 == 'robustlink':
            print("robustlink exist")
            if d2 == "3.0.1":
                print("no upgrade required for robustlink")

            else:
                robustlink_update()
                print("robustlink Updated")
        else:
            print('Checking for other required applications')

    if row5 == "5":
        if e1 == "robustvpn":
            print("Robustvpn exist")
            if e2 == "3.0.0":
                print("no upgrades is required for robustVPN")

            else:
                robustvpn_update()
                print('RobustVPN is updated')

        elif e1 == 'snmp':
            print("snmp exist")
            if e2 == "3.0.0":
                print("no upgrades is required for snmp")
            else:
                snmp_update()
                print("smnp Updated")

        elif e1 == 'rcms':
            print("rcms exist")
            if e2 == "3.0.5":
                print("no upgrade required for rcms")

            else:
                rcms_update()
                print("rcms Updated")

        elif e1 == 'robustlink':
            print("robustlink exist")
            if e2 == "3.0.1":
                print("no upgrade required for robustlink")

            else:
                robustlink_update()
                print("robustlink Updated")
        else:
            print('Updating other required applications')

    if a1 != 'robustlink' and b1 != 'robustlink' and c1 != 'robustlink' and d1 != 'robustlink' and e1 != 'robustlink':
        print('Installing robustlink')
        robustlink_update()
        print('robustlink installed ')

    elif a1 != 'rcms' and b1 != 'rcms' and c1 != 'rcms' and d1 != 'rcms' and e1 != 'rcms':
        print('Installing rcms')
        rcms_update()
        print('rcms installed')


    elif a1 != 'snmp' and b1 != 'snmp' and c1 != 'snmp' and d1 != 'snmp'and e1 != 'snmp':
        print('Installing snmp')
        snmp_update()
        print('snmp installed')


    elif a1 != 'robustvpn' and b1 != 'robustvpn' and c1 != 'robustvpn' and d1 != 'robustvpn' and e1 != 'robustvpn':
        print('Installing robustvpn')
        robustvpn_update()
        print('robustvpn installed')




else:
    print('No applications upgrade required. All the applications are up to date')


def reboot():
    reboot = driver.find_element_by_id('id_reboot').click()

    reboot_sure = driver.find_element_by_id('id_comfirm_yes')
    reboot_sure.click()
    print('Rebooting')
    reduce_wait_time('id_username_val')
    #time.sleep(180)

status = driver.find_element_by_xpath('.//*[@id="id_nav_status_group"]')
status.click()
reduce_wait_time('id_system-hardware_version_row')
hardware_version = driver.find_elements_by_id('id_system-hardware_version_row')
value1 = driver.find_element_by_xpath('.//*[@id="id_system-hardware_version_val"]').text


if value1 == '1.3':
    system = driver.find_element_by_id('id_nav_system_group').click()
    time.sleep(5)
    profile = driver.find_element_by_xpath('.//*[@id="id_system_profile_menu"]').click()
    time.sleep(2)
    driver.find_elements_by_class_name('rbt_checkbox')
    driver.find_element_by_xpath('.//*[@id="id_profile-import_ignore_invalid_row"]/ul/li[2]/span/div').click()
    driver.find_elements_by_id('id_profile-import_ignore_invalid_val')
    on_off = driver.find_element_by_xpath(
        './/*[@id="id_profile-import_ignore_invalid_row"]/ul/li[2]/span/div/span').text
    print('ignore Invalid Settings ', on_off)
    print('Installing configuration file')
    driver.find_element_by_xpath('.//*[@id="id_import_xml_file_val"]').send_keys(
        'C:\\Users\\siman\\PycharmProjects\\pythonProject1\\configuration files\\config3.0.26_lite_AU_Optus_v1.xml')
    driver.find_element_by_xpath('.//*[@id="id_import_xml_file_form"]/div/ul/li[2]/span[2]/input').click()
    reduce_wait_time_xml('xubox_layer')
    save()
    print('Please wait while the configuration file is updating......')
    #reduce_wait_time('id_username_val')
    time.sleep(360)
    #reboot()


elif value1 == '1.2':
    system = driver.find_element_by_id('id_nav_system_group').click()
    time.sleep(5)
    profile = driver.find_element_by_xpath('.//*[@id="id_system_profile_menu"]').click()
    time.sleep(2)
    driver.find_elements_by_class_name('rbt_checkbox')
    driver.find_element_by_xpath('.//*[@id="id_profile-import_ignore_invalid_row"]/ul/li[2]/span/div').click()
    driver.find_elements_by_id('id_profile-import_ignore_invalid_val')
    on_off = driver.find_element_by_xpath(
        './/*[@id="id_profile-import_ignore_invalid_row"]/ul/li[2]/span/div/span').text
    print('ignore Invalid Settings ', on_off)
    print('Installing configuration file')
    driver.find_element_by_xpath('.//*[@id="id_import_xml_file_val"]').send_keys(
        'C:\\Users\\siman\\PycharmProjects\\pythonProject1\\configuration files\\config3.0.25_lite_AU_Optus_Telstra_v1.xml')
    driver.find_element_by_xpath('.//*[@id="id_import_xml_file_form"]/div/ul/li[2]/span[2]/input').click()
    reduce_wait_time_xml('xubox_layer')
    save()
    print('Please wait while the configuration file is updating......')
    time.sleep(360)
    #reduce_wait_time('id_username_val')
    #reboot()

else:
    print(' Configuration file already exist. No update required  ')
    reduce_wait_time_xml('xubox_layer')
    save()
    print('Please wait while the configuration file is updating......')
    time.sleep(360)
    #reduce_wait_time('id_username_val')

    #reboot()


driver.quit()


print('Lets validate the  configurations ')
os.system('simcardcheck.py')