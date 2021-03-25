from selenium import webdriver
import time
import subprocess
import platform

router_ipadd = '192.168.0.1'
driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
driver.get('http://192.168.0.1/auth/login.html')
#driver.minimize_window()

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


#router_ipadd = 'http://192.168.0.1/auth/login.html'
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
        time = 6
        current_ip_address = [router_ipadd]
        for i in range(time):
            for each in current_ip_address:
                if ping_ip(each):
                    print(f"{each} is available")

                else:
                    print(f"{each} is not available")
                    time.sleep(5)


def save():
   print('Saving changes')
   driver.find_element_by_xpath('.//*[@id="id_save"]').click()


def reboot():
   reboot = driver.find_element_by_id('id_reboot').click()

   reboot_sure = driver.find_element_by_id('id_comfirm_yes')
   reboot_sure.click()
   print('Rebooting')
   time.sleep(180)

login()

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

print('Please wait while the configuration file is updating......')
save()

time.sleep(60)
reboot()
ping_router()