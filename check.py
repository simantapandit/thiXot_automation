from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
import string

driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
driver.get('http://192.168.0.1/auth/login.html')
#driver.minimize_window()


def login():
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

    try:
        if get_title == 'Router Web Manager':
            driver.find_element_by_id('id_username_val').send_keys(username)
            driver.find_element_by_id('id_password_val').send_keys(pass2)
            driver.find_element_by_id('id_login').click()

    except:
        print()

    try:
        if get_title == 'Router Web Manager':
            driver.find_element_by_id('id_username_val').send_keys(username)
            driver.find_element_by_id('id_password_val').send_keys(pass3)
            driver.find_element_by_id('id_login').click()

    except:
        print()

    else:
        print('Please contact your network Admin')


login()


print('Please validate the saved configurations')
print()
driver.find_elements_by_xpath('.//*[@id="id_system-device_model_row"]')
dev = driver.find_element_by_xpath('.//*[@id="id_system-device_model_val"]').text
print('Device Model=', dev )

firmware_version = driver.find_elements_by_id('id_system-firmware_version_full_row')
title = driver.find_element_by_xpath('.//*[@id="id_system-firmware_version_full_tip"]').text
value = driver.find_element_by_xpath('.//*[@id="id_system-firmware_version_full_val"]').text
print(title, value)

hardware_version = driver.find_elements_by_id('id_system-hardware_version_row')
title1 = driver.find_element_by_xpath('.//*[@id="id_system-hardware_version_tip"]').text
value1 = driver.find_element_by_xpath('.//*[@id="id_system-hardware_version_val"]').text
print(title1, value1)

serail = driver.find_element_by_xpath('.//*[@id="id_system-serial_number_val"]').text
print("Serial Number =", serail)

active_link = driver.find_element_by_xpath('.//*[@id="id_active_link-desc_val"]').text
print("Active Link =", active_link)

interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
time.sleep(2)
link_manager = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_menu"]/span[1]').click()
time.sleep(2)
link_status = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_status_tab"]').click()
A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
#ptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
#p1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
print(A1, 'is', link1)

A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
#uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
#ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
print(A2, 'is', link2)

counter = 6
for i in range(counter):
    if link1 =='Connected':
        print('The router is connected back to the SIM1')
        print('Please check the configurations')
        driver.find_element_by_xpath('.//*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
        time.sleep(1)
        driver.find_element_by_xpath('.//*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
        time.sleep(2)

        driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
        model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
        print('Modem Model =', model_status)

        iccid1 = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
        print(' SIM1 ICCID =', iccid1)
        iccid = iccid1.replace('F')

        imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
        print('SIM1 IMEI =', imei)

        Network_provider = driver.find_element_by_xpath('.//*[@id="id_cellular-status-operator_1"]').text
        print('SIM1 Network Provider =', Network_provider)

        network_type = driver.find_element_by_xpath('.//*[@id="id_cellular-status-network_type_1"]').text
        print('SIM1 Network type =', network_type)

        signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
        print('Signal Strength using SIM1  =', signal_strength)
        time.sleep(2)

        print('Router can Switch back to SIM1 after SIM2 has been deactivated')
        break

    else:
        print('SIM1 hasnot been connected')
        print('Waiting on SIM1 to be active. Please wait 2 minutes')
        time.sleep(2)
        print("")








