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

row1 = driver.find_elements_by_xpath('.//*[@id="id_sdk-app_list_val_1"]')


row2 = driver.find_elements_by_xpath('.//*[@id="id_sdk-app_list_tip"]')

count = len(driver.find_elements_by_xpath("./html/body/div/div[4]/div/div[1]/div[3]/div[2]"))
for i in row2:
    index = driver.find_elements_by_xpath('.//*[@id="id_sdk-app_list-id"]').text
#index1 = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-id_1"]').text
#print(index1)
    print(index)


#**********
robustlink = driver.find_elements_by_xpath('.//*[@id="id_sdk-app_list_val_2"]')
rlink_name =driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-name_2"]').text
rlink_version = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-version_2"]').text
rlink_status = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-status_2"]').text
rlink_description = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-description_2"]').text
print(rlink_name, rlink_version, rlink_status, rlink_description)
#************
robustvpn = driver.find_elements_by_xpath('.//*[@id="id_sdk-app_list_val_1"]')
rvpn_name =driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-name_1"]').text
rvpn_version = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-version_1"]').text
rvpn_status = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-status_1"]').text
rvpn_description = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-description_1"]').text
print(rvpn_name, rvpn_version, rvpn_status, rvpn_description)
#************
rcms = driver.find_elements_by_xpath('.//*[@id="id_sdk-app_list_val_3"]')

rcms_name = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-name_3"]').text
rcms_version = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-version_3"]').text
rcms_status = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-status_3"]').text
rcms_description = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-description_3"]').text
print(rcms_name, rcms_version, rcms_status, rcms_description)
#********
snmp = driver.find_elements_by_xpath('.//*[@id="id_sdk-app_list_val_4"]')

snmp_name = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-name_4"]').text
snmp_version = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-version_4"]').text
snmp_status = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-status_4"]').text
snmp_description = driver.find_element_by_xpath('.//*[@id="id_sdk-app_list-description_4"]').text
print(snmp_name, snmp_version, snmp_status, snmp_description)



if index == '1':
    if rvpn_name != ["robustlink", "snmp", "rcms"]:
        print("RobustVPN exist")
        if rvpn_version == "3.0.0":
            print("no upgrades is required for robustVPN")
        else:
            driver.find_element_by_xpath('/html/body/div/div[4]/div/div[1]/div[2]/form/div/ul/li[2]/span[1]/input').send_keys('C:\\Users\\siman\\PycharmProjects\\pythonProject1\\applications\\RobustelVPN\\r3000-robustvpn-3.0.0.rpk')
            driver.find_element_by_id('id_input_file').click()
            time.sleep(10)
            driver.find_element_by_xpath('.//*[@id="id_comfirm_no"]').click()

    if rvpn_name != ['robustlink', 'robustvpn', 'rcms']:
        print("snmp exist")
        if rvpn_version == "3.0.2":
            print("no upgrades is required for snmp")
        else:
            driver.find_element_by_xpath('/html/body/div/div[4]/div/div[1]/div[2]/form/div/ul/li[2]/span[1]/input').send_keys('C:\\Users\\siman\\PycharmProjects\\pythonProject1\\applications\\snmp\\r3000-snmp-3.0.2.rpk')
            driver.find_element_by_id('id_input_file').click()
            time.sleep(10)
            driver.find_element_by_xpath('.//*[@id="id_comfirm_no"]').click()
            print('snmp updatee')

    if rvpn_name != ['robustlink', 'snmp', 'robustvpn']:
        print("rcms exist")
        if rvpn_version == "3.0.5":
            print("no upgrade required for rcms")

        else:
            driver.find_element_by_xpath('/html/body/div/div[4]/div/div[1]/div[2]/form/div/ul/li[2]/span[1]/input').send_keys('C:\\Users\\siman\\PycharmProjects\\pythonProject1\\applications\\rcms\\r3000-rcms-3.0.5-20201112064743.rpk')
            driver.find_element_by_id('id_input_file').click()
            time.sleep(10)
            driver.find_element_by_xpath('.//*[@id="id_comfirm_no"]').click()
            print('robustvpn updated')

    if rvpn_name != ['snmp', 'robustvpn', 'rcms']:
        print("robustlink exist")
        if rvpn_version == "3.0.1":
            print("no upgrade required for robustlink")

        else:
            driver.find_element_by_xpath('/html/body/div/div[4]/div/div[1]/div[2]/form/div/ul/li[2]/span[1]/input').send_keys('C:\\Users\\siman\\PycharmProjects\\pythonProject1\\applications\\Robustlink\\r3000-robustlink-3.0.1.rpk')
            driver.find_element_by_id('id_input_file').click()
            time.sleep(10)
            driver.find_element_by_xpath('.//*[@id="id_comfirm_no"]').click()
            print('Snmp updated')

    else:
        print('done')










if index == 'Index':

    # robust VPN update
    driver.find_element_by_xpath('/html/body/div/div[4]/div/div[1]/div[2]/form/div/ul/li[2]/span[1]/input').send_keys('C:\\Users\\siman\\PycharmProjects\\pythonProject1\\applications\\RobustelVPN\\r3000-robustvpn-3.0.0.rpk')
    driver.find_element_by_id('id_input_file').click()
    time.sleep(10)
    driver.find_element_by_xpath('.//*[@id="id_comfirm_no"]').click()

     #   #rcms update
    driver.find_element_by_xpath('/html/body/div/div[4]/div/div[1]/div[2]/form/div/ul/li[2]/span[1]/input').send_keys('C:\\Users\\siman\\PycharmProjects\\pythonProject1\\applications\\rcms\\r3000-rcms-3.0.5-20201112064743.rpk')
    driver.find_element_by_id('id_input_file').click()
    time.sleep(10)
    driver.find_element_by_xpath('.//*[@id="id_comfirm_no"]').click()
    #
     #   #snmp update
    driver.find_element_by_xpath('/html/body/div/div[4]/div/div[1]/div[2]/form/div/ul/li[2]/span[1]/input').send_keys('C:\\Users\\siman\\PycharmProjects\\pythonProject1\\applications\\snmp\\r3000-snmp-3.0.2.rpk')
    driver.find_element_by_id('id_input_file').click()
    time.sleep(10)
    driver.find_element_by_xpath('.//*[@id="id_comfirm_no"]').click()

        #robustlink update
    driver.find_element_by_xpath('/html/body/div/div[4]/div/div[1]/div[2]/form/div/ul/li[2]/span[1]/input').send_keys('C:\\Users\\siman\\PycharmProjects\\pythonProject1\\applications\\Robustlink\\r3000-robustlink-3.0.1.rpk')
    driver.find_element_by_id('id_input_file').click()
    time.sleep(10)
    driver.find_element_by_xpath('.//*[@id="id_comfirm_no"]').click()

else:
    print("No Update required")



