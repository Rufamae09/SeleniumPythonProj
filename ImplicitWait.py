from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.facebook.com/")  #opening URL takes some time

driver.implicitly_wait(10)    # wait for 10 seconds

assert "Facebook" in driver.title

driver.find_element_by_name("email").send_keys("rufamae.dono")
driver.find_element_by_id("pass").send_keys("ittakesamanandawoman?")

driver.find_element_by_name("login").click()

driver.close()

