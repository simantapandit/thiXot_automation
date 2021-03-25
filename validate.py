from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os
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

def connect():
    driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
    driver.get('http://192.168.0.1/auth/login.html')
    time.sleep(5)
    login()
    driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click() #interface
    time.sleep(2)
    driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_menu"]/span[1]').click() #link manager
    time.sleep(2)
    driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_status_tab"]').click()  #link manager status
    A1= driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
    link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
    uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
    ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
    print(A1, 'is', link1, 'UpTime is ', uptime1, 'Ip Address', ip1  )

    A2= driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
    link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
    #uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
    #ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
    print(A2, 'is', link2)

    #link_status_click = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status_val_1"]').click()
    driver.find_element_by_xpath('.//*[@id="id_interface_cellular_menu"]/span[1]').click() #cellular
    time.sleep(1)
    driver.find_element_by_xpath('.//*[@id="id_interface_cellular_status_tab"]').click() #cellular status
    time.sleep(2)

    driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click() #B1
    model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
    print('Modem Model =', model_status)

    iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
    print('Active SIM ICCID =', iccid)


    imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
    print('Active SIM IMEI =', imei)

    Network_provider= driver.find_element_by_xpath('.//*[@id="id_cellular-status-operator_1"]').text
    print('Active Network Provider =', Network_provider)

    network_type =  driver.find_element_by_xpath('.//*[@id="id_cellular-status-network_type_1"]').text
    print('Active Network type =', network_type)

    signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
    print('Signal Strength  =', signal_strength)


    #*********************************************************************************
    #**********************connecting to Optus sim Manager*****************************************
    print('Connecting to Optus SIM Card Manager')
    driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
    driver.get('https://optus.jasperwireless.com/provision/jsp/login.jsp;jsessionid=54954536A2F659DBD472B4CD880B5A75')
    #driver.minimize_window()


    username = "simanta"
    password = "thinxtra"

    driver.find_element_by_xpath('.//*[@id="j_username"]').send_keys(username)
    driver.find_element_by_xpath('.//*[@id="j_password"]').send_keys(password)

    driver.find_element_by_xpath('./html/body/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/input[2]').click()

    time.sleep(5)
    driver.find_element_by_id('jw-searchfield-1021-inputEl').send_keys(iccid)
    driver.find_element_by_xpath('.//*[@id="jw-searchfield-1021-triggerWrap"]/tbody/tr/td[1]').click()
    time.sleep(10)



    driver.find_element_by_xpath('.//*[@id="ext-gen1284"]/div/a').click()
    time.sleep(10)

    driver.find_element_by_xpath('.//*[@id="jw-button-1027"]').click()
    time.sleep(10)

    driver.find_element_by_xpath('.//*[@id="3-inputEl"]').clear()
    time.sleep(5)
    element = driver.find_element_by_xpath('.//*[@id="3-inputEl"]').send_keys('Deactivate')
    time.sleep(5)
    driver.find_element_by_xpath('.//*[@id="jw-boundlist-1361-listEl"]/ul/li').click()

    driver.find_element_by_id('jw-button-1384-btnIconEl').click()

    time.sleep(10)
    print('sim1 has been deactivated')

    driver.quit()

    print('Connecting back to the Router interface')

    print('Waiting on SIM2 to be active. Please wait....... ')
    driver.find_element_by_id('id_reboot').click()
    reboot_sure = driver.find_element_by_id('id_comfirm_yes')
    reboot_sure.click()
    print('Rebooting')
    time.sleep(300)
    #os.system('validate2.py')
    driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
    driver.get('http://192.168.0.1/auth/login.html')
    # driver.minimize_window()

    username = "admin"
    pass1 = "thinxtra"
    pass2 = "admin"
    pass3 = "S8ThaCGBPjcqq2L42NYhlQ=="

    get_title = driver.title
    print("welcome to Robustel ", get_title)
    if get_title == 'Router Web Manager':
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

    active_link = driver.find_element_by_xpath('.//*[@id="id_active_link-desc_val"]').text
    print("Active Link =", active_link)

    if active_link == 'WWAN2':
        interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
        time.sleep(2)
        link_manager = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_menu"]/span[1]').click()
        time.sleep(2)
        link_status = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_status_tab"]').click()
        A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
        link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
        uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
        ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
        print(A1, 'is', link1, 'UpTime is ', uptime1, 'Ip Address', ip1)

        A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
        link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
        uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
        ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
        print(A2, 'is', link2, uptime2, ip2)

        cellular = driver.find_element_by_xpath('.//*[@id="id_interface_cellular_menu"]/span[1]').click()
        time.sleep(1)
        cellular_status = driver.find_element_by_xpath('.//*[@id="id_interface_cellular_status_tab"]').click()
        time.sleep(2)

        B1 = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()
        model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
        print('Modem Model =', model_status)

        iccid1 = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
        print('ICCID after deactivating SIM1 =', iccid1)

        imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
        print('IMEI after deactivating SIM1 =', imei)

        Network_provider = driver.find_element_by_xpath('.//*[@id="id_cellular-status-operator_1"]').text
        print('Network Provider after deactivating SIM1 =', Network_provider)

        network_type = driver.find_element_by_xpath('.//*[@id="id_cellular-status-network_type_1"]').text
        print('Network type after deactivating SIM1 =', network_type)

        signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
        print('Signal_Strength after deactivating SIM1 =', signal_strength)

        print('Activating SIM1 back on. Please wait......')

        print('Rebooting. Please wait.......')
        driver.find_element_by_id('id_reboot').click()
        reboot_sure = driver.find_element_by_id('id_comfirm_yes')
        reboot_sure.click()
        time.sleep(
            360)  # problem occured  after this line of code: the  router looses the  internet connection : solution: may be increse the time sleep until  5 mins

        print('Connecting to Optus SIM Card Manager again')
        driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
        driver.get(
            'https://optus.jasperwireless.com/provision/jsp/login.jsp;jsessionid=54954536A2F659DBD472B4CD880B5A75')
        # driver.minimize_window()

        username = "simanta"
        password = "thinxtra"

        driver.find_element_by_xpath('.//*[@id="j_username"]').send_keys(username)
        driver.find_element_by_xpath('.//*[@id="j_password"]').send_keys(password)

        driver.find_element_by_xpath(
            './html/body/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/input[2]').click()

        time.sleep(5)
        driver.find_element_by_id('jw-searchfield-1021-inputEl').send_keys(iccid)
        driver.find_element_by_xpath('.//*[@id="jw-searchfield-1021-triggerWrap"]/tbody/tr/td[1]').click()
        time.sleep(10)

        driver.find_element_by_link_text(iccid).click()

        driver.find_element_by_xpath('.//*[@id="jw-button-1027"]').click()
        time.sleep(10)

        driver.find_element_by_xpath('.//*[@id="3-inputEl"]').clear()
        time.sleep(5)

        element = driver.find_element_by_xpath('.//*[@id="3-inputEl"]').send_keys('Deac')
        time.sleep(10)

        driver.find_element_by_xpath('./html/body/div[26]/div/ul/li').click()

        time.sleep(5)

        driver.find_element_by_link_text('Ok').click()
        time.sleep(10)

        #reboot may requre ask romain
        # Write code to validate the varaibles "
        print('sim1 is been activated back ')
        driver.quit()

    elif active_link == 'WWAN1':
        print('SIM1 is not deactivated properly')

    else:
        print('Check the physical interface of the SIM2 slot')

def connection_check():
    interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
    time.sleep(2)
    link_manager = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_menu"]/span[1]').click()
    time.sleep(2)
    link_status = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_status_tab"]').click()
    A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
    link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
    uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
    ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
    print(A1, 'is', link1, 'UpTime is ', uptime1, 'Ip Address', ip1)

    A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
    link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
    uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
    ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
    print(A2, 'is', link2, uptime2, ip2)


def first_validate():
    driver.find_element_by_xpath('.//*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
    time.sleep(1)
    driver.find_element_by_xpath('.//*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
    time.sleep(2)

    driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
    model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
    print('Modem Model =', model_status)

    iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
    print('Active SIM ICCID =', iccid)

    imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
    print('Active SIM IMEI =', imei)

    Network_provider = driver.find_element_by_xpath('.//*[@id="id_cellular-status-operator_1"]').text
    print('Active Network Provider =', Network_provider)

    network_type = driver.find_element_by_xpath('.//*[@id="id_cellular-status-network_type_1"]').text
    print('Active Network type =', network_type)

    signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
    print('Signal Strength  =', signal_strength)

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

if active_link == 'WWAN2':
    print('SIM1 is not active. The Router is Connected to SIM2')
    print('Trying to connect to SIM1. Please wait.....')
    time.sleep(180)
    driver.get('http://192.168.0.1/auth/login.html')
    login()
    active_link = driver.find_element_by_xpath('.//*[@id="id_active_link-desc_val"]').text
    print("Active Link =", active_link)
    if active_link == 'WWAN2':
        print('Please check the SIM1 physical interface')

    else:
        print('Connected to SIM1')
        connect()



elif active_link == 'WWAN1':
    print('SIM1 is active')
    #driver.get('http://192.168.0.1/auth/login.html')
    interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
    time.sleep(2)
    link_manager = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_menu"]/span[1]').click()
    time.sleep(2)
    link_status = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_status_tab"]').click()
    A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
    link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
    uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
    ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
    print(A1, 'is', link1, 'UpTime is ', uptime1, 'Ip Address', ip1)

    A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
    link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
    uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
    ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
    print(A2, 'is', link2, uptime2, ip2)

    # link_status_click = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status_val_1"]').click()
    driver.find_element_by_xpath('.//*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
    time.sleep(1)
    driver.find_element_by_xpath('.//*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
    time.sleep(2)

    driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
    model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
    print('Modem Model =', model_status)

    iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
    print('Active SIM ICCID =', iccid)

    imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
    print('Active SIM IMEI =', imei)

    Network_provider = driver.find_element_by_xpath('.//*[@id="id_cellular-status-operator_1"]').text
    print('Active Network Provider =', Network_provider)

    network_type = driver.find_element_by_xpath('.//*[@id="id_cellular-status-network_type_1"]').text
    print('Active Network type =', network_type)

    signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
    print('Signal Strength  =', signal_strength)

    # *********************************************************************************
    # **********************connecting to Optus sim Manager*****************************************
    print('Connecting to Optus SIM Card Manager')
    driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
    driver.get('https://optus.jasperwireless.com/provision/jsp/login.jsp;jsessionid=54954536A2F659DBD472B4CD880B5A75')
    # driver.minimize_window()

    username = "simanta"
    password = "thinxtra"

    driver.find_element_by_xpath('.//*[@id="j_username"]').send_keys(username)
    driver.find_element_by_xpath('.//*[@id="j_password"]').send_keys(password)

    driver.find_element_by_xpath(
        './html/body/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/input[2]').click()

    time.sleep(5)
    driver.find_element_by_id('jw-searchfield-1021-inputEl').send_keys(iccid)
    driver.find_element_by_xpath('.//*[@id="jw-searchfield-1021-triggerWrap"]/tbody/tr/td[1]').click()
    time.sleep(10)
    driver.find_element_by_link_text(iccid).click()

    driver.find_element_by_xpath('.//*[@id="jw-button-1027"]').click()
    time.sleep(10)

    driver.find_element_by_xpath('.//*[@id="3-inputEl"]').clear()
    time.sleep(5)

    element = driver.find_element_by_xpath('.//*[@id="3-inputEl"]').send_keys('Deac')
    time.sleep(10)

    driver.find_element_by_xpath('./html/body/div[26]/div/ul/li').click()

    time.sleep(5)

    driver.find_element_by_link_text('Ok').click()

    time.sleep(10)
    print('sim1 has been deactivated')

    driver.quit()

    print('Connecting back to the Router interface')

    print('Waiting on SIM2 to be active. Please wait....... ')
    time.sleep(300)
    #os.system('validate2.py')
    driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
    driver.get('http://192.168.0.1/auth/login.html')
    # driver.minimize_window()

    username = "admin"
    pass1 = "thinxtra"
    pass2 = "admin"
    pass3 = "S8ThaCGBPjcqq2L42NYhlQ=="

    get_title = driver.title
    print("welcome to Robustel ", get_title)
    if get_title == 'Router Web Manager':
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

    active_link = driver.find_element_by_xpath('.//*[@id="id_active_link-desc_val"]').text
    print("Active Link =", active_link)

    if active_link == 'WWAN2':
        connection_check()

        if link2 =='Connected':
            print('Router is connected to SIM2')
            cellular = driver.find_element_by_xpath('.//*[@id="id_interface_cellular_menu"]/span[1]').click()
            time.sleep(1)
            cellular_status = driver.find_element_by_xpath('.//*[@id="id_interface_cellular_status_tab"]').click()
            time.sleep(2)

            B1 = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()
            model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
            print('Modem Model =', model_status)

            iccid1 = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
            print('ICCID after deactivating SIM1 =', iccid1)

            imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
            print('IMEI after deactivating SIM1 =', imei)

            Network_provider = driver.find_element_by_xpath('.//*[@id="id_cellular-status-operator_1"]').text
            print('Network Provider after deactivating SIM1 =', Network_provider)

            network_type = driver.find_element_by_xpath('.//*[@id="id_cellular-status-network_type_1"]').text
            print('Network type after deactivating SIM1 =', network_type)

            signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
            print('Signal_Strength after deactivating SIM1 =', signal_strength)

            print('Activating SIM1 back on. Please wait......')

              # problem occured  after this line of code: the  router looses the  internet connection : solution: may be increse the time sleep until  5 mins

            print('Connecting to Optus SIM Card Manager again')
            driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
            driver.get(
                'https://optus.jasperwireless.com/provision/jsp/login.jsp;jsessionid=54954536A2F659DBD472B4CD880B5A75')
            # driver.minimize_window()

            username = "simanta"
            password = "thinxtra"

            driver.find_element_by_xpath('.//*[@id="j_username"]').send_keys(username)
            driver.find_element_by_xpath('.//*[@id="j_password"]').send_keys(password)

            driver.find_element_by_xpath(
                './html/body/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/input[2]').click()

            time.sleep(5)
            driver.find_element_by_id('jw-searchfield-1021-inputEl').send_keys(iccid)
            driver.find_element_by_xpath('.//*[@id="jw-searchfield-1021-triggerWrap"]/tbody/tr/td[1]').click()
            time.sleep(10)

            driver.find_element_by_link_text(iccid).click()

            driver.find_element_by_xpath('.//*[@id="jw-button-1027"]').click()
            time.sleep(10)

            driver.find_element_by_xpath('.//*[@id="3-inputEl"]').clear()
            time.sleep(5)

            element = driver.find_element_by_xpath('.//*[@id="3-inputEl"]').send_keys('Activated')
            time.sleep(10)

            driver.find_element_by_xpath('./html/body/div[26]/div/ul/li').click()

            time.sleep(5)

            driver.find_element_by_link_text('Ok').click()
            time.sleep(360)
            print('sim1 is been activated back ')
            # Write code to validate the varaibles "

            driver.quit()

        elif link2 =='Disconnected':
            print('SIM2 is disconnected')
            time.sleep(5)
            driver.find_element_by_id('id_reboot').click()
            reboot_sure = driver.find_element_by_id('id_comfirm_yes')
            reboot_sure.click()
            print('Rebooting')
            time.sleep(300)
            driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
            driver.get('http://192.168.0.1/auth/login.html')
            login()

            interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
            time.sleep(2)
            link_manager = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_menu"]/span[1]').click()
            time.sleep(2)
            link_status = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_status_tab"]').click()
            A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
            link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
            uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
            ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
            print(A1, 'is', link1, 'UpTime is ', uptime1, 'Ip Address', ip1)

            A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
            link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
            uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
            ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
            print(A2, 'is', link2, uptime2, ip2)
            if link2 == 'Connected':


            cellular = driver.find_element_by_xpath('.//*[@id="id_interface_cellular_menu"]/span[1]').click()
            time.sleep(1)
            cellular_status = driver.find_element_by_xpath('.//*[@id="id_interface_cellular_status_tab"]').click()
            time.sleep(2)

            B1 = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()
            model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
            print('Modem Model =', model_status)

            iccid1 = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
            print('ICCID after deactivating SIM1 =', iccid1)

            imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
            print('IMEI after deactivating SIM1 =', imei)

            Network_provider = driver.find_element_by_xpath('.//*[@id="id_cellular-status-operator_1"]').text
            print('Network Provider after deactivating SIM1 =', Network_provider)

            network_type = driver.find_element_by_xpath('.//*[@id="id_cellular-status-network_type_1"]').text
            print('Network type after deactivating SIM1 =', network_type)

            signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
            print('Signal_Strength after deactivating SIM1 =', signal_strength)

            print('Activating SIM1 back on. Please wait......')

            time.sleep(
                360)  # problem occured  after this line of code: the  router looses the  internet connection : solution: may be increse the time sleep until  5 mins

            print('Connecting to Optus SIM Card Manager again')
            driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
            driver.get(
                'https://optus.jasperwireless.com/provision/jsp/login.jsp;jsessionid=54954536A2F659DBD472B4CD880B5A75')
            # driver.minimize_window()

            username = "simanta"
            password = "thinxtra"

            driver.find_element_by_xpath('.//*[@id="j_username"]').send_keys(username)
            driver.find_element_by_xpath('.//*[@id="j_password"]').send_keys(password)

            driver.find_element_by_xpath(
                './html/body/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/input[2]').click()

            time.sleep(5)
            driver.find_element_by_id('jw-searchfield-1021-inputEl').send_keys(iccid)
            driver.find_element_by_xpath('.//*[@id="jw-searchfield-1021-triggerWrap"]/tbody/tr/td[1]').click()
            time.sleep(10)

            driver.find_element_by_link_text(iccid).click()

            driver.find_element_by_xpath('.//*[@id="jw-button-1027"]').click()
            time.sleep(10)

            driver.find_element_by_xpath('.//*[@id="3-inputEl"]').clear()
            time.sleep(5)

            element = driver.find_element_by_xpath('.//*[@id="3-inputEl"]').send_keys('Activated')
            time.sleep(10)

            driver.find_element_by_xpath('./html/body/div[26]/div/ul/li').click()

            time.sleep(5)

            driver.find_element_by_link_text('Ok').click()
            time.sleep(10)
            print('sim1 is been activated back ')
            # Write code to validate the varaibles "

            driver.quit()

        elif link2 == 'Connecting' or 'Initializing':
            print('SIM1 is connecting')
            time.sleep(360)
            cellular = driver.find_element_by_xpath('.//*[@id="id_interface_cellular_menu"]/span[1]').click()
            time.sleep(1)
            cellular_status = driver.find_element_by_xpath('.//*[@id="id_interface_cellular_status_tab"]').click()
            time.sleep(2)

            B1 = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()
            model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
            print('Modem Model =', model_status)

            iccid1 = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
            print('ICCID after deactivating SIM1 =', iccid1)

            imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
            print('IMEI after deactivating SIM1 =', imei)

            Network_provider = driver.find_element_by_xpath('.//*[@id="id_cellular-status-operator_1"]').text
            print('Network Provider after deactivating SIM1 =', Network_provider)

            network_type = driver.find_element_by_xpath('.//*[@id="id_cellular-status-network_type_1"]').text
            print('Network type after deactivating SIM1 =', network_type)

            signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
            print('Signal_Strength after deactivating SIM1 =', signal_strength)

            print('Activating SIM1 back on. Please wait......')

            time.sleep(
                360)  # problem occured  after this line of code: the  router looses the  internet connection : solution: may be increse the time sleep until  5 mins

            print('Connecting to Optus SIM Card Manager again')
            driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
            driver.get(
                'https://optus.jasperwireless.com/provision/jsp/login.jsp;jsessionid=54954536A2F659DBD472B4CD880B5A75')
            # driver.minimize_window()

            username = "simanta"
            password = "thinxtra"

            driver.find_element_by_xpath('.//*[@id="j_username"]').send_keys(username)
            driver.find_element_by_xpath('.//*[@id="j_password"]').send_keys(password)

            driver.find_element_by_xpath(
                './html/body/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/input[2]').click()

            time.sleep(5)
            driver.find_element_by_id('jw-searchfield-1021-inputEl').send_keys(iccid)
            driver.find_element_by_xpath('.//*[@id="jw-searchfield-1021-triggerWrap"]/tbody/tr/td[1]').click()
            time.sleep(10)

            driver.find_element_by_link_text(iccid).click()

            driver.find_element_by_xpath('.//*[@id="jw-button-1027"]').click()
            time.sleep(10)

            driver.find_element_by_xpath('.//*[@id="3-inputEl"]').clear()
            time.sleep(5)

            element = driver.find_element_by_xpath('.//*[@id="3-inputEl"]').send_keys('Activated')
            time.sleep(10)

            driver.find_element_by_xpath('./html/body/div[26]/div/ul/li').click()

            time.sleep(5)

            driver.find_element_by_link_text('Ok').click()
            time.sleep(10)
            print('sim1 is been activated back ')
            # Write code to validate the varaibles "

            driver.quit()

        else:
            print('Router does not connect to SIM2')





    elif active_link == 'WWAN1':

        print('Router is still connected to SIM1. Rebooting....')
        time.sleep(10)
        reboot = driver.find_element_by_id('id_reboot').click()
        reboot_sure = driver.find_element_by_id('id_comfirm_yes')
        reboot_sure.click()
        driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
        driver.get('http://192.168.0.1/auth/login.html')
        login()
        interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
        time.sleep(2)

        link_manager = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_menu"]/span[1]').click()
        time.sleep(2)
        link_status = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_status_tab"]').click()


        if link2 =='Connected':
            print('Router is connected to SIM2')
            cellular = driver.find_element_by_xpath('.//*[@id="id_interface_cellular_menu"]/span[1]').click()
            time.sleep(1)
            cellular_status = driver.find_element_by_xpath('.//*[@id="id_interface_cellular_status_tab"]').click()
            time.sleep(2)

            B1 = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()
            model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
            print('Modem Model =', model_status)

            iccid1 = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
            print('ICCID after deactivating SIM1 =', iccid1)

            imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
            print('IMEI after deactivating SIM1 =', imei)

            Network_provider = driver.find_element_by_xpath('.//*[@id="id_cellular-status-operator_1"]').text
            print('Network Provider after deactivating SIM1 =', Network_provider)

            network_type = driver.find_element_by_xpath('.//*[@id="id_cellular-status-network_type_1"]').text
            print('Network type after deactivating SIM1 =', network_type)

            signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
            print('Signal_Strength after deactivating SIM1 =', signal_strength)

            print('Activating SIM1 back on. Please wait......')

            time.sleep(
                360)  # problem occured  after this line of code: the  router looses the  internet connection : solution: may be increse the time sleep until  5 mins

            print('Connecting to Optus SIM Card Manager again')
            driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
            driver.get(
                'https://optus.jasperwireless.com/provision/jsp/login.jsp;jsessionid=54954536A2F659DBD472B4CD880B5A75')
            # driver.minimize_window()

            username = "simanta"
            password = "thinxtra"

            driver.find_element_by_xpath('.//*[@id="j_username"]').send_keys(username)
            driver.find_element_by_xpath('.//*[@id="j_password"]').send_keys(password)

            driver.find_element_by_xpath(
                './html/body/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/input[2]').click()

            time.sleep(5)
            driver.find_element_by_id('jw-searchfield-1021-inputEl').send_keys(iccid)
            driver.find_element_by_xpath('.//*[@id="jw-searchfield-1021-triggerWrap"]/tbody/tr/td[1]').click()
            time.sleep(10)

            driver.find_element_by_link_text(iccid).click()

            driver.find_element_by_xpath('.//*[@id="jw-button-1027"]').click()
            time.sleep(10)

            driver.find_element_by_xpath('.//*[@id="3-inputEl"]').clear()
            time.sleep(5)

            element = driver.find_element_by_xpath('.//*[@id="3-inputEl"]').send_keys('Activated')
            time.sleep(10)

            driver.find_element_by_xpath('./html/body/div[26]/div/ul/li').click()

            time.sleep(5)

            driver.find_element_by_link_text('Ok').click()
            time.sleep(10)
            print('sim1 is been activated back ')
            # Write code to validate the varaibles "

            driver.quit()

        elif link2 == 'Connecting' or 'Initializing':
            print('SIM1 is connecting')
            time.sleep(360)
            cellular = driver.find_element_by_xpath('.//*[@id="id_interface_cellular_menu"]/span[1]').click()
            time.sleep(1)
            cellular_status = driver.find_element_by_xpath('.//*[@id="id_interface_cellular_status_tab"]').click()
            time.sleep(2)

            B1 = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()
            model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
            print('Modem Model =', model_status)

            iccid1 = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
            print('ICCID after deactivating SIM1 =', iccid1)

            imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
            print('IMEI after deactivating SIM1 =', imei)

            Network_provider = driver.find_element_by_xpath('.//*[@id="id_cellular-status-operator_1"]').text
            print('Network Provider after deactivating SIM1 =', Network_provider)

            network_type = driver.find_element_by_xpath('.//*[@id="id_cellular-status-network_type_1"]').text
            print('Network type after deactivating SIM1 =', network_type)

            signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
            print('Signal_Strength after deactivating SIM1 =', signal_strength)

            print('Activating SIM1 back on. Please wait......')

            time.sleep(
                360)  # problem occured  after this line of code: the  router looses the  internet connection : solution: may be increse the time sleep until  5 mins

            print('Connecting to Optus SIM Card Manager again')
            driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
            driver.get(
                'https://optus.jasperwireless.com/provision/jsp/login.jsp;jsessionid=54954536A2F659DBD472B4CD880B5A75')
            # driver.minimize_window()

            username = "simanta"
            password = "thinxtra"

            driver.find_element_by_xpath('.//*[@id="j_username"]').send_keys(username)
            driver.find_element_by_xpath('.//*[@id="j_password"]').send_keys(password)

            driver.find_element_by_xpath(
                './html/body/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/input[2]').click()

            time.sleep(5)
            driver.find_element_by_id('jw-searchfield-1021-inputEl').send_keys(iccid)
            driver.find_element_by_xpath('.//*[@id="jw-searchfield-1021-triggerWrap"]/tbody/tr/td[1]').click()
            time.sleep(10)

            driver.find_element_by_link_text(iccid).click()

            driver.find_element_by_xpath('.//*[@id="jw-button-1027"]').click()
            time.sleep(10)

            driver.find_element_by_xpath('.//*[@id="3-inputEl"]').clear()
            time.sleep(5)

            element = driver.find_element_by_xpath('.//*[@id="3-inputEl"]').send_keys('Activated')
            time.sleep(10)

            driver.find_element_by_xpath('./html/body/div[26]/div/ul/li').click()

            time.sleep(5)

            driver.find_element_by_link_text('Ok').click()
            time.sleep(10)
            print('sim1 is been activated back ')
            # Write code to validate the varaibles "

            driver.quit()

        else:
            print('Router does not connect to SIM2')


    else:
        print('Check the physical interface of the SIM2 slot')
else:
    print("Both SIM Card slots are not working")







