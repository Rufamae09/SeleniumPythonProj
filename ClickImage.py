import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.guru99.com/selenium-tutorial.html")

driver.find_element_by_class_name("g-logo").click()

driver.close()
