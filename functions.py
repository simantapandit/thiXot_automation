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

    return link1, link2