import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://newtours.demoaut.com/")   #FR
print(driver.title)

driver.get("http://pavantestingtools.blogspot.in/")    #TT
print(driver.title)
time.sleep(5)

driver.back()
print(driver.title)   #FR
time.sleep(5)

driver.forward()
print(driver.title)   #TT
time.sleep(5)

driver.close()