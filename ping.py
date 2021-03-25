from selenium import webdriver
import time
import subprocess
import platform

#driver = webdriver.Chrome("C:\\Users\\siman\\PycharmProjects\\pythonProject1\\chromedriver.exe")
router_ipadd = '192.168.0.1'

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
        times = 100

        for i in range(times):
            #for each in current_ip_address:
                if ping_ip(router_ipadd):
                    print(f"{router_ipadd} is connected")
                    break

                else:
                    print(f"{router_ipadd} is not reachable")


        else:
            #times == 6:
            print(f'Router cannot connect to the {router_ipadd}')
            print('Router looses the connection after  6 tries')
            quit()

ping_router()

