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

if link1 == 'Connected':
    print('The router is connected to the SIM1')
    print('Please check the configurations')
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
    time.sleep(2)
    print('Deactivating SIM1 now ')
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
        './html/body/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/input').click()

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



    print('Waiting on SIM2 to be active. Please wait....... ')
    time.sleep(120)
    print('Connecting back to the Router interface')

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
    #uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
    ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
    print(A1, 'is', link1)

    A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
    link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
    #uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
    #ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
    print(A2, 'is', link2)

    if link2 == 'Connected':
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
            './html/body/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/input').click()

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
        print('SIM1 has been activated back from Optus SIM Manager. Lets check if router has switch back to SIM1 ')
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
        #ptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
        #p1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
        print(A1, 'is', link1)

        A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
        link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
       #uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
        #p2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
        print(A2, 'is', link2)

        if link1 == 'Connected':
            print('The router is connected back to the SIM1')
            print('Please check the configurations')
            driver.find_element_by_xpath('.//*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
            time.sleep(1)
            driver.find_element_by_xpath('.//*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
            time.sleep(2)

            driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
            model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
            print('Modem Model =', model_status)

            iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
            print(' SIM1 ICCID =', iccid)

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

        elif link1 == 'Disconnected':
            print('SIM1 is disconnected')
            time.sleep(5)
            driver.find_element_by_id('id_reboot').click()
            reboot_sure = driver.find_element_by_id('id_comfirm_yes')
            reboot_sure.click()
            print('Rebooting')
            time.sleep(360)
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
            #uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
            #ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
            print(A1, 'is', link1)

            A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
            link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
            #uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
            #ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
            print(A2, 'is', link2)

            if link1 == 'Connected':
                print('The router is connected back to the SIM1')
                print('Please check the configurations')
                driver.find_element_by_xpath('.//*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                time.sleep(1)
                driver.find_element_by_xpath('.//*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                time.sleep(2)

                driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                print('Modem Model =', model_status)

                iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                print(' SIM1 ICCID =', iccid)

                imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                print('SIM1 IMEI =', imei)

                Network_provider = driver.find_element_by_xpath('.//*[@id="id_cellular-status-operator_1"]').text
                print('SIM1 Network Provider =', Network_provider)

                network_type = driver.find_element_by_xpath('.//*[@id="id_cellular-status-network_type_1"]').text
                print('SIM1 Network type =', network_type)

                signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                print('Signal Strength using SIM1  =', signal_strength)
                time.sleep(2)

                print('Router can Switch back to SIM1 after a Rebooting ')


            elif link1 == 'Disconnected':
                print('Router cannot switch back to SIM1 even after rebooting')


            else:
                print('Router is Connecting to SIM1. Please wait......')
                time.sleep(360)
                print('Please check the configurations')

                interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                time.sleep(2)
                link_manager = driver.find_element_by_xpath(
                    './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                time.sleep(2)
                link_status = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_status_tab"]').click()
                A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                #uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                #ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                print(A1, 'is', link1)

                A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                #uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                #ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                print(A2, 'is', link2)

                if link1 == "Connected":

                    driver.find_element_by_xpath('.//*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                    time.sleep(1)
                    driver.find_element_by_xpath(
                        './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                    time.sleep(2)

                    driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                    model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                    print('Modem Model =', model_status)

                    iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                    print(' SIM1 ICCID =', iccid)

                    imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                    print('SIM1 IMEI =', imei)

                    Network_provider = driver.find_element_by_xpath('.//*[@id="id_cellular-status-operator_1"]').text
                    print('SIM1 Network Provider =', Network_provider)

                    network_type = driver.find_element_by_xpath('.//*[@id="id_cellular-status-network_type_1"]').text
                    print('SIM1 Network type =', network_type)

                    signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                    print('Signal Strength using SIM1  =', signal_strength)
                    time.sleep(2)
                    print('Router can Switch back to SIM1 but takes time ( Additional 5 minutes )')

                elif link1 == 'Disconnected':
                    print('Router cannot switch back to SIM1 even after waiting more than 6 minutes ')

                else:
                    print('Router tried to connect back to SIM1 but fails ')

        else:
            print('Router is Connecting to SIM1. Please wait......')
            time.sleep(360)
            print('Please check the configurations')

            interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
            time.sleep(2)
            link_manager = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_menu"]/span[1]').click()
            time.sleep(2)
            link_status = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_status_tab"]').click()
            A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
            link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
            #me1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
            #ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
            print(A1, 'is', link1)

            A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
            link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
           # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
            #ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
            print(A2, 'is', link2)

            if link1 == "Connected":

                driver.find_element_by_xpath('.//*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                time.sleep(1)
                driver.find_element_by_xpath('.//*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                time.sleep(2)

                driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                print('Modem Model =', model_status)

                iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                print(' SIM1 ICCID =', iccid)

                imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                print('SIM1 IMEI =', imei)

                Network_provider = driver.find_element_by_xpath('.//*[@id="id_cellular-status-operator_1"]').text
                print('SIM1 Network Provider =', Network_provider)

                network_type = driver.find_element_by_xpath('.//*[@id="id_cellular-status-network_type_1"]').text
                print('SIM1 Network type =', network_type)

                signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                print('Signal Strength using SIM1  =', signal_strength)
                time.sleep(2)
                print('Router can Switch back to SIM1 but takes time ( Additional 5 minutes )')

            elif link1 == 'Disconnected':
                print('Router cannot switch back to SIM1 even after waiting more than 6 minutes ')

            else:
                print('Router tried to connect back to SIM1 but fails ')

    elif link2 == 'Disconnected':
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
            #uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
            ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
            print(A1, 'is', link1)

            A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
            link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
            #uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
            #ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
            print(A2, 'is', link2)

            if link2 == 'Connected':
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

                print('Connecting to Optus SIM Card Manager again')
                driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
                driver.get(
                    'https://optus.jasperwireless.com/provision/jsp/login.jsp;jsessionid=54954536A2F659DBD472B4CD880B5A75')
                # driver.minimize_window()

                username = "simanta"
                password = "thinxtra"

                driver.find_element_by_xpath('.//*[@id="j_username"]').send_keys(username)
                driver.find_element_by_xpath('.//*[@id="j_password"]').send_keys(password)

                driver.find_element_by_xpath('./html/body/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/input').click()

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
                print(
                    'SIM1 has been activated back from Optus SIM Manager. Lets check if router has switch back to SIM1 ')
                driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
                driver.get('http://192.168.0.1/auth/login.html')

                login()

                interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                time.sleep(2)
                link_manager = driver.find_element_by_xpath(
                    './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                time.sleep(2)
                link_status = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_status_tab"]').click()
                A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                #uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                #ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                print(A1, 'is', link1)

                A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                #uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                #p2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                print(A2, 'is', link2)

                if link1 == 'Connected':
                    print('The router is connected back to the SIM1')
                    print('Please check the configurations')
                    driver.find_element_by_xpath('.//*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                    time.sleep(1)
                    driver.find_element_by_xpath(
                        './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                    time.sleep(2)

                    driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                    model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                    print('Modem Model =', model_status)

                    iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                    print(' SIM1 ICCID =', iccid)

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

                elif link1 == 'Disconnected':
                    print('SIM1 is disconnected')
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
                    link_manager = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                    time.sleep(2)
                    link_status = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_status_tab"]').click()
                    A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                    link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                    #uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                    #ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                    print(A1, 'is', link1)

                    A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                    link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                    #uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                    #ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                    print(A2, 'is', link2)

                    if link1 == 'Connected':
                        print('The router is connected back to the SIM1')
                        print('Please check the configurations')
                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                        time.sleep(1)
                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                        time.sleep(2)

                        driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                        model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                        print('Modem Model =', model_status)

                        iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                        print(' SIM1 ICCID =', iccid)

                        imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                        print('SIM1 IMEI =', imei)

                        Network_provider = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-operator_1"]').text
                        print('SIM1 Network Provider =', Network_provider)

                        network_type = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-network_type_1"]').text
                        print('SIM1 Network type =', network_type)

                        signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                        print('Signal Strength using SIM1  =', signal_strength)
                        time.sleep(2)

                        print('Router can Switch back to SIM1 after a Rebooting ')


                    elif link1 == 'Disconnected':
                        print('Router cannot switch back to SIM1 even after rebooting')


                    else:
                        print('Router is Connecting to SIM1. Please wait......')
                        time.sleep(360)
                        print('Please check the configurations')

                        interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                        time.sleep(2)
                        link_manager = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                        time.sleep(2)
                        link_status = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_status_tab"]').click()
                        A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                        link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                        #uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                        #ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                        print(A1, 'is', link1)

                        A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                        link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                        #uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                        #ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                        print(A2, 'is', link2)

                        if link1 == "Connected":

                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                            time.sleep(1)
                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                            time.sleep(2)

                            driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                            model_status = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-modem_model_1"]').text
                            print('Modem Model =', model_status)

                            iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                            print(' SIM1 ICCID =', iccid)

                            imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                            print('SIM1 IMEI =', imei)

                            Network_provider = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-operator_1"]').text
                            print('SIM1 Network Provider =', Network_provider)

                            network_type = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-network_type_1"]').text
                            print('SIM1 Network type =', network_type)

                            signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                            print('Signal Strength using SIM1  =', signal_strength)
                            time.sleep(2)
                            print('Router can Switch back to SIM1 but takes time ( Additional 5 minutes )')

                        elif link1 == 'Disconnected':
                            print('Router cannot switch back to SIM1 even after waiting more than 6 minutes ')

                        else:
                            print('Router tried to connect back to SIM1 but fails ')

                else:
                    print('Router is Connecting to SIM1. Please wait......')
                    time.sleep(360)
                    print('Please check the configurations')

                    interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                    time.sleep(2)
                    link_manager = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                    time.sleep(2)
                    link_status = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_status_tab"]').click()
                    A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                    link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                    #me1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                    #ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                    print(A1, 'is', link1)

                    A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                    link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                    #uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                    #ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                    print(A2, 'is', link2)

                    if link1 == "Connected":

                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                        time.sleep(1)
                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                        time.sleep(2)

                        driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                        model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                        print('Modem Model =', model_status)

                        iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                        print(' SIM1 ICCID =', iccid)

                        imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                        print('SIM1 IMEI =', imei)

                        Network_provider = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-operator_1"]').text
                        print('SIM1 Network Provider =', Network_provider)

                        network_type = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-network_type_1"]').text
                        print('SIM1 Network type =', network_type)

                        signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                        print('Signal Strength using SIM1  =', signal_strength)
                        time.sleep(2)
                        print('Router can Switch back to SIM1 but takes time ( Additional 5 minutes )')

                    elif link1 == 'Disconnected':
                        print('Router cannot switch back to SIM1 even after waiting more than 6 minutes ')

                    else:
                        print('Router tried to connect back to SIM1 but fails ')

            elif link2 == 'Disconnected':
                print('Router cannot connect to SIM2 even after rebooting')

            else:
                print('Router is Connecting to SIM2. Please wait......')
                time.sleep(360)
                print('Please check the configurations')

                interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                time.sleep(2)
                link_manager = driver.find_element_by_xpath(
                    './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                time.sleep(2)
                link_status = driver.find_element_by_xpath(
                    './/*[@id="id_interface_link_manager_status_tab"]').click()
                A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                #me1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                #ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                print(A1, 'is', link1)

                A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                #uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                #ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                print(A2, 'is', link2)

                if link2 == 'Connected':
                    print('Router is connected to SIM2')
                    cellular = driver.find_element_by_xpath('.//*[@id="id_interface_cellular_menu"]/span[1]').click()
                    time.sleep(1)
                    cellular_status = driver.find_element_by_xpath(
                        './/*[@id="id_interface_cellular_status_tab"]').click()
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
                        './html/body/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/input').click()

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
                    print(
                        'SIM1 has been activated back from Optus SIM Manager. Lets check if router has switch back to SIM1 ')
                    driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
                    driver.get('http://192.168.0.1/auth/login.html')

                    login()

                    interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                    time.sleep(2)
                    link_manager = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                    time.sleep(2)
                    link_status = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_status_tab"]').click()
                    A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                    link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                    #uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                    #ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                    print(A1, 'is', link1)

                    A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                    link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                   # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                   #ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                    print(A2, 'is', link2)

                    if link1 == 'Connected':
                        print('The router is connected back to the SIM1')
                        print('Please check the configurations')
                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                        time.sleep(1)
                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                        time.sleep(2)

                        driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                        model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                        print('Modem Model =', model_status)

                        iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                        print(' SIM1 ICCID =', iccid)

                        imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                        print('SIM1 IMEI =', imei)

                        Network_provider = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-operator_1"]').text
                        print('SIM1 Network Provider =', Network_provider)

                        network_type = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-network_type_1"]').text
                        print('SIM1 Network type =', network_type)

                        signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                        print('Signal Strength using SIM1  =', signal_strength)
                        time.sleep(2)

                        print('Router can Switch back to SIM1 after SIM2 has been deactivated')

                    elif link1 == 'Disconnected':
                        print('SIM1 is disconnected')
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
                        link_manager = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                        time.sleep(2)
                        link_status = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_status_tab"]').click()
                        A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                        link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                        #uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                        #ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                        print(A1, 'is', link1)

                        A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                        link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                        #uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                        #ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                        print(A2, 'is', link2)

                        if link1 == 'Connected':
                            print('The router is connected back to the SIM1')
                            print('Please check the configurations')
                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                            time.sleep(1)
                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                            time.sleep(2)

                            driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                            model_status = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-modem_model_1"]').text
                            print('Modem Model =', model_status)

                            iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                            print(' SIM1 ICCID =', iccid)

                            imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                            print('SIM1 IMEI =', imei)

                            Network_provider = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-operator_1"]').text
                            print('SIM1 Network Provider =', Network_provider)

                            network_type = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-network_type_1"]').text
                            print('SIM1 Network type =', network_type)

                            signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                            print('Signal Strength using SIM1  =', signal_strength)
                            time.sleep(2)

                            print('Router can Switch back to SIM1 after a Rebooting ')


                        elif link1 == 'Disconnected':
                            print('Router cannot switch back to SIM1 even after rebooting')


                        else:
                            print('Router is Connecting to SIM1. Please wait......')
                            time.sleep(360)
                            print('Please check the configurations')

                            interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                            time.sleep(2)
                            link_manager = driver.find_element_by_xpath(
                                './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                            time.sleep(2)
                            link_status = driver.find_element_by_xpath(
                                './/*[@id="id_interface_link_manager_status_tab"]').click()
                            A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                            link1 = driver.find_element_by_xpath(
                                './/*[@id="id_link_manager-link_status-status_1"]').text
                            #uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                            #ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                            print(A1, 'is', link1)

                            A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                            link2 = driver.find_element_by_xpath(
                                './/*[@id="id_link_manager-link_status-status_2"]').text
                            #uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                            #ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                            print(A2, 'is', link2)

                            if link1 == "Connected":

                                driver.find_element_by_xpath(
                                    './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                                time.sleep(1)
                                driver.find_element_by_xpath(
                                    './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                                time.sleep(2)

                                driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                                model_status = driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-modem_model_1"]').text
                                print('Modem Model =', model_status)

                                iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                                print(' SIM1 ICCID =', iccid)

                                imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                                print('SIM1 IMEI =', imei)

                                Network_provider = driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-operator_1"]').text
                                print('SIM1 Network Provider =', Network_provider)

                                network_type = driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-network_type_1"]').text
                                print('SIM1 Network type =', network_type)

                                signal_strength = driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-csq_1"]').text
                                print('Signal Strength using SIM1  =', signal_strength)
                                time.sleep(2)
                                print('Router can Switch back to SIM1 but takes time ( Additional 5 minutes )')

                            elif link1 == 'Disconnected':
                                print('Router cannot switch back to SIM1 even after waiting more than 6 minutes ')

                            else:
                                print('Router tried to connect back to SIM1 but fails ')

                    else:
                        print('Router is Connecting to SIM1. Please wait......')
                        time.sleep(360)
                        print('Please check the configurations')

                        interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                        time.sleep(2)
                        link_manager = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                        time.sleep(2)
                        link_status = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_status_tab"]').click()
                        A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                        link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                        #uptime1 = driver.find_element_by_xpath( './/*[@id="id_link_manager-link_status-link_uptime_1"]').text
                        #ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                        print(A1, 'is', link1)

                        A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                        link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                        #uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                        #ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                        print(A2, 'is', link2)

                        if link1 == "Connected":

                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                            time.sleep(1)
                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                            time.sleep(2)

                            driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                            model_status = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-modem_model_1"]').text
                            print('Modem Model =', model_status)

                            iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                            print(' SIM1 ICCID =', iccid)

                            imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                            print('SIM1 IMEI =', imei)

                            Network_provider = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-operator_1"]').text
                            print('SIM1 Network Provider =', Network_provider)

                            network_type = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-network_type_1"]').text
                            print('SIM1 Network type =', network_type)

                            signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                            print('Signal Strength using SIM1  =', signal_strength)
                            time.sleep(2)
                            print('Router can Switch back to SIM1 but takes time ( Additional 5 minutes )')

                        elif link1 == 'Disconnected':
                            print('Router cannot switch back to SIM1 even after waiting more than 6 minutes ')

                        else:
                            print('Router tried to connect back to SIM1 but fails ')


    else:
        print('Router is connecting to SIM2')
        time.sleep(360)
        print('Please check the configurations')

        interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
        time.sleep(2)
        link_manager = driver.find_element_by_xpath(
            './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
        time.sleep(2)
        link_status = driver.find_element_by_xpath(
            './/*[@id="id_interface_link_manager_status_tab"]').click()
        A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
        link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
        #me1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
        #ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
        print(A1, 'is', link1)

        A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
        link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
        #uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
       #ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
        print(A2, 'is', link2)

        if link2 == 'Connected':
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
                './html/body/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/input').click()

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
            print(
                'SIM1 has been activated back from Optus SIM Manager. Lets check if router has switch back to SIM1 ')
            driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
            driver.get('http://192.168.0.1/auth/login.html')

            login()

            interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
            time.sleep(2)
            link_manager = driver.find_element_by_xpath(
                './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
            time.sleep(2)
            link_status = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_status_tab"]').click()
            A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
            link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
            #uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
            #ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
            print(A1, 'is', link1)

            A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
            link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
            #uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
            #ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
            print(A2, 'is', link2)

            if link1 == 'Connected':
                print('The router is connected back to the SIM1')
                print('Please check the configurations')
                driver.find_element_by_xpath('.//*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                time.sleep(1)
                driver.find_element_by_xpath(
                    './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                time.sleep(2)

                driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                print('Modem Model =', model_status)

                iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                print(' SIM1 ICCID =', iccid)

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

            elif link1 == 'Disconnected':
                print('SIM1 is disconnected')
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
                link_manager = driver.find_element_by_xpath(
                    './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                time.sleep(2)
                link_status = driver.find_element_by_xpath(
                    './/*[@id="id_interface_link_manager_status_tab"]').click()
                A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                #uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                #ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                print(A1, 'is', link1)

                A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
               # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                #ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                print(A2, 'is', link2)

                if link1 == 'Connected':
                    print('The router is connected back to the SIM1')
                    print('Please check the configurations')
                    driver.find_element_by_xpath(
                        './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                    time.sleep(1)
                    driver.find_element_by_xpath(
                        './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                    time.sleep(2)

                    driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                    model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                    print('Modem Model =', model_status)

                    iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                    print(' SIM1 ICCID =', iccid)

                    imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                    print('SIM1 IMEI =', imei)

                    Network_provider = driver.find_element_by_xpath(
                        './/*[@id="id_cellular-status-operator_1"]').text
                    print('SIM1 Network Provider =', Network_provider)

                    network_type = driver.find_element_by_xpath(
                        './/*[@id="id_cellular-status-network_type_1"]').text
                    print('SIM1 Network type =', network_type)

                    signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                    print('Signal Strength using SIM1  =', signal_strength)
                    time.sleep(2)

                    print('Router can Switch back to SIM1 after a Rebooting ')


                elif link1 == 'Disconnected':
                    print('Router cannot switch back to SIM1 even after rebooting')


                else:
                    print('Router is Connecting to SIM1. Please wait......')
                    time.sleep(360)
                    print('Please check the configurations')

                    interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                    time.sleep(2)
                    link_manager = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                    time.sleep(2)
                    link_status = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_status_tab"]').click()
                    A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                    link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                    #uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                    #ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                    print(A1, 'is', link1)

                    A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                    link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                   # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                    #p2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                    print(A2, 'is', link2)

                    if link1 == "Connected":

                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                        time.sleep(1)
                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                        time.sleep(2)

                        driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                        model_status = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-modem_model_1"]').text
                        print('Modem Model =', model_status)

                        iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                        print(' SIM1 ICCID =', iccid)

                        imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                        print('SIM1 IMEI =', imei)

                        Network_provider = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-operator_1"]').text
                        print('SIM1 Network Provider =', Network_provider)

                        network_type = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-network_type_1"]').text
                        print('SIM1 Network type =', network_type)

                        signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                        print('Signal Strength using SIM1  =', signal_strength)
                        time.sleep(2)
                        print('Router can Switch back to SIM1 but takes time ( Additional 5 minutes )')

                    elif link1 == 'Disconnected':
                        print('Router cannot switch back to SIM1 even after waiting more than 6 minutes ')

                    else:
                        print('Router tried to connect back to SIM1 but fails ')

            else:
                print('Router is Connecting to SIM1. Please wait......')
                time.sleep(360)
                print('Please check the configurations')

                interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                time.sleep(2)
                link_manager = driver.find_element_by_xpath(
                    './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                time.sleep(2)
                link_status = driver.find_element_by_xpath(
                    './/*[@id="id_interface_link_manager_status_tab"]').click()
                A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                #e1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                #p1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                print(A1, 'is', link1)

                A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                #ptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                #p2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                print(A2, 'is', link2)

                if link1 == "Connected":

                    driver.find_element_by_xpath(
                        './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                    time.sleep(1)
                    driver.find_element_by_xpath(
                        './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                    time.sleep(2)

                    driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                    model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                    print('Modem Model =', model_status)

                    iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                    print(' SIM1 ICCID =', iccid)

                    imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                    print('SIM1 IMEI =', imei)

                    Network_provider = driver.find_element_by_xpath(
                        './/*[@id="id_cellular-status-operator_1"]').text
                    print('SIM1 Network Provider =', Network_provider)

                    network_type = driver.find_element_by_xpath(
                        './/*[@id="id_cellular-status-network_type_1"]').text
                    print('SIM1 Network type =', network_type)

                    signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                    print('Signal Strength using SIM1  =', signal_strength)
                    time.sleep(2)
                    print('Router can Switch back to SIM1 but takes time ( Additional 5 minutes )')

                elif link1 == 'Disconnected':
                    print('Router cannot switch back to SIM1 even after waiting more than 6 minutes ')

                else:
                    print('Router tried to connect back to SIM1 but fails ')


        elif link2 == 'Disconnected':
            print('The router cannot connect to SIM2')
        else:
            print('The router cannot connect to SIM2')

elif link1 == 'Disconnected':
    print('Router is Disconnected to SIM1')
    time.sleep(5)
    driver.find_element_by_id('id_reboot').click()
    reboot_sure = driver.find_element_by_id('id_comfirm_yes')
    reboot_sure.click()
    print('Rebooting')
    time.sleep(360)
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
    # ptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
    # p1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
    print(A1, 'is', link1)

    A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
    link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
    # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
    # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
    print(A2, 'is', link2)
    if link1 == 'Connected':
        print('The router is connected to the SIM1')
        print('Please check the configurations')
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
        time.sleep(2)
        print('Deactivating SIM1 now ')
        # *********************************************************************************
        # **********************connecting to Optus sim Manager*****************************************
        print('Connecting to Optus SIM Card Manager')
        driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
        driver.get(
            'https://optus.jasperwireless.com/provision/jsp/login.jsp;jsessionid=54954536A2F659DBD472B4CD880B5A75')
        # driver.minimize_window()

        username = "simanta"
        password = "thinxtra"

        driver.find_element_by_xpath('.//*[@id="j_username"]').send_keys(username)
        driver.find_element_by_xpath('.//*[@id="j_password"]').send_keys(password)

        driver.find_element_by_xpath(
            './html/body/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/input').click()

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

        print('Waiting on SIM2 to be active. Please wait....... ')
        time.sleep(120)
        print('Connecting back to the Router interface')

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
        # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
        ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
        print(A1, 'is', link1)

        A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
        link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
        # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
        # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
        print(A2, 'is', link2)

        if link2 == 'Connected':
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
                './html/body/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/input').click()

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
            print('SIM1 has been activated back from Optus SIM Manager. Lets check if router has switch back to SIM1 ')
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
            # ptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
            # p1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
            print(A1, 'is', link1)

            A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
            link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
            # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
            # p2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
            print(A2, 'is', link2)

            if link1 == 'Connected':
                print('The router is connected back to the SIM1')
                print('Please check the configurations')
                driver.find_element_by_xpath('.//*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                time.sleep(1)
                driver.find_element_by_xpath('.//*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                time.sleep(2)

                driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                print('Modem Model =', model_status)

                iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                print(' SIM1 ICCID =', iccid)

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

            elif link1 == 'Disconnected':
                print('SIM1 is disconnected')
                time.sleep(5)
                driver.find_element_by_id('id_reboot').click()
                reboot_sure = driver.find_element_by_id('id_comfirm_yes')
                reboot_sure.click()
                print('Rebooting')
                time.sleep(360)
                driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
                driver.get('http://192.168.0.1/auth/login.html')
                login()

                interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                time.sleep(2)
                link_manager = driver.find_element_by_xpath(
                    './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                time.sleep(2)
                link_status = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_status_tab"]').click()
                A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                print(A1, 'is', link1)

                A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                print(A2, 'is', link2)

                if link1 == 'Connected':
                    print('The router is connected back to the SIM1')
                    print('Please check the configurations')
                    driver.find_element_by_xpath('.//*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                    time.sleep(1)
                    driver.find_element_by_xpath(
                        './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                    time.sleep(2)

                    driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                    model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                    print('Modem Model =', model_status)

                    iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                    print(' SIM1 ICCID =', iccid)

                    imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                    print('SIM1 IMEI =', imei)

                    Network_provider = driver.find_element_by_xpath('.//*[@id="id_cellular-status-operator_1"]').text
                    print('SIM1 Network Provider =', Network_provider)

                    network_type = driver.find_element_by_xpath('.//*[@id="id_cellular-status-network_type_1"]').text
                    print('SIM1 Network type =', network_type)

                    signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                    print('Signal Strength using SIM1  =', signal_strength)
                    time.sleep(2)

                    print('Router can Switch back to SIM1 after a Rebooting ')


                elif link1 == 'Disconnected':
                    print('Router cannot switch back to SIM1 even after rebooting')


                else:
                    print('Router is Connecting to SIM1. Please wait......')
                    time.sleep(360)
                    print('Please check the configurations')

                    interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                    time.sleep(2)
                    link_manager = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                    time.sleep(2)
                    link_status = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_status_tab"]').click()
                    A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                    link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                    # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                    # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                    print(A1, 'is', link1)

                    A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                    link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                    # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                    # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                    print(A2, 'is', link2)

                    if link1 == "Connected":

                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                        time.sleep(1)
                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                        time.sleep(2)

                        driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                        model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                        print('Modem Model =', model_status)

                        iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                        print(' SIM1 ICCID =', iccid)

                        imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                        print('SIM1 IMEI =', imei)

                        Network_provider = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-operator_1"]').text
                        print('SIM1 Network Provider =', Network_provider)

                        network_type = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-network_type_1"]').text
                        print('SIM1 Network type =', network_type)

                        signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                        print('Signal Strength using SIM1  =', signal_strength)
                        time.sleep(2)
                        print('Router can Switch back to SIM1 but takes time ( Additional 5 minutes )')

                    elif link1 == 'Disconnected':
                        print('Router cannot switch back to SIM1 even after waiting more than 6 minutes ')

                    else:
                        print('Router tried to connect back to SIM1 but fails ')

            else:
                print('Router is Connecting to SIM1. Please wait......')
                time.sleep(360)
                print('Please check the configurations')

                interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                time.sleep(2)
                link_manager = driver.find_element_by_xpath(
                    './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                time.sleep(2)
                link_status = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_status_tab"]').click()
                A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                # me1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                print(A1, 'is', link1)

                A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                print(A2, 'is', link2)

                if link1 == "Connected":

                    driver.find_element_by_xpath('.//*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                    time.sleep(1)
                    driver.find_element_by_xpath(
                        './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                    time.sleep(2)

                    driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                    model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                    print('Modem Model =', model_status)

                    iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                    print(' SIM1 ICCID =', iccid)

                    imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                    print('SIM1 IMEI =', imei)

                    Network_provider = driver.find_element_by_xpath('.//*[@id="id_cellular-status-operator_1"]').text
                    print('SIM1 Network Provider =', Network_provider)

                    network_type = driver.find_element_by_xpath('.//*[@id="id_cellular-status-network_type_1"]').text
                    print('SIM1 Network type =', network_type)

                    signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                    print('Signal Strength using SIM1  =', signal_strength)
                    time.sleep(2)
                    print('Router can Switch back to SIM1 but takes time ( Additional 5 minutes )')

                elif link1 == 'Disconnected':
                    print('Router cannot switch back to SIM1 even after waiting more than 6 minutes ')

                else:
                    print('Router tried to connect back to SIM1 but fails ')

        elif link2 == 'Disconnected':
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
            # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
            ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
            print(A1, 'is', link1)

            A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
            link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
            # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
            # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
            print(A2, 'is', link2)

            if link2 == 'Connected':
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
                    './html/body/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/input').click()

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
                print(
                    'SIM1 has been activated back from Optus SIM Manager. Lets check if router has switch back to SIM1 ')
                driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
                driver.get('http://192.168.0.1/auth/login.html')

                login()

                interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                time.sleep(2)
                link_manager = driver.find_element_by_xpath(
                    './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                time.sleep(2)
                link_status = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_status_tab"]').click()
                A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                print(A1, 'is', link1)

                A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                # p2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                print(A2, 'is', link2)

                if link1 == 'Connected':
                    print('The router is connected back to the SIM1')
                    print('Please check the configurations')
                    driver.find_element_by_xpath('.//*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                    time.sleep(1)
                    driver.find_element_by_xpath(
                        './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                    time.sleep(2)

                    driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                    model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                    print('Modem Model =', model_status)

                    iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                    print(' SIM1 ICCID =', iccid)

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

                elif link1 == 'Disconnected':
                    print('SIM1 is disconnected')
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
                    link_manager = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                    time.sleep(2)
                    link_status = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_status_tab"]').click()
                    A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                    link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                    # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                    # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                    print(A1, 'is', link1)

                    A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                    link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                    # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                    # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                    print(A2, 'is', link2)

                    if link1 == 'Connected':
                        print('The router is connected back to the SIM1')
                        print('Please check the configurations')
                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                        time.sleep(1)
                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                        time.sleep(2)

                        driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                        model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                        print('Modem Model =', model_status)

                        iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                        print(' SIM1 ICCID =', iccid)

                        imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                        print('SIM1 IMEI =', imei)

                        Network_provider = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-operator_1"]').text
                        print('SIM1 Network Provider =', Network_provider)

                        network_type = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-network_type_1"]').text
                        print('SIM1 Network type =', network_type)

                        signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                        print('Signal Strength using SIM1  =', signal_strength)
                        time.sleep(2)

                        print('Router can Switch back to SIM1 after a Rebooting ')


                    elif link1 == 'Disconnected':
                        print('Router cannot switch back to SIM1 even after rebooting')


                    else:
                        print('Router is Connecting to SIM1. Please wait......')
                        time.sleep(360)
                        print('Please check the configurations')

                        interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                        time.sleep(2)
                        link_manager = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                        time.sleep(2)
                        link_status = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_status_tab"]').click()
                        A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                        link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                        # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                        # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                        print(A1, 'is', link1)

                        A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                        link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                        # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                        # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                        print(A2, 'is', link2)

                        if link1 == "Connected":

                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                            time.sleep(1)
                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                            time.sleep(2)

                            driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                            model_status = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-modem_model_1"]').text
                            print('Modem Model =', model_status)

                            iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                            print(' SIM1 ICCID =', iccid)

                            imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                            print('SIM1 IMEI =', imei)

                            Network_provider = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-operator_1"]').text
                            print('SIM1 Network Provider =', Network_provider)

                            network_type = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-network_type_1"]').text
                            print('SIM1 Network type =', network_type)

                            signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                            print('Signal Strength using SIM1  =', signal_strength)
                            time.sleep(2)
                            print('Router can Switch back to SIM1 but takes time ( Additional 5 minutes )')

                        elif link1 == 'Disconnected':
                            print('Router cannot switch back to SIM1 even after waiting more than 6 minutes ')

                        else:
                            print('Router tried to connect back to SIM1 but fails ')

                else:
                    print('Router is Connecting to SIM1. Please wait......')
                    time.sleep(360)
                    print('Please check the configurations')

                    interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                    time.sleep(2)
                    link_manager = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                    time.sleep(2)
                    link_status = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_status_tab"]').click()
                    A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                    link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                    # me1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                    # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                    print(A1, 'is', link1)

                    A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                    link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                    # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                    # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                    print(A2, 'is', link2)

                    if link1 == "Connected":

                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                        time.sleep(1)
                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                        time.sleep(2)

                        driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                        model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                        print('Modem Model =', model_status)

                        iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                        print(' SIM1 ICCID =', iccid)

                        imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                        print('SIM1 IMEI =', imei)

                        Network_provider = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-operator_1"]').text
                        print('SIM1 Network Provider =', Network_provider)

                        network_type = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-network_type_1"]').text
                        print('SIM1 Network type =', network_type)

                        signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                        print('Signal Strength using SIM1  =', signal_strength)
                        time.sleep(2)
                        print('Router can Switch back to SIM1 but takes time ( Additional 5 minutes )')

                    elif link1 == 'Disconnected':
                        print('Router cannot switch back to SIM1 even after waiting more than 6 minutes ')

                    else:
                        print('Router tried to connect back to SIM1 but fails ')

            elif link2 == 'Disconnected':
                print('Router cannot connect to SIM2 even after rebooting')

            else:
                print('Router is Connecting to SIM2. Please wait......')
                time.sleep(360)
                print('Please check the configurations')

                interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                time.sleep(2)
                link_manager = driver.find_element_by_xpath(
                    './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                time.sleep(2)
                link_status = driver.find_element_by_xpath(
                    './/*[@id="id_interface_link_manager_status_tab"]').click()
                A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                # me1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                print(A1, 'is', link1)

                A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                print(A2, 'is', link2)

                if link2 == 'Connected':
                    print('Router is connected to SIM2')
                    cellular = driver.find_element_by_xpath('.//*[@id="id_interface_cellular_menu"]/span[1]').click()
                    time.sleep(1)
                    cellular_status = driver.find_element_by_xpath(
                        './/*[@id="id_interface_cellular_status_tab"]').click()
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
                        './html/body/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/input').click()

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
                    print(
                        'SIM1 has been activated back from Optus SIM Manager. Lets check if router has switch back to SIM1 ')
                    driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
                    driver.get('http://192.168.0.1/auth/login.html')

                    login()

                    interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                    time.sleep(2)
                    link_manager = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                    time.sleep(2)
                    link_status = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_status_tab"]').click()
                    A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                    link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                    # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                    # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                    print(A1, 'is', link1)

                    A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                    link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                    # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                    # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                    print(A2, 'is', link2)

                    if link1 == 'Connected':
                        print('The router is connected back to the SIM1')
                        print('Please check the configurations')
                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                        time.sleep(1)
                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                        time.sleep(2)

                        driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                        model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                        print('Modem Model =', model_status)

                        iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                        print(' SIM1 ICCID =', iccid)

                        imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                        print('SIM1 IMEI =', imei)

                        Network_provider = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-operator_1"]').text
                        print('SIM1 Network Provider =', Network_provider)

                        network_type = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-network_type_1"]').text
                        print('SIM1 Network type =', network_type)

                        signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                        print('Signal Strength using SIM1  =', signal_strength)
                        time.sleep(2)

                        print('Router can Switch back to SIM1 after SIM2 has been deactivated')

                    elif link1 == 'Disconnected':
                        print('SIM1 is disconnected')
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
                        link_manager = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                        time.sleep(2)
                        link_status = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_status_tab"]').click()
                        A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                        link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                        # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                        # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                        print(A1, 'is', link1)

                        A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                        link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                        # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                        # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                        print(A2, 'is', link2)

                        if link1 == 'Connected':
                            print('The router is connected back to the SIM1')
                            print('Please check the configurations')
                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                            time.sleep(1)
                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                            time.sleep(2)

                            driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                            model_status = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-modem_model_1"]').text
                            print('Modem Model =', model_status)

                            iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                            print(' SIM1 ICCID =', iccid)

                            imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                            print('SIM1 IMEI =', imei)

                            Network_provider = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-operator_1"]').text
                            print('SIM1 Network Provider =', Network_provider)

                            network_type = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-network_type_1"]').text
                            print('SIM1 Network type =', network_type)

                            signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                            print('Signal Strength using SIM1  =', signal_strength)
                            time.sleep(2)

                            print('Router can Switch back to SIM1 after a Rebooting ')


                        elif link1 == 'Disconnected':
                            print('Router cannot switch back to SIM1 even after rebooting')


                        else:
                            print('Router is Connecting to SIM1. Please wait......')
                            time.sleep(360)
                            print('Please check the configurations')

                            interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                            time.sleep(2)
                            link_manager = driver.find_element_by_xpath(
                                './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                            time.sleep(2)
                            link_status = driver.find_element_by_xpath(
                                './/*[@id="id_interface_link_manager_status_tab"]').click()
                            A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                            link1 = driver.find_element_by_xpath(
                                './/*[@id="id_link_manager-link_status-status_1"]').text
                            # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                            # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                            print(A1, 'is', link1)

                            A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                            link2 = driver.find_element_by_xpath(
                                './/*[@id="id_link_manager-link_status-status_2"]').text
                            # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                            # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                            print(A2, 'is', link2)

                            if link1 == "Connected":

                                driver.find_element_by_xpath(
                                    './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                                time.sleep(1)
                                driver.find_element_by_xpath(
                                    './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                                time.sleep(2)

                                driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                                model_status = driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-modem_model_1"]').text
                                print('Modem Model =', model_status)

                                iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                                print(' SIM1 ICCID =', iccid)

                                imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                                print('SIM1 IMEI =', imei)

                                Network_provider = driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-operator_1"]').text
                                print('SIM1 Network Provider =', Network_provider)

                                network_type = driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-network_type_1"]').text
                                print('SIM1 Network type =', network_type)

                                signal_strength = driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-csq_1"]').text
                                print('Signal Strength using SIM1  =', signal_strength)
                                time.sleep(2)
                                print('Router can Switch back to SIM1 but takes time ( Additional 5 minutes )')

                            elif link1 == 'Disconnected':
                                print('Router cannot switch back to SIM1 even after waiting more than 6 minutes ')

                            else:
                                print('Router tried to connect back to SIM1 but fails ')

                    else:
                        print('Router is Connecting to SIM1. Please wait......')
                        time.sleep(360)
                        print('Please check the configurations')

                        interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                        time.sleep(2)
                        link_manager = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                        time.sleep(2)
                        link_status = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_status_tab"]').click()
                        A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                        link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                        # uptime1 = driver.find_element_by_xpath( './/*[@id="id_link_manager-link_status-link_uptime_1"]').text
                        # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                        print(A1, 'is', link1)

                        A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                        link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                        # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                        # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                        print(A2, 'is', link2)

                        if link1 == "Connected":

                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                            time.sleep(1)
                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                            time.sleep(2)

                            driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                            model_status = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-modem_model_1"]').text
                            print('Modem Model =', model_status)

                            iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                            print(' SIM1 ICCID =', iccid)

                            imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                            print('SIM1 IMEI =', imei)

                            Network_provider = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-operator_1"]').text
                            print('SIM1 Network Provider =', Network_provider)

                            network_type = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-network_type_1"]').text
                            print('SIM1 Network type =', network_type)

                            signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                            print('Signal Strength using SIM1  =', signal_strength)
                            time.sleep(2)
                            print('Router can Switch back to SIM1 but takes time ( Additional 5 minutes )')

                        elif link1 == 'Disconnected':
                            print('Router cannot switch back to SIM1 even after waiting more than 6 minutes ')

                        else:
                            print('Router tried to connect back to SIM1 but fails ')


        else:
            print('Router is connecting to SIM2')
            time.sleep(360)
            print('Please check the configurations')

            interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
            time.sleep(2)
            link_manager = driver.find_element_by_xpath(
                './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
            time.sleep(2)
            link_status = driver.find_element_by_xpath(
                './/*[@id="id_interface_link_manager_status_tab"]').click()
            A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
            link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
            # me1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
            # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
            print(A1, 'is', link1)

            A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
            link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
            # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
            # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
            print(A2, 'is', link2)

            if link2 == 'Connected':
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
                    './html/body/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/input').click()

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
                print(
                    'SIM1 has been activated back from Optus SIM Manager. Lets check if router has switch back to SIM1 ')
                driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
                driver.get('http://192.168.0.1/auth/login.html')

                login()

                interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                time.sleep(2)
                link_manager = driver.find_element_by_xpath(
                    './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                time.sleep(2)
                link_status = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_status_tab"]').click()
                A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                print(A1, 'is', link1)

                A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                print(A2, 'is', link2)

                if link1 == 'Connected':
                    print('The router is connected back to the SIM1')
                    print('Please check the configurations')
                    driver.find_element_by_xpath('.//*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                    time.sleep(1)
                    driver.find_element_by_xpath(
                        './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                    time.sleep(2)

                    driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                    model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                    print('Modem Model =', model_status)

                    iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                    print(' SIM1 ICCID =', iccid)

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

                elif link1 == 'Disconnected':
                    print('SIM1 is disconnected')
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
                    link_manager = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                    time.sleep(2)
                    link_status = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_status_tab"]').click()
                    A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                    link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                    # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                    # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                    print(A1, 'is', link1)

                    A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                    link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                    # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                    # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                    print(A2, 'is', link2)

                    if link1 == 'Connected':
                        print('The router is connected back to the SIM1')
                        print('Please check the configurations')
                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                        time.sleep(1)
                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                        time.sleep(2)

                        driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                        model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                        print('Modem Model =', model_status)

                        iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                        print(' SIM1 ICCID =', iccid)

                        imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                        print('SIM1 IMEI =', imei)

                        Network_provider = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-operator_1"]').text
                        print('SIM1 Network Provider =', Network_provider)

                        network_type = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-network_type_1"]').text
                        print('SIM1 Network type =', network_type)

                        signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                        print('Signal Strength using SIM1  =', signal_strength)
                        time.sleep(2)

                        print('Router can Switch back to SIM1 after a Rebooting ')


                    elif link1 == 'Disconnected':
                        print('Router cannot switch back to SIM1 even after rebooting')


                    else:
                        print('Router is Connecting to SIM1. Please wait......')
                        time.sleep(360)
                        print('Please check the configurations')

                        interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                        time.sleep(2)
                        link_manager = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                        time.sleep(2)
                        link_status = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_status_tab"]').click()
                        A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                        link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                        # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                        # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                        print(A1, 'is', link1)

                        A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                        link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                        # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                        # p2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                        print(A2, 'is', link2)

                        if link1 == "Connected":

                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                            time.sleep(1)
                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                            time.sleep(2)

                            driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                            model_status = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-modem_model_1"]').text
                            print('Modem Model =', model_status)

                            iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                            print(' SIM1 ICCID =', iccid)

                            imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                            print('SIM1 IMEI =', imei)

                            Network_provider = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-operator_1"]').text
                            print('SIM1 Network Provider =', Network_provider)

                            network_type = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-network_type_1"]').text
                            print('SIM1 Network type =', network_type)

                            signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                            print('Signal Strength using SIM1  =', signal_strength)
                            time.sleep(2)
                            print('Router can Switch back to SIM1 but takes time ( Additional 5 minutes )')

                        elif link1 == 'Disconnected':
                            print('Router cannot switch back to SIM1 even after waiting more than 6 minutes ')

                        else:
                            print('Router tried to connect back to SIM1 but fails ')

                else:
                    print('Router is Connecting to SIM1. Please wait......')
                    time.sleep(360)
                    print('Please check the configurations')

                    interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                    time.sleep(2)
                    link_manager = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                    time.sleep(2)
                    link_status = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_status_tab"]').click()
                    A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                    link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                    # e1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                    # p1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                    print(A1, 'is', link1)

                    A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                    link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                    # ptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                    # p2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                    print(A2, 'is', link2)

                    if link1 == "Connected":

                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                        time.sleep(1)
                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                        time.sleep(2)

                        driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                        model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                        print('Modem Model =', model_status)

                        iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                        print(' SIM1 ICCID =', iccid)

                        imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                        print('SIM1 IMEI =', imei)

                        Network_provider = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-operator_1"]').text
                        print('SIM1 Network Provider =', Network_provider)

                        network_type = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-network_type_1"]').text
                        print('SIM1 Network type =', network_type)

                        signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                        print('Signal Strength using SIM1  =', signal_strength)
                        time.sleep(2)
                        print('Router can Switch back to SIM1 but takes time ( Additional 5 minutes )')

                    elif link1 == 'Disconnected':
                        print('Router cannot switch back to SIM1 even after waiting more than 6 minutes ')

                    else:
                        print('Router tried to connect back to SIM1 but fails ')


            elif link2 == 'Disconnected':
                print('The router cannot connect to SIM2')
            else:
                print('The router cannot connect to SIM2')

    elif link1 == 'Disconnected':
        print('The router cannot connect to SIM1')

    else:
        print('Router is connecting to SIM1. Please wait....')
        time.sleep(360)
        interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
        time.sleep(2)
        link_manager = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_menu"]/span[1]').click()
        time.sleep(2)
        link_status = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_status_tab"]').click()
        A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
        link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
        # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
        ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
        print(A1, 'is', link1)

        A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
        link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
        # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
        # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
        print(A2, 'is', link2)

        #%%%%%%%%%%%%%%%%%%%%%%%%%%%
        if link1 == 'Connected':
            print('The router is connected to the SIM1')
            print('Please check the configurations')
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
            time.sleep(2)
            print('Deactivating SIM1 now ')
            # *********************************************************************************
            # **********************connecting to Optus sim Manager*****************************************
            print('Connecting to Optus SIM Card Manager')
            driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
            driver.get(
                'https://optus.jasperwireless.com/provision/jsp/login.jsp;jsessionid=54954536A2F659DBD472B4CD880B5A75')
            # driver.minimize_window()

            username = "simanta"
            password = "thinxtra"

            driver.find_element_by_xpath('.//*[@id="j_username"]').send_keys(username)
            driver.find_element_by_xpath('.//*[@id="j_password"]').send_keys(password)

            driver.find_element_by_xpath(
                './html/body/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/input').click()

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

            print('Waiting on SIM2 to be active. Please wait....... ')
            time.sleep(120)
            print('Connecting back to the Router interface')

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
            # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
            ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
            print(A1, 'is', link1)

            A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
            link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
            # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
            # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
            print(A2, 'is', link2)

            if link2 == 'Connected':
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
                    './html/body/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/input').click()

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
                print(
                    'SIM1 has been activated back from Optus SIM Manager. Lets check if router has switch back to SIM1 ')
                driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
                driver.get('http://192.168.0.1/auth/login.html')

                login()

                interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                time.sleep(2)
                link_manager = driver.find_element_by_xpath(
                    './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
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
                # p2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                print(A2, 'is', link2)

                if link1 == 'Connected':
                    print('The router is connected back to the SIM1')
                    print('Please check the configurations')
                    driver.find_element_by_xpath('.//*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                    time.sleep(1)
                    driver.find_element_by_xpath(
                        './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                    time.sleep(2)

                    driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                    model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                    print('Modem Model =', model_status)

                    iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                    print(' SIM1 ICCID =', iccid)

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

                elif link1 == 'Disconnected':
                    print('SIM1 is disconnected')
                    time.sleep(5)
                    driver.find_element_by_id('id_reboot').click()
                    reboot_sure = driver.find_element_by_id('id_comfirm_yes')
                    reboot_sure.click()
                    print('Rebooting')
                    time.sleep(360)
                    driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
                    driver.get('http://192.168.0.1/auth/login.html')
                    login()

                    interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                    time.sleep(2)
                    link_manager = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                    time.sleep(2)
                    link_status = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_status_tab"]').click()
                    A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                    link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                    # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                    # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                    print(A1, 'is', link1)

                    A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                    link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                    # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                    # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                    print(A2, 'is', link2)

                    if link1 == 'Connected':
                        print('The router is connected back to the SIM1')
                        print('Please check the configurations')
                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                        time.sleep(1)
                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                        time.sleep(2)

                        driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                        model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                        print('Modem Model =', model_status)

                        iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                        print(' SIM1 ICCID =', iccid)

                        imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                        print('SIM1 IMEI =', imei)

                        Network_provider = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-operator_1"]').text
                        print('SIM1 Network Provider =', Network_provider)

                        network_type = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-network_type_1"]').text
                        print('SIM1 Network type =', network_type)

                        signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                        print('Signal Strength using SIM1  =', signal_strength)
                        time.sleep(2)

                        print('Router can Switch back to SIM1 after a Rebooting ')


                    elif link1 == 'Disconnected':
                        print('Router cannot switch back to SIM1 even after rebooting')


                    else:
                        print('Router is Connecting to SIM1. Please wait......')
                        time.sleep(360)
                        print('Please check the configurations')

                        interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                        time.sleep(2)
                        link_manager = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                        time.sleep(2)
                        link_status = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_status_tab"]').click()
                        A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                        link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                        # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                        # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                        print(A1, 'is', link1)

                        A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                        link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                        # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                        # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                        print(A2, 'is', link2)

                        if link1 == "Connected":

                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                            time.sleep(1)
                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                            time.sleep(2)

                            driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                            model_status = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-modem_model_1"]').text
                            print('Modem Model =', model_status)

                            iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                            print(' SIM1 ICCID =', iccid)

                            imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                            print('SIM1 IMEI =', imei)

                            Network_provider = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-operator_1"]').text
                            print('SIM1 Network Provider =', Network_provider)

                            network_type = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-network_type_1"]').text
                            print('SIM1 Network type =', network_type)

                            signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                            print('Signal Strength using SIM1  =', signal_strength)
                            time.sleep(2)
                            print('Router can Switch back to SIM1 but takes time ( Additional 5 minutes )')

                        elif link1 == 'Disconnected':
                            print('Router cannot switch back to SIM1 even after waiting more than 6 minutes ')

                        else:
                            print('Router tried to connect back to SIM1 but fails ')

                else:
                    print('Router is Connecting to SIM1. Please wait......')
                    time.sleep(360)
                    print('Please check the configurations')

                    interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                    time.sleep(2)
                    link_manager = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                    time.sleep(2)
                    link_status = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_status_tab"]').click()
                    A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                    link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                    # me1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                    # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                    print(A1, 'is', link1)

                    A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                    link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                    # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                    # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                    print(A2, 'is', link2)

                    if link1 == "Connected":

                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                        time.sleep(1)
                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                        time.sleep(2)

                        driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                        model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                        print('Modem Model =', model_status)

                        iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                        print(' SIM1 ICCID =', iccid)

                        imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                        print('SIM1 IMEI =', imei)

                        Network_provider = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-operator_1"]').text
                        print('SIM1 Network Provider =', Network_provider)

                        network_type = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-network_type_1"]').text
                        print('SIM1 Network type =', network_type)

                        signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                        print('Signal Strength using SIM1  =', signal_strength)
                        time.sleep(2)
                        print('Router can Switch back to SIM1 but takes time ( Additional 5 minutes )')

                    elif link1 == 'Disconnected':
                        print('Router cannot switch back to SIM1 even after waiting more than 6 minutes ')

                    else:
                        print('Router tried to connect back to SIM1 but fails ')

            elif link2 == 'Disconnected':
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
                link_manager = driver.find_element_by_xpath(
                    './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                time.sleep(2)
                link_status = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_status_tab"]').click()
                A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                print(A1, 'is', link1)

                A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                print(A2, 'is', link2)

                if link2 == 'Connected':
                    print('Router is connected to SIM2')
                    cellular = driver.find_element_by_xpath('.//*[@id="id_interface_cellular_menu"]/span[1]').click()
                    time.sleep(1)
                    cellular_status = driver.find_element_by_xpath(
                        './/*[@id="id_interface_cellular_status_tab"]').click()
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
                        './html/body/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/input').click()

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
                    print(
                        'SIM1 has been activated back from Optus SIM Manager. Lets check if router has switch back to SIM1 ')
                    driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
                    driver.get('http://192.168.0.1/auth/login.html')

                    login()

                    interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                    time.sleep(2)
                    link_manager = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                    time.sleep(2)
                    link_status = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_status_tab"]').click()
                    A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                    link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                    # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                    # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                    print(A1, 'is', link1)

                    A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                    link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                    # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                    # p2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                    print(A2, 'is', link2)

                    if link1 == 'Connected':
                        print('The router is connected back to the SIM1')
                        print('Please check the configurations')
                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                        time.sleep(1)
                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                        time.sleep(2)

                        driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                        model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                        print('Modem Model =', model_status)

                        iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                        print(' SIM1 ICCID =', iccid)

                        imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                        print('SIM1 IMEI =', imei)

                        Network_provider = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-operator_1"]').text
                        print('SIM1 Network Provider =', Network_provider)

                        network_type = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-network_type_1"]').text
                        print('SIM1 Network type =', network_type)

                        signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                        print('Signal Strength using SIM1  =', signal_strength)
                        time.sleep(2)

                        print('Router can Switch back to SIM1 after SIM2 has been deactivated')

                    elif link1 == 'Disconnected':
                        print('SIM1 is disconnected')
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
                        link_manager = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                        time.sleep(2)
                        link_status = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_status_tab"]').click()
                        A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                        link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                        # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                        # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                        print(A1, 'is', link1)

                        A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                        link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                        # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                        # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                        print(A2, 'is', link2)

                        if link1 == 'Connected':
                            print('The router is connected back to the SIM1')
                            print('Please check the configurations')
                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                            time.sleep(1)
                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                            time.sleep(2)

                            driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                            model_status = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-modem_model_1"]').text
                            print('Modem Model =', model_status)

                            iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                            print(' SIM1 ICCID =', iccid)

                            imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                            print('SIM1 IMEI =', imei)

                            Network_provider = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-operator_1"]').text
                            print('SIM1 Network Provider =', Network_provider)

                            network_type = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-network_type_1"]').text
                            print('SIM1 Network type =', network_type)

                            signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                            print('Signal Strength using SIM1  =', signal_strength)
                            time.sleep(2)

                            print('Router can Switch back to SIM1 after a Rebooting ')


                        elif link1 == 'Disconnected':
                            print('Router cannot switch back to SIM1 even after rebooting')


                        else:
                            print('Router is Connecting to SIM1. Please wait......')
                            time.sleep(360)
                            print('Please check the configurations')

                            interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                            time.sleep(2)
                            link_manager = driver.find_element_by_xpath(
                                './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                            time.sleep(2)
                            link_status = driver.find_element_by_xpath(
                                './/*[@id="id_interface_link_manager_status_tab"]').click()
                            A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                            link1 = driver.find_element_by_xpath(
                                './/*[@id="id_link_manager-link_status-status_1"]').text
                            # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                            # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                            print(A1, 'is', link1)

                            A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                            link2 = driver.find_element_by_xpath(
                                './/*[@id="id_link_manager-link_status-status_2"]').text
                            # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                            # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                            print(A2, 'is', link2)

                            if link1 == "Connected":

                                driver.find_element_by_xpath(
                                    './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                                time.sleep(1)
                                driver.find_element_by_xpath(
                                    './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                                time.sleep(2)

                                driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                                model_status = driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-modem_model_1"]').text
                                print('Modem Model =', model_status)

                                iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                                print(' SIM1 ICCID =', iccid)

                                imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                                print('SIM1 IMEI =', imei)

                                Network_provider = driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-operator_1"]').text
                                print('SIM1 Network Provider =', Network_provider)

                                network_type = driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-network_type_1"]').text
                                print('SIM1 Network type =', network_type)

                                signal_strength = driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-csq_1"]').text
                                print('Signal Strength using SIM1  =', signal_strength)
                                time.sleep(2)
                                print('Router can Switch back to SIM1 but takes time ( Additional 5 minutes )')

                            elif link1 == 'Disconnected':
                                print('Router cannot switch back to SIM1 even after waiting more than 6 minutes ')

                            else:
                                print('Router tried to connect back to SIM1 but fails ')

                    else:
                        print('Router is Connecting to SIM1. Please wait......')
                        time.sleep(360)
                        print('Please check the configurations')

                        interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                        time.sleep(2)
                        link_manager = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                        time.sleep(2)
                        link_status = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_status_tab"]').click()
                        A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                        link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                        # me1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                        # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                        print(A1, 'is', link1)

                        A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                        link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                        # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                        # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                        print(A2, 'is', link2)

                        if link1 == "Connected":

                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                            time.sleep(1)
                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                            time.sleep(2)

                            driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                            model_status = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-modem_model_1"]').text
                            print('Modem Model =', model_status)

                            iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                            print(' SIM1 ICCID =', iccid)

                            imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                            print('SIM1 IMEI =', imei)

                            Network_provider = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-operator_1"]').text
                            print('SIM1 Network Provider =', Network_provider)

                            network_type = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-network_type_1"]').text
                            print('SIM1 Network type =', network_type)

                            signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                            print('Signal Strength using SIM1  =', signal_strength)
                            time.sleep(2)
                            print('Router can Switch back to SIM1 but takes time ( Additional 5 minutes )')

                        elif link1 == 'Disconnected':
                            print('Router cannot switch back to SIM1 even after waiting more than 6 minutes ')

                        else:
                            print('Router tried to connect back to SIM1 but fails ')

                elif link2 == 'Disconnected':
                    print('Router cannot connect to SIM2 even after rebooting')

                else:
                    print('Router is Connecting to SIM2. Please wait......')
                    time.sleep(360)
                    print('Please check the configurations')

                    interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                    time.sleep(2)
                    link_manager = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                    time.sleep(2)
                    link_status = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_status_tab"]').click()
                    A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                    link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                    # me1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                    # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                    print(A1, 'is', link1)

                    A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                    link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                    # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                    # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                    print(A2, 'is', link2)

                    if link2 == 'Connected':
                        print('Router is connected to SIM2')
                        cellular = driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_menu"]/span[1]').click()
                        time.sleep(1)
                        cellular_status = driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_status_tab"]').click()
                        time.sleep(2)

                        B1 = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()
                        model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                        print('Modem Model =', model_status)

                        iccid1 = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                        print('ICCID after deactivating SIM1 =', iccid1)

                        imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                        print('IMEI after deactivating SIM1 =', imei)

                        Network_provider = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-operator_1"]').text
                        print('Network Provider after deactivating SIM1 =', Network_provider)

                        network_type = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-network_type_1"]').text
                        print('Network type after deactivating SIM1 =', network_type)

                        signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                        print('Signal_Strength after deactivating SIM1 =', signal_strength)

                        print('Activating SIM1 back on. Please wait......')

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
                            './html/body/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/input').click()

                        time.sleep(5)
                        driver.find_element_by_id('jw-searchfield-1021-inputEl').send_keys(iccid)
                        driver.find_element_by_xpath(
                            './/*[@id="jw-searchfield-1021-triggerWrap"]/tbody/tr/td[1]').click()
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
                        print(
                            'SIM1 has been activated back from Optus SIM Manager. Lets check if router has switch back to SIM1 ')
                        driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
                        driver.get('http://192.168.0.1/auth/login.html')

                        login()

                        interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                        time.sleep(2)
                        link_manager = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                        time.sleep(2)
                        link_status = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_status_tab"]').click()
                        A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                        link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                        # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                        # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                        print(A1, 'is', link1)

                        A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                        link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                        # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                        # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                        print(A2, 'is', link2)

                        if link1 == 'Connected':
                            print('The router is connected back to the SIM1')
                            print('Please check the configurations')
                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                            time.sleep(1)
                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                            time.sleep(2)

                            driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                            model_status = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-modem_model_1"]').text
                            print('Modem Model =', model_status)

                            iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                            print(' SIM1 ICCID =', iccid)

                            imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                            print('SIM1 IMEI =', imei)

                            Network_provider = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-operator_1"]').text
                            print('SIM1 Network Provider =', Network_provider)

                            network_type = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-network_type_1"]').text
                            print('SIM1 Network type =', network_type)

                            signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                            print('Signal Strength using SIM1  =', signal_strength)
                            time.sleep(2)

                            print('Router can Switch back to SIM1 after SIM2 has been deactivated')

                        elif link1 == 'Disconnected':
                            print('SIM1 is disconnected')
                            time.sleep(5)
                            driver.find_element_by_id('id_reboot').click()
                            reboot_sure = driver.find_element_by_id('id_comfirm_yes')
                            reboot_sure.click()
                            print('Rebooting')
                            time.sleep(300)
                            driver = webdriver.Chrome(
                                "C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
                            driver.get('http://192.168.0.1/auth/login.html')
                            login()

                            interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                            time.sleep(2)
                            link_manager = driver.find_element_by_xpath(
                                './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                            time.sleep(2)
                            link_status = driver.find_element_by_xpath(
                                './/*[@id="id_interface_link_manager_status_tab"]').click()
                            A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                            link1 = driver.find_element_by_xpath(
                                './/*[@id="id_link_manager-link_status-status_1"]').text
                            # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                            # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                            print(A1, 'is', link1)

                            A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                            link2 = driver.find_element_by_xpath(
                                './/*[@id="id_link_manager-link_status-status_2"]').text
                            # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                            # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                            print(A2, 'is', link2)

                            if link1 == 'Connected':
                                print('The router is connected back to the SIM1')
                                print('Please check the configurations')
                                driver.find_element_by_xpath(
                                    './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                                time.sleep(1)
                                driver.find_element_by_xpath(
                                    './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                                time.sleep(2)

                                driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                                model_status = driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-modem_model_1"]').text
                                print('Modem Model =', model_status)

                                iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                                print(' SIM1 ICCID =', iccid)

                                imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                                print('SIM1 IMEI =', imei)

                                Network_provider = driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-operator_1"]').text
                                print('SIM1 Network Provider =', Network_provider)

                                network_type = driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-network_type_1"]').text
                                print('SIM1 Network type =', network_type)

                                signal_strength = driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-csq_1"]').text
                                print('Signal Strength using SIM1  =', signal_strength)
                                time.sleep(2)

                                print('Router can Switch back to SIM1 after a Rebooting ')


                            elif link1 == 'Disconnected':
                                print('Router cannot switch back to SIM1 even after rebooting')


                            else:
                                print('Router is Connecting to SIM1. Please wait......')
                                time.sleep(360)
                                print('Please check the configurations')

                                interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                                time.sleep(2)
                                link_manager = driver.find_element_by_xpath(
                                    './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                                time.sleep(2)
                                link_status = driver.find_element_by_xpath(
                                    './/*[@id="id_interface_link_manager_status_tab"]').click()
                                A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                                link1 = driver.find_element_by_xpath(
                                    './/*[@id="id_link_manager-link_status-status_1"]').text
                                # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                                # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                                print(A1, 'is', link1)

                                A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                                link2 = driver.find_element_by_xpath(
                                    './/*[@id="id_link_manager-link_status-status_2"]').text
                                # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                                # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                                print(A2, 'is', link2)

                                if link1 == "Connected":

                                    driver.find_element_by_xpath(
                                        './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                                    time.sleep(1)
                                    driver.find_element_by_xpath(
                                        './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                                    time.sleep(2)

                                    driver.find_element_by_xpath(
                                        './/*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                                    model_status = driver.find_element_by_xpath(
                                        './/*[@id="id_cellular-status-modem_model_1"]').text
                                    print('Modem Model =', model_status)

                                    iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                                    print(' SIM1 ICCID =', iccid)

                                    imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                                    print('SIM1 IMEI =', imei)

                                    Network_provider = driver.find_element_by_xpath(
                                        './/*[@id="id_cellular-status-operator_1"]').text
                                    print('SIM1 Network Provider =', Network_provider)

                                    network_type = driver.find_element_by_xpath(
                                        './/*[@id="id_cellular-status-network_type_1"]').text
                                    print('SIM1 Network type =', network_type)

                                    signal_strength = driver.find_element_by_xpath(
                                        './/*[@id="id_cellular-status-csq_1"]').text
                                    print('Signal Strength using SIM1  =', signal_strength)
                                    time.sleep(2)
                                    print('Router can Switch back to SIM1 but takes time ( Additional 5 minutes )')

                                elif link1 == 'Disconnected':
                                    print('Router cannot switch back to SIM1 even after waiting more than 6 minutes ')

                                else:
                                    print('Router tried to connect back to SIM1 but fails ')

                        else:
                            print('Router is Connecting to SIM1. Please wait......')
                            time.sleep(360)
                            print('Please check the configurations')

                            interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                            time.sleep(2)
                            link_manager = driver.find_element_by_xpath(
                                './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                            time.sleep(2)
                            link_status = driver.find_element_by_xpath(
                                './/*[@id="id_interface_link_manager_status_tab"]').click()
                            A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                            link1 = driver.find_element_by_xpath(
                                './/*[@id="id_link_manager-link_status-status_1"]').text
                            # uptime1 = driver.find_element_by_xpath( './/*[@id="id_link_manager-link_status-link_uptime_1"]').text
                            # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                            print(A1, 'is', link1)

                            A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                            link2 = driver.find_element_by_xpath(
                                './/*[@id="id_link_manager-link_status-status_2"]').text
                            # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                            # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                            print(A2, 'is', link2)

                            if link1 == "Connected":

                                driver.find_element_by_xpath(
                                    './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                                time.sleep(1)
                                driver.find_element_by_xpath(
                                    './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                                time.sleep(2)

                                driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                                model_status = driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-modem_model_1"]').text
                                print('Modem Model =', model_status)

                                iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                                print(' SIM1 ICCID =', iccid)

                                imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                                print('SIM1 IMEI =', imei)

                                Network_provider = driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-operator_1"]').text
                                print('SIM1 Network Provider =', Network_provider)

                                network_type = driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-network_type_1"]').text
                                print('SIM1 Network type =', network_type)

                                signal_strength = driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-csq_1"]').text
                                print('Signal Strength using SIM1  =', signal_strength)
                                time.sleep(2)
                                print('Router can Switch back to SIM1 but takes time ( Additional 5 minutes )')

                            elif link1 == 'Disconnected':
                                print('Router cannot switch back to SIM1 even after waiting more than 6 minutes ')

                            else:
                                print('Router tried to connect back to SIM1 but fails ')


            else:
                print('Router is connecting to SIM2')
                time.sleep(360)
                print('Please check the configurations')

                interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                time.sleep(2)
                link_manager = driver.find_element_by_xpath(
                    './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                time.sleep(2)
                link_status = driver.find_element_by_xpath(
                    './/*[@id="id_interface_link_manager_status_tab"]').click()
                A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                # me1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                print(A1, 'is', link1)

                A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                print(A2, 'is', link2)

                if link2 == 'Connected':
                    print('Router is connected to SIM2')
                    cellular = driver.find_element_by_xpath('.//*[@id="id_interface_cellular_menu"]/span[1]').click()
                    time.sleep(1)
                    cellular_status = driver.find_element_by_xpath(
                        './/*[@id="id_interface_cellular_status_tab"]').click()
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
                        './html/body/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/input').click()

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
                    print(
                        'SIM1 has been activated back from Optus SIM Manager. Lets check if router has switch back to SIM1 ')
                    driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
                    driver.get('http://192.168.0.1/auth/login.html')

                    login()

                    interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                    time.sleep(2)
                    link_manager = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                    time.sleep(2)
                    link_status = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_status_tab"]').click()
                    A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                    link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                    # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                    # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                    print(A1, 'is', link1)

                    A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                    link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                    # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                    # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                    print(A2, 'is', link2)

                    if link1 == 'Connected':
                        print('The router is connected back to the SIM1')
                        print('Please check the configurations')
                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                        time.sleep(1)
                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                        time.sleep(2)

                        driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                        model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                        print('Modem Model =', model_status)

                        iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                        print(' SIM1 ICCID =', iccid)

                        imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                        print('SIM1 IMEI =', imei)

                        Network_provider = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-operator_1"]').text
                        print('SIM1 Network Provider =', Network_provider)

                        network_type = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-network_type_1"]').text
                        print('SIM1 Network type =', network_type)

                        signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                        print('Signal Strength using SIM1  =', signal_strength)
                        time.sleep(2)

                        print('Router can Switch back to SIM1 after SIM2 has been deactivated')

                    elif link1 == 'Disconnected':
                        print('SIM1 is disconnected')
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
                        link_manager = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                        time.sleep(2)
                        link_status = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_status_tab"]').click()
                        A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                        link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                        # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                        # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                        print(A1, 'is', link1)

                        A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                        link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                        # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                        # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                        print(A2, 'is', link2)

                        if link1 == 'Connected':
                            print('The router is connected back to the SIM1')
                            print('Please check the configurations')
                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                            time.sleep(1)
                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                            time.sleep(2)

                            driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                            model_status = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-modem_model_1"]').text
                            print('Modem Model =', model_status)

                            iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                            print(' SIM1 ICCID =', iccid)

                            imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                            print('SIM1 IMEI =', imei)

                            Network_provider = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-operator_1"]').text
                            print('SIM1 Network Provider =', Network_provider)

                            network_type = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-network_type_1"]').text
                            print('SIM1 Network type =', network_type)

                            signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                            print('Signal Strength using SIM1  =', signal_strength)
                            time.sleep(2)

                            print('Router can Switch back to SIM1 after a Rebooting ')


                        elif link1 == 'Disconnected':
                            print('Router cannot switch back to SIM1 even after rebooting')


                        else:
                            print('Router is Connecting to SIM1. Please wait......')
                            time.sleep(360)
                            print('Please check the configurations')

                            interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                            time.sleep(2)
                            link_manager = driver.find_element_by_xpath(
                                './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                            time.sleep(2)
                            link_status = driver.find_element_by_xpath(
                                './/*[@id="id_interface_link_manager_status_tab"]').click()
                            A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                            link1 = driver.find_element_by_xpath(
                                './/*[@id="id_link_manager-link_status-status_1"]').text
                            # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                            # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                            print(A1, 'is', link1)

                            A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                            link2 = driver.find_element_by_xpath(
                                './/*[@id="id_link_manager-link_status-status_2"]').text
                            # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                            # p2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                            print(A2, 'is', link2)

                            if link1 == "Connected":

                                driver.find_element_by_xpath(
                                    './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                                time.sleep(1)
                                driver.find_element_by_xpath(
                                    './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                                time.sleep(2)

                                driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                                model_status = driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-modem_model_1"]').text
                                print('Modem Model =', model_status)

                                iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                                print(' SIM1 ICCID =', iccid)

                                imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                                print('SIM1 IMEI =', imei)

                                Network_provider = driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-operator_1"]').text
                                print('SIM1 Network Provider =', Network_provider)

                                network_type = driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-network_type_1"]').text
                                print('SIM1 Network type =', network_type)

                                signal_strength = driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-csq_1"]').text
                                print('Signal Strength using SIM1  =', signal_strength)
                                time.sleep(2)
                                print('Router can Switch back to SIM1 but takes time ( Additional 5 minutes )')

                            elif link1 == 'Disconnected':
                                print('Router cannot switch back to SIM1 even after waiting more than 6 minutes ')

                            else:
                                print('Router tried to connect back to SIM1 but fails ')

                    else:
                        print('Router is Connecting to SIM1. Please wait......')
                        time.sleep(360)
                        print('Please check the configurations')

                        interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                        time.sleep(2)
                        link_manager = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                        time.sleep(2)
                        link_status = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_status_tab"]').click()
                        A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                        link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                        # e1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                        # p1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                        print(A1, 'is', link1)

                        A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                        link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                        # ptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                        # p2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                        print(A2, 'is', link2)

                        if link1 == "Connected":

                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                            time.sleep(1)
                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                            time.sleep(2)

                            driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                            model_status = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-modem_model_1"]').text
                            print('Modem Model =', model_status)

                            iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                            print(' SIM1 ICCID =', iccid)

                            imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                            print('SIM1 IMEI =', imei)

                            Network_provider = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-operator_1"]').text
                            print('SIM1 Network Provider =', Network_provider)

                            network_type = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-network_type_1"]').text
                            print('SIM1 Network type =', network_type)

                            signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                            print('Signal Strength using SIM1  =', signal_strength)
                            time.sleep(2)
                            print('Router can Switch back to SIM1 but takes time ( Additional 5 minutes )')

                        elif link1 == 'Disconnected':
                            print('Router cannot switch back to SIM1 even after waiting more than 6 minutes ')

                        else:
                            print('Router tried to connect back to SIM1 but fails ')


                elif link2 == 'Disconnected':
                    print('The router cannot connect to SIM2')
                else:
                    print('The router cannot connect to SIM2')



        elif link1 == 'Disconnected':
            print('SIM1 is Disconnected. Router  cannot connect to SIM1')

        else:
            print('SIM1 is still connecting. Router cannot connect to SIM1')


else:
    print('Router is connecting to SIM1. Please wait....')
    time.sleep(360)
    interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
    time.sleep(2)
    link_manager = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_menu"]/span[1]').click()
    time.sleep(2)
    link_status = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_status_tab"]').click()
    A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
    link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
    # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
    ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
    print(A1, 'is', link1)

    A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
    link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
    # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
    # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
    print(A2, 'is', link2)

    # %%%%%%%%%%%%%%%%%%%%%%%%%%%
    if link1 == 'Connected':
        print('The router is connected to the SIM1')
        print('Please check the configurations')
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
        time.sleep(2)
        print('Deactivating SIM1 now ')
        # *********************************************************************************
        # **********************connecting to Optus sim Manager*****************************************
        print('Connecting to Optus SIM Card Manager')
        driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
        driver.get(
            'https://optus.jasperwireless.com/provision/jsp/login.jsp;jsessionid=54954536A2F659DBD472B4CD880B5A75')
        # driver.minimize_window()

        username = "simanta"
        password = "thinxtra"

        driver.find_element_by_xpath('.//*[@id="j_username"]').send_keys(username)
        driver.find_element_by_xpath('.//*[@id="j_password"]').send_keys(password)

        driver.find_element_by_xpath(
            './html/body/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/input').click()

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

        print('Waiting on SIM2 to be active. Please wait....... ')
        time.sleep(120)
        print('Connecting back to the Router interface')

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
        # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
        ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
        print(A1, 'is', link1)

        A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
        link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
        # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
        # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
        print(A2, 'is', link2)

        if link2 == 'Connected':
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
                './html/body/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/input').click()

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
            print(
                'SIM1 has been activated back from Optus SIM Manager. Lets check if router has switch back to SIM1 ')
            driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
            driver.get('http://192.168.0.1/auth/login.html')

            login()

            interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
            time.sleep(2)
            link_manager = driver.find_element_by_xpath(
                './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
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
            # p2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
            print(A2, 'is', link2)

            if link1 == 'Connected':
                print('The router is connected back to the SIM1')
                print('Please check the configurations')
                driver.find_element_by_xpath('.//*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                time.sleep(1)
                driver.find_element_by_xpath(
                    './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                time.sleep(2)

                driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                print('Modem Model =', model_status)

                iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                print(' SIM1 ICCID =', iccid)

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

            elif link1 == 'Disconnected':
                print('SIM1 is disconnected')
                time.sleep(5)
                driver.find_element_by_id('id_reboot').click()
                reboot_sure = driver.find_element_by_id('id_comfirm_yes')
                reboot_sure.click()
                print('Rebooting')
                time.sleep(360)
                driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
                driver.get('http://192.168.0.1/auth/login.html')
                login()

                interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                time.sleep(2)
                link_manager = driver.find_element_by_xpath(
                    './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                time.sleep(2)
                link_status = driver.find_element_by_xpath(
                    './/*[@id="id_interface_link_manager_status_tab"]').click()
                A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                print(A1, 'is', link1)

                A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                print(A2, 'is', link2)

                if link1 == 'Connected':
                    print('The router is connected back to the SIM1')
                    print('Please check the configurations')
                    driver.find_element_by_xpath(
                        './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                    time.sleep(1)
                    driver.find_element_by_xpath(
                        './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                    time.sleep(2)

                    driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                    model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                    print('Modem Model =', model_status)

                    iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                    print(' SIM1 ICCID =', iccid)

                    imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                    print('SIM1 IMEI =', imei)

                    Network_provider = driver.find_element_by_xpath(
                        './/*[@id="id_cellular-status-operator_1"]').text
                    print('SIM1 Network Provider =', Network_provider)

                    network_type = driver.find_element_by_xpath(
                        './/*[@id="id_cellular-status-network_type_1"]').text
                    print('SIM1 Network type =', network_type)

                    signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                    print('Signal Strength using SIM1  =', signal_strength)
                    time.sleep(2)

                    print('Router can Switch back to SIM1 after a Rebooting ')


                elif link1 == 'Disconnected':
                    print('Router cannot switch back to SIM1 even after rebooting')


                else:
                    print('Router is Connecting to SIM1. Please wait......')
                    time.sleep(360)
                    print('Please check the configurations')

                    interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                    time.sleep(2)
                    link_manager = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                    time.sleep(2)
                    link_status = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_status_tab"]').click()
                    A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                    link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                    # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                    # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                    print(A1, 'is', link1)

                    A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                    link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                    # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                    # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                    print(A2, 'is', link2)

                    if link1 == "Connected":

                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                        time.sleep(1)
                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                        time.sleep(2)

                        driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                        model_status = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-modem_model_1"]').text
                        print('Modem Model =', model_status)

                        iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                        print(' SIM1 ICCID =', iccid)

                        imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                        print('SIM1 IMEI =', imei)

                        Network_provider = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-operator_1"]').text
                        print('SIM1 Network Provider =', Network_provider)

                        network_type = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-network_type_1"]').text
                        print('SIM1 Network type =', network_type)

                        signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                        print('Signal Strength using SIM1  =', signal_strength)
                        time.sleep(2)
                        print('Router can Switch back to SIM1 but takes time ( Additional 5 minutes )')

                    elif link1 == 'Disconnected':
                        print('Router cannot switch back to SIM1 even after waiting more than 6 minutes ')

                    else:
                        print('Router tried to connect back to SIM1 but fails ')

            else:
                print('Router is Connecting to SIM1. Please wait......')
                time.sleep(360)
                print('Please check the configurations')

                interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                time.sleep(2)
                link_manager = driver.find_element_by_xpath(
                    './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                time.sleep(2)
                link_status = driver.find_element_by_xpath(
                    './/*[@id="id_interface_link_manager_status_tab"]').click()
                A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                # me1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                print(A1, 'is', link1)

                A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                print(A2, 'is', link2)

                if link1 == "Connected":

                    driver.find_element_by_xpath(
                        './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                    time.sleep(1)
                    driver.find_element_by_xpath(
                        './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                    time.sleep(2)

                    driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                    model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                    print('Modem Model =', model_status)

                    iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                    print(' SIM1 ICCID =', iccid)

                    imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                    print('SIM1 IMEI =', imei)

                    Network_provider = driver.find_element_by_xpath(
                        './/*[@id="id_cellular-status-operator_1"]').text
                    print('SIM1 Network Provider =', Network_provider)

                    network_type = driver.find_element_by_xpath(
                        './/*[@id="id_cellular-status-network_type_1"]').text
                    print('SIM1 Network type =', network_type)

                    signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                    print('Signal Strength using SIM1  =', signal_strength)
                    time.sleep(2)
                    print('Router can Switch back to SIM1 but takes time ( Additional 5 minutes )')

                elif link1 == 'Disconnected':
                    print('Router cannot switch back to SIM1 even after waiting more than 6 minutes ')

                else:
                    print('Router tried to connect back to SIM1 but fails ')

        elif link2 == 'Disconnected':
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
            link_manager = driver.find_element_by_xpath(
                './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
            time.sleep(2)
            link_status = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_status_tab"]').click()
            A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
            link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
            # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
            ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
            print(A1, 'is', link1)

            A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
            link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
            # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
            # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
            print(A2, 'is', link2)

            if link2 == 'Connected':
                print('Router is connected to SIM2')
                cellular = driver.find_element_by_xpath('.//*[@id="id_interface_cellular_menu"]/span[1]').click()
                time.sleep(1)
                cellular_status = driver.find_element_by_xpath(
                    './/*[@id="id_interface_cellular_status_tab"]').click()
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
                    './html/body/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/input').click()

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
                print(
                    'SIM1 has been activated back from Optus SIM Manager. Lets check if router has switch back to SIM1 ')
                driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
                driver.get('http://192.168.0.1/auth/login.html')

                login()

                interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                time.sleep(2)
                link_manager = driver.find_element_by_xpath(
                    './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                time.sleep(2)
                link_status = driver.find_element_by_xpath(
                    './/*[@id="id_interface_link_manager_status_tab"]').click()
                A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                print(A1, 'is', link1)

                A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                # p2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                print(A2, 'is', link2)

                if link1 == 'Connected':
                    print('The router is connected back to the SIM1')
                    print('Please check the configurations')
                    driver.find_element_by_xpath(
                        './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                    time.sleep(1)
                    driver.find_element_by_xpath(
                        './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                    time.sleep(2)

                    driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                    model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                    print('Modem Model =', model_status)

                    iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                    print(' SIM1 ICCID =', iccid)

                    imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                    print('SIM1 IMEI =', imei)

                    Network_provider = driver.find_element_by_xpath(
                        './/*[@id="id_cellular-status-operator_1"]').text
                    print('SIM1 Network Provider =', Network_provider)

                    network_type = driver.find_element_by_xpath(
                        './/*[@id="id_cellular-status-network_type_1"]').text
                    print('SIM1 Network type =', network_type)

                    signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                    print('Signal Strength using SIM1  =', signal_strength)
                    time.sleep(2)

                    print('Router can Switch back to SIM1 after SIM2 has been deactivated')

                elif link1 == 'Disconnected':
                    print('SIM1 is disconnected')
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
                    link_manager = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                    time.sleep(2)
                    link_status = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_status_tab"]').click()
                    A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                    link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                    # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                    # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                    print(A1, 'is', link1)

                    A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                    link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                    # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                    # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                    print(A2, 'is', link2)

                    if link1 == 'Connected':
                        print('The router is connected back to the SIM1')
                        print('Please check the configurations')
                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                        time.sleep(1)
                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                        time.sleep(2)

                        driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                        model_status = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-modem_model_1"]').text
                        print('Modem Model =', model_status)

                        iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                        print(' SIM1 ICCID =', iccid)

                        imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                        print('SIM1 IMEI =', imei)

                        Network_provider = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-operator_1"]').text
                        print('SIM1 Network Provider =', Network_provider)

                        network_type = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-network_type_1"]').text
                        print('SIM1 Network type =', network_type)

                        signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                        print('Signal Strength using SIM1  =', signal_strength)
                        time.sleep(2)

                        print('Router can Switch back to SIM1 after a Rebooting ')


                    elif link1 == 'Disconnected':
                        print('Router cannot switch back to SIM1 even after rebooting')


                    else:
                        print('Router is Connecting to SIM1. Please wait......')
                        time.sleep(360)
                        print('Please check the configurations')

                        interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                        time.sleep(2)
                        link_manager = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                        time.sleep(2)
                        link_status = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_status_tab"]').click()
                        A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                        link1 = driver.find_element_by_xpath(
                            './/*[@id="id_link_manager-link_status-status_1"]').text
                        # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                        # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                        print(A1, 'is', link1)

                        A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                        link2 = driver.find_element_by_xpath(
                            './/*[@id="id_link_manager-link_status-status_2"]').text
                        # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                        # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                        print(A2, 'is', link2)

                        if link1 == "Connected":

                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                            time.sleep(1)
                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                            time.sleep(2)

                            driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                            model_status = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-modem_model_1"]').text
                            print('Modem Model =', model_status)

                            iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                            print(' SIM1 ICCID =', iccid)

                            imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                            print('SIM1 IMEI =', imei)

                            Network_provider = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-operator_1"]').text
                            print('SIM1 Network Provider =', Network_provider)

                            network_type = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-network_type_1"]').text
                            print('SIM1 Network type =', network_type)

                            signal_strength = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-csq_1"]').text
                            print('Signal Strength using SIM1  =', signal_strength)
                            time.sleep(2)
                            print('Router can Switch back to SIM1 but takes time ( Additional 5 minutes )')

                        elif link1 == 'Disconnected':
                            print('Router cannot switch back to SIM1 even after waiting more than 6 minutes ')

                        else:
                            print('Router tried to connect back to SIM1 but fails ')

                else:
                    print('Router is Connecting to SIM1. Please wait......')
                    time.sleep(360)
                    print('Please check the configurations')

                    interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                    time.sleep(2)
                    link_manager = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                    time.sleep(2)
                    link_status = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_status_tab"]').click()
                    A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                    link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                    # me1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                    # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                    print(A1, 'is', link1)

                    A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                    link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                    # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                    # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                    print(A2, 'is', link2)

                    if link1 == "Connected":

                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                        time.sleep(1)
                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                        time.sleep(2)

                        driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                        model_status = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-modem_model_1"]').text
                        print('Modem Model =', model_status)

                        iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                        print(' SIM1 ICCID =', iccid)

                        imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                        print('SIM1 IMEI =', imei)

                        Network_provider = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-operator_1"]').text
                        print('SIM1 Network Provider =', Network_provider)

                        network_type = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-network_type_1"]').text
                        print('SIM1 Network type =', network_type)

                        signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                        print('Signal Strength using SIM1  =', signal_strength)
                        time.sleep(2)
                        print('Router can Switch back to SIM1 but takes time ( Additional 5 minutes )')

                    elif link1 == 'Disconnected':
                        print('Router cannot switch back to SIM1 even after waiting more than 6 minutes ')

                    else:
                        print('Router tried to connect back to SIM1 but fails ')

            elif link2 == 'Disconnected':
                print('Router cannot connect to SIM2 even after rebooting')

            else:
                print('Router is Connecting to SIM2. Please wait......')
                time.sleep(360)
                print('Please check the configurations')

                interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                time.sleep(2)
                link_manager = driver.find_element_by_xpath(
                    './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                time.sleep(2)
                link_status = driver.find_element_by_xpath(
                    './/*[@id="id_interface_link_manager_status_tab"]').click()
                A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                # me1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                print(A1, 'is', link1)

                A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                print(A2, 'is', link2)

                if link2 == 'Connected':
                    print('Router is connected to SIM2')
                    cellular = driver.find_element_by_xpath(
                        './/*[@id="id_interface_cellular_menu"]/span[1]').click()
                    time.sleep(1)
                    cellular_status = driver.find_element_by_xpath(
                        './/*[@id="id_interface_cellular_status_tab"]').click()
                    time.sleep(2)

                    B1 = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()
                    model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                    print('Modem Model =', model_status)

                    iccid1 = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                    print('ICCID after deactivating SIM1 =', iccid1)

                    imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                    print('IMEI after deactivating SIM1 =', imei)

                    Network_provider = driver.find_element_by_xpath(
                        './/*[@id="id_cellular-status-operator_1"]').text
                    print('Network Provider after deactivating SIM1 =', Network_provider)

                    network_type = driver.find_element_by_xpath(
                        './/*[@id="id_cellular-status-network_type_1"]').text
                    print('Network type after deactivating SIM1 =', network_type)

                    signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                    print('Signal_Strength after deactivating SIM1 =', signal_strength)

                    print('Activating SIM1 back on. Please wait......')

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
                        './html/body/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/input').click()

                    time.sleep(5)
                    driver.find_element_by_id('jw-searchfield-1021-inputEl').send_keys(iccid)
                    driver.find_element_by_xpath(
                        './/*[@id="jw-searchfield-1021-triggerWrap"]/tbody/tr/td[1]').click()
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
                    print(
                        'SIM1 has been activated back from Optus SIM Manager. Lets check if router has switch back to SIM1 ')
                    driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
                    driver.get('http://192.168.0.1/auth/login.html')

                    login()

                    interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                    time.sleep(2)
                    link_manager = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                    time.sleep(2)
                    link_status = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_status_tab"]').click()
                    A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                    link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                    # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                    # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                    print(A1, 'is', link1)

                    A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                    link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                    # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                    # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                    print(A2, 'is', link2)

                    if link1 == 'Connected':
                        print('The router is connected back to the SIM1')
                        print('Please check the configurations')
                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                        time.sleep(1)
                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                        time.sleep(2)

                        driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                        model_status = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-modem_model_1"]').text
                        print('Modem Model =', model_status)

                        iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                        print(' SIM1 ICCID =', iccid)

                        imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                        print('SIM1 IMEI =', imei)

                        Network_provider = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-operator_1"]').text
                        print('SIM1 Network Provider =', Network_provider)

                        network_type = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-network_type_1"]').text
                        print('SIM1 Network type =', network_type)

                        signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                        print('Signal Strength using SIM1  =', signal_strength)
                        time.sleep(2)

                        print('Router can Switch back to SIM1 after SIM2 has been deactivated')

                    elif link1 == 'Disconnected':
                        print('SIM1 is disconnected')
                        time.sleep(5)
                        driver.find_element_by_id('id_reboot').click()
                        reboot_sure = driver.find_element_by_id('id_comfirm_yes')
                        reboot_sure.click()
                        print('Rebooting')
                        time.sleep(300)
                        driver = webdriver.Chrome(
                            "C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
                        driver.get('http://192.168.0.1/auth/login.html')
                        login()

                        interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                        time.sleep(2)
                        link_manager = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                        time.sleep(2)
                        link_status = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_status_tab"]').click()
                        A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                        link1 = driver.find_element_by_xpath(
                            './/*[@id="id_link_manager-link_status-status_1"]').text
                        # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                        # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                        print(A1, 'is', link1)

                        A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                        link2 = driver.find_element_by_xpath(
                            './/*[@id="id_link_manager-link_status-status_2"]').text
                        # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                        # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                        print(A2, 'is', link2)

                        if link1 == 'Connected':
                            print('The router is connected back to the SIM1')
                            print('Please check the configurations')
                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                            time.sleep(1)
                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                            time.sleep(2)

                            driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                            model_status = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-modem_model_1"]').text
                            print('Modem Model =', model_status)

                            iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                            print(' SIM1 ICCID =', iccid)

                            imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                            print('SIM1 IMEI =', imei)

                            Network_provider = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-operator_1"]').text
                            print('SIM1 Network Provider =', Network_provider)

                            network_type = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-network_type_1"]').text
                            print('SIM1 Network type =', network_type)

                            signal_strength = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-csq_1"]').text
                            print('Signal Strength using SIM1  =', signal_strength)
                            time.sleep(2)

                            print('Router can Switch back to SIM1 after a Rebooting ')


                        elif link1 == 'Disconnected':
                            print('Router cannot switch back to SIM1 even after rebooting')


                        else:
                            print('Router is Connecting to SIM1. Please wait......')
                            time.sleep(360)
                            print('Please check the configurations')

                            interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                            time.sleep(2)
                            link_manager = driver.find_element_by_xpath(
                                './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                            time.sleep(2)
                            link_status = driver.find_element_by_xpath(
                                './/*[@id="id_interface_link_manager_status_tab"]').click()
                            A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                            link1 = driver.find_element_by_xpath(
                                './/*[@id="id_link_manager-link_status-status_1"]').text
                            # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                            # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                            print(A1, 'is', link1)

                            A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                            link2 = driver.find_element_by_xpath(
                                './/*[@id="id_link_manager-link_status-status_2"]').text
                            # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                            # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                            print(A2, 'is', link2)

                            if link1 == "Connected":

                                driver.find_element_by_xpath(
                                    './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                                time.sleep(1)
                                driver.find_element_by_xpath(
                                    './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                                time.sleep(2)

                                driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                                model_status = driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-modem_model_1"]').text
                                print('Modem Model =', model_status)

                                iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                                print(' SIM1 ICCID =', iccid)

                                imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                                print('SIM1 IMEI =', imei)

                                Network_provider = driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-operator_1"]').text
                                print('SIM1 Network Provider =', Network_provider)

                                network_type = driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-network_type_1"]').text
                                print('SIM1 Network type =', network_type)

                                signal_strength = driver.find_element_by_xpath(
                                    './/*[@id="id_cellular-status-csq_1"]').text
                                print('Signal Strength using SIM1  =', signal_strength)
                                time.sleep(2)
                                print('Router can Switch back to SIM1 but takes time ( Additional 5 minutes )')

                            elif link1 == 'Disconnected':
                                print('Router cannot switch back to SIM1 even after waiting more than 6 minutes ')

                            else:
                                print('Router tried to connect back to SIM1 but fails ')

                    else:
                        print('Router is Connecting to SIM1. Please wait......')
                        time.sleep(360)
                        print('Please check the configurations')

                        interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                        time.sleep(2)
                        link_manager = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                        time.sleep(2)
                        link_status = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_status_tab"]').click()
                        A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                        link1 = driver.find_element_by_xpath(
                            './/*[@id="id_link_manager-link_status-status_1"]').text
                        # uptime1 = driver.find_element_by_xpath( './/*[@id="id_link_manager-link_status-link_uptime_1"]').text
                        # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                        print(A1, 'is', link1)

                        A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                        link2 = driver.find_element_by_xpath(
                            './/*[@id="id_link_manager-link_status-status_2"]').text
                        # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                        # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                        print(A2, 'is', link2)

                        if link1 == "Connected":

                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                            time.sleep(1)
                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                            time.sleep(2)

                            driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                            model_status = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-modem_model_1"]').text
                            print('Modem Model =', model_status)

                            iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                            print(' SIM1 ICCID =', iccid)

                            imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                            print('SIM1 IMEI =', imei)

                            Network_provider = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-operator_1"]').text
                            print('SIM1 Network Provider =', Network_provider)

                            network_type = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-network_type_1"]').text
                            print('SIM1 Network type =', network_type)

                            signal_strength = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-csq_1"]').text
                            print('Signal Strength using SIM1  =', signal_strength)
                            time.sleep(2)
                            print('Router can Switch back to SIM1 but takes time ( Additional 5 minutes )')

                        elif link1 == 'Disconnected':
                            print('Router cannot switch back to SIM1 even after waiting more than 6 minutes ')

                        else:
                            print('Router tried to connect back to SIM1 but fails ')


        else:
            print('Router is connecting to SIM2')
            time.sleep(360)
            print('Please check the configurations')

            interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
            time.sleep(2)
            link_manager = driver.find_element_by_xpath(
                './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
            time.sleep(2)
            link_status = driver.find_element_by_xpath(
                './/*[@id="id_interface_link_manager_status_tab"]').click()
            A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
            link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
            # me1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
            # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
            print(A1, 'is', link1)

            A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
            link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
            # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
            # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
            print(A2, 'is', link2)

            if link2 == 'Connected':
                print('Router is connected to SIM2')
                cellular = driver.find_element_by_xpath('.//*[@id="id_interface_cellular_menu"]/span[1]').click()
                time.sleep(1)
                cellular_status = driver.find_element_by_xpath(
                    './/*[@id="id_interface_cellular_status_tab"]').click()
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
                    './html/body/form/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr/td/table/tbody/tr[10]/td/input').click()

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
                print(
                    'SIM1 has been activated back from Optus SIM Manager. Lets check if router has switch back to SIM1 ')
                driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
                driver.get('http://192.168.0.1/auth/login.html')

                login()

                interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                time.sleep(2)
                link_manager = driver.find_element_by_xpath(
                    './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                time.sleep(2)
                link_status = driver.find_element_by_xpath(
                    './/*[@id="id_interface_link_manager_status_tab"]').click()
                A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                print(A1, 'is', link1)

                A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                print(A2, 'is', link2)

                if link1 == 'Connected':
                    print('The router is connected back to the SIM1')
                    print('Please check the configurations')
                    driver.find_element_by_xpath(
                        './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                    time.sleep(1)
                    driver.find_element_by_xpath(
                        './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                    time.sleep(2)

                    driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                    model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                    print('Modem Model =', model_status)

                    iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                    print(' SIM1 ICCID =', iccid)

                    imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                    print('SIM1 IMEI =', imei)

                    Network_provider = driver.find_element_by_xpath(
                        './/*[@id="id_cellular-status-operator_1"]').text
                    print('SIM1 Network Provider =', Network_provider)

                    network_type = driver.find_element_by_xpath(
                        './/*[@id="id_cellular-status-network_type_1"]').text
                    print('SIM1 Network type =', network_type)

                    signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                    print('Signal Strength using SIM1  =', signal_strength)
                    time.sleep(2)

                    print('Router can Switch back to SIM1 after SIM2 has been deactivated')

                elif link1 == 'Disconnected':
                    print('SIM1 is disconnected')
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
                    link_manager = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                    time.sleep(2)
                    link_status = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_status_tab"]').click()
                    A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                    link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                    # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                    # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                    print(A1, 'is', link1)

                    A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                    link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                    # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                    # ip2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                    print(A2, 'is', link2)

                    if link1 == 'Connected':
                        print('The router is connected back to the SIM1')
                        print('Please check the configurations')
                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                        time.sleep(1)
                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                        time.sleep(2)

                        driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                        model_status = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-modem_model_1"]').text
                        print('Modem Model =', model_status)

                        iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                        print(' SIM1 ICCID =', iccid)

                        imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                        print('SIM1 IMEI =', imei)

                        Network_provider = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-operator_1"]').text
                        print('SIM1 Network Provider =', Network_provider)

                        network_type = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-network_type_1"]').text
                        print('SIM1 Network type =', network_type)

                        signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                        print('Signal Strength using SIM1  =', signal_strength)
                        time.sleep(2)

                        print('Router can Switch back to SIM1 after a Rebooting ')


                    elif link1 == 'Disconnected':
                        print('Router cannot switch back to SIM1 even after rebooting')


                    else:
                        print('Router is Connecting to SIM1. Please wait......')
                        time.sleep(360)
                        print('Please check the configurations')

                        interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                        time.sleep(2)
                        link_manager = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                        time.sleep(2)
                        link_status = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_status_tab"]').click()
                        A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                        link1 = driver.find_element_by_xpath(
                            './/*[@id="id_link_manager-link_status-status_1"]').text
                        # uptime1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                        # ip1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                        print(A1, 'is', link1)

                        A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                        link2 = driver.find_element_by_xpath(
                            './/*[@id="id_link_manager-link_status-status_2"]').text
                        # uptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                        # p2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                        print(A2, 'is', link2)

                        if link1 == "Connected":

                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                            time.sleep(1)
                            driver.find_element_by_xpath(
                                './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                            time.sleep(2)

                            driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                            model_status = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-modem_model_1"]').text
                            print('Modem Model =', model_status)

                            iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                            print(' SIM1 ICCID =', iccid)

                            imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                            print('SIM1 IMEI =', imei)

                            Network_provider = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-operator_1"]').text
                            print('SIM1 Network Provider =', Network_provider)

                            network_type = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-network_type_1"]').text
                            print('SIM1 Network type =', network_type)

                            signal_strength = driver.find_element_by_xpath(
                                './/*[@id="id_cellular-status-csq_1"]').text
                            print('Signal Strength using SIM1  =', signal_strength)
                            time.sleep(2)
                            print('Router can Switch back to SIM1 but takes time ( Additional 5 minutes )')

                        elif link1 == 'Disconnected':
                            print('Router cannot switch back to SIM1 even after waiting more than 6 minutes ')

                        else:
                            print('Router tried to connect back to SIM1 but fails ')

                else:
                    print('Router is Connecting to SIM1. Please wait......')
                    time.sleep(360)
                    print('Please check the configurations')

                    interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                    time.sleep(2)
                    link_manager = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                    time.sleep(2)
                    link_status = driver.find_element_by_xpath(
                        './/*[@id="id_interface_link_manager_status_tab"]').click()
                    A1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_1"]').text
                    link1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_1"]').text
                    # e1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_1"]').text
                    # p1 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_1"]').text
                    print(A1, 'is', link1)

                    A2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_2"]').text
                    link2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-status_2"]').text
                    # ptime2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-link_uptime_2"]').text
                    # p2 = driver.find_element_by_xpath('.//*[@id="id_link_manager-link_status-ip_2"]').text
                    print(A2, 'is', link2)

                    if link1 == "Connected":

                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_menu"]/span[1]').click()  # cellular
                        time.sleep(1)
                        driver.find_element_by_xpath(
                            './/*[@id="id_interface_cellular_status_tab"]').click()  # cellular status
                        time.sleep(2)

                        driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()  # B1
                        model_status = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-modem_model_1"]').text
                        print('Modem Model =', model_status)

                        iccid = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                        print(' SIM1 ICCID =', iccid)

                        imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                        print('SIM1 IMEI =', imei)

                        Network_provider = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-operator_1"]').text
                        print('SIM1 Network Provider =', Network_provider)

                        network_type = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-network_type_1"]').text
                        print('SIM1 Network type =', network_type)

                        signal_strength = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                        print('Signal Strength using SIM1  =', signal_strength)
                        time.sleep(2)
                        print('Router can Switch back to SIM1 but takes time ( Additional 5 minutes )')

                    elif link1 == 'Disconnected':
                        print('Router cannot switch back to SIM1 even after waiting more than 6 minutes ')

                    else:
                        print('Router tried to connect back to SIM1 but fails ')


            elif link2 == 'Disconnected':
                print('The router cannot connect to SIM2')
            else:
                print('The router cannot connect to SIM2')



    elif link1 == 'Disconnected':
        print('SIM1 is Disconnected. Router  cannot connect to SIM1')

    else:
        print('SIM1 is still connecting. Router cannot connect to SIM1')




