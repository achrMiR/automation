from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import pytest 

@pytest.fixture(scope="class")
def setup(request):
    s=Service('C:\Program Files\chromedriver_win32\chromedriver.exe')
    driver = webdriver.Chrome(service=s)
    request.cls.driver = driver
    url='http://192.168.5.50/'
    driver.get(url)
    driver.maximize_window()

    yield driver
    driver.close()

@pytest.mark.usefixtures("setup")
class TestExample:

    @pytest.mark.smoke
    def test_title(self):
        print("Verify title...")
        assert "Selenium Easy" in self.driver.title

    @pytest.mark.smoke
    def test_content_text(self):
        print("Verify content on the page...")
        centertext = self.driver.find_element_by_css_selector('.tab-content .text-center').text
        assert "WELCOME TO SELENIUM EASY DEMO" == centertext

    @pytest.mark.regression
    @pytest.mark.smoke
    def test_practicing(self):
        print("verifying exercise--")
        startpractisingBtn = self.driver.find_element_by_id('btn_basic_example')
        startpractisingBtn.click()
        time.sleep(10)
        WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#basic .head')))



















delay = 3  # seconds

time.sleep(delay)
username = driver.find_element(By.CSS_SELECTOR, '#login-page > div > div.content > div.row.no-gutters > div.col.form > div > section.user-login > form > input')
password = driver.find_element(By.CSS_SELECTOR, '#login-page > div > div.content > div.row.no-gutters > div.col.form > div > section.user-login > form > div.password.mt-5 > input')

username.send_keys("service")
password.send_keys("mir4service")

driver.find_element(By.CSS_SELECTOR, '#login-page > div > div.content > div.row.no-gutters > div.col.form > div > section.user-login > form > div.row.mt-5.align-items-center > div.col-auto.text-right > button').click()

time.sleep(delay)

# setup
driver.find_element(By.CSS_SELECTOR, '#app > div > main > aside > nav.menu-left > section > a:nth-child(2)').click()

time.sleep(delay)
driver.find_element(By.CSS_SELECTOR, '#app > div > main > aside > nav:nth-child(2) > section > a:nth-child(8)').click()

"""
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

    i += 1 """


# driver.close()
