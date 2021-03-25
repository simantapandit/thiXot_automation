from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import os


driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
driver.get('http://192.168.0.1/auth/login.html')
#driver.get('http://10.6.20.50/auth/login.html')
#driver.minimize_window()
time.sleep(10)
def login():
    user = 'admin'
    pas = ('thinxtra',"S8ThaCGBPjcqq2L42NYhlQ==" , 'admin')

    try:
        for i in pas:
            driver.find_element_by_id('id_username_val').send_keys(user)
            driver.find_element_by_id('id_password_val').send_keys(i)
            driver.find_element_by_id('id_login').click()
    except:
        print()


login()

time.sleep(5)
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

#SIM check starts from here


interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
time.sleep(2)
link_manager = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_menu"]/span[1]').click()
time.sleep(5)
link_status = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_status_tab"]').click()
time.sleep(20)
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

max_times = 6

for i in range(max_times):
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

        iccid1 = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
        print('Active SIM ICCID =', iccid1)
        iccid = iccid1.replace('F','')

        imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
        print('Active SIM IMEI =', imei)

        Network_provider = driver.find_element_by_xpath('.//*[@id="id_cellular-status-operator_1"]').text
        print('Active Network Provider =', Network_provider)

        network_type = driver.find_element_by_xpath('.//*[@id="id_cellular-status-network_type_1"]').text
        print('Active Network type =', network_type)
        if network_type == 'LTE':
            print('Active Link has Excellent Connectivity')
        else:
            print('Active Link has Poor Connectivity')

        signal_strength_first = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
        print('Signal Strength  =', signal_strength_first)
        split1 = signal_strength_first.split('(',1)
        signal_strength_1 = split1[0]

        if signal_strength_1 == '28' or '29' or '30' or '31':
            print('Active Link has excellent signal strength')
        if signal_strength_1 == '23' or '24' or '25' or '26' or '27':
            print('Active Link has Average signal strength')
        else:
            print('Active Link has Average signal strength')
        driver.quit()
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
        print('SIM1 has been deactivated')
        sim_status=driver.find_element_by_xpath('.//*[@id="displayfield-1045-inputEl"]').text



        print('Waiting on SIM2 to be active. Please wait....... ')
        time.sleep(240)
        print('Connecting back to the Router interface')
        login_times = 10

        for i in range(login_times):
            if sim_status == 'Deactivated':
                driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
                driver.get('http://192.168.0.1/auth/login.html')
                time.sleep(10)
                login()
                time.sleep(5)
                if
                break
            else:
                print('Trying to reconnect to the router interface. ')
                time.sleep(40)


        #driver.get('http://10.6.20.50/auth/login.html')

        status = driver.find_element_by_xpath('.//*[@id="id_nav_status_group"]')
        status.click()

        interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
        time.sleep(2)
        link_manager = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_menu"]/span[1]').click()
        time.sleep(2)
        link_status = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_status_tab"]').click()
        time.sleep(20)
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
        max_tries = 6
        for i in range(max_tries):
            if link2 == 'Connected':
                print('Router is connected to SIM2')
                cellular = driver.find_element_by_xpath('.//*[@id="id_interface_cellular_menu"]/span[1]').click()
                time.sleep(1)
                cellular_status = driver.find_element_by_xpath('.//*[@id="id_interface_cellular_status_tab"]').click()
                time.sleep(2)

                B1 = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_status_1"]').click()
                model_status = driver.find_element_by_xpath('.//*[@id="id_cellular-status-modem_model_1"]').text
                print('Modem Model =', model_status)

                iccid_sim2 = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                print('SIM2 ICCID  =', iccid_sim2)


                imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                print('SIM2 IMEI =', imei)

                Network_provider = driver.find_element_by_xpath('.//*[@id="id_cellular-status-operator_1"]').text
                print('SIM2 Network Provider =', Network_provider)

                network_type = driver.find_element_by_xpath('.//*[@id="id_cellular-status-network_type_1"]').text
                print('SIM2 Network type =', network_type)

                signal_strength_second = driver.find_element_by_xpath('.//*[@id="id_cellular-status-csq_1"]').text
                print('SIM2 Signal_Strength=', signal_strength_second)

                split2 = signal_strength_second.split('(', 1)
                signal_strength_2 = split2[0]

                if signal_strength_2 == '28' or '29' or '30' or '31':
                    print('SIM2 has excellent signal strength')
                if signal_strength_2 == '23' or '24' or '25' or '26' or '27':
                    print('SIM2 has Average signal strength')
                else:
                    print('SIM2 has Average signal strength')

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
                sim_status_back = driver.find_element_by_xpath('.//*[@id="displayfield-1045-inputEl"]').text
                time.sleep(5)

                driver.find_element_by_link_text('Ok').click()
                time.sleep(10)
                driver.quit()
                time.sleep(360)

                print(
                    'SIM1 has been activated back from Optus SIM Manager. Lets check if router has switch back to SIM1 ')

                driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
                driver.get('http://192.168.0.1/auth/login.html')
                time.sleep(10)
                login()
                time.sleep(5)
                device = driver.find_element_by_xpath('.//*[@id="id_system-device_model_tip"]').text

                login_back_times = 10
                for i in range(login_back_times):
                    if device == 'Device Model':
                        break

                    else:
                        print('Trying to reconnect to the router interface. ')
                        time.sleep(40)


                status = driver.find_element_by_xpath('.//*[@id="id_nav_status_group"]')
                status.click()
                interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                time.sleep(2)
                link_manager = driver.find_element_by_xpath(
                    './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                time.sleep(2)
                link_status = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_status_tab"]').click()
                time.sleep(20)
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

                counter = 6
                for i in range(counter):
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

                        iccid1 = driver.find_element_by_xpath('.//*[@id="id_cellular-status-iccid_1"]').text
                        print(' SIM1 ICCID =', iccid1)
                        iccid = iccid1.replace('F','')
                        imei = driver.find_element_by_xpath('.//*[@id="id_cellular-status-imei_1"]').text
                        print('SIM1 IMEI =', imei)

                        Network_provider = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-operator_1"]').text
                        print('SIM1 Network Provider =', Network_provider)

                        network_type = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-network_type_1"]').text
                        print('SIM1 Network type =', network_type)

                        time.sleep(2)
                        signal_strength_third = driver.find_element_by_xpath(
                            './/*[@id="id_cellular-status-csq_1"]').text
                        print('SIM2 Signal_Strength=', signal_strength_third)

                        split3 = signal_strength_third.split('(', 1)
                        signal_strength_3 = split3[0]

                        if signal_strength_3 == '28' or '29' or '30' or '31':
                            print('SIM2 has excellent signal strength')
                        if signal_strength_3 == '23' or '24' or '25' or '26' or '27':
                            print('SIM2 has Average signal strength')
                        else:
                            print('SIM2 has Average signal strength')
                        print('Router can Switch back to SIM1 after SIM2 has been deactivated')
                        break

                    else:
                        print('SIM1 hasnot been connected')
                        print('Waiting on SIM1 to be active. Please wait 2 minutes')
                        time.sleep(120)
                        #interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                        time.sleep(2)
                        link_manager = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                        time.sleep(2)
                        link_status = driver.find_element_by_xpath(
                            './/*[@id="id_interface_link_manager_status_tab"]').click()
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
                break
            else:
                print('SIM1 hasnot been connected')
                print('Waiting on SIM1 to be active. Please wait 2 minutes')
                time.sleep(120)
                #interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
                time.sleep(2)
                link_manager = driver.find_element_by_xpath(
                    './/*[@id="id_interface_link_manager_menu"]/span[1]').click()
                time.sleep(2)
                link_status = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_status_tab"]').click()
                time.sleep(20)
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
        break
    else:
        print('SIM1 hasnot been connected')
        print('Waiting on SIM1 to be active. Please wait 2 minutes')
        time.sleep(120)
        #interface = driver.find_element_by_xpath('.//*[@id="id_nav_interface_group"]').click()
        time.sleep(3)
        link_manager = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_menu"]/span[1]').click()
        time.sleep(2)
        link_status = driver.find_element_by_xpath('.//*[@id="id_interface_link_manager_status_tab"]').click()
        time.sleep(20)
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



