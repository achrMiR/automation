from selenium import webdriver
import time

delay = 3  # seconds
url = 'http://192.168.5.50/'


driver = webdriver.Chrome(executable_path="C:\Program Files\chromedriver_win32\chromedriver.exe")

driver.get(url)

username = driver.find_element_by_id("login_username")
password = driver.find_element_by_id("login_password")

username.send_keys("service")
password.send_keys("mir4service")

driver.find_element_by_name("submit").click()

# setup
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[1]/ul/li[2]/div').click()

# scheduler
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[7]/div[1]/div[2]/div[2]/ul[1]/li[1]/a').click()

# top bar arrow right
time.sleep(2)
driver.find_element_by_xpath('//*[@id="topsubbar_fleet_schedule_scroll_right"]').click()
driver.find_element_by_xpath('//*[@id="topsubbar_fleet_schedule_scroll_right"]').click()

i = 0
j = 0
iterations = 100
start_day = '4'

while i < iterations:
    # print(i)
    start_date = '2021-09-0' + start_day

    # anders menu
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="topsubbar_fleet_schedule_list"]/li[14]').click()

    # mission
    driver.find_element_by_xpath('//*[@id="topsubbar_fleet_schedule_list"]/li[14]/ul/li[1]').click()

    # run asap
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="run_asap_toggle"]').click()

    # time.sleep(2)
    elem = driver.find_element_by_xpath('//*[@id="earliest_start_time_date"]')
    elem.clear()
    elem.send_keys(start_date)

    # time.sleep(2)
    driver.find_element_by_name("submit").click()

    if i == iterations-1:
        print(start_day)
        start_day = int(start_day)
        start_day += 1
        start_day = str(start_day)
        print("days done")
        i = -1
        j += 1

    if j == 7:
        break

    i += 1


driver.close()
