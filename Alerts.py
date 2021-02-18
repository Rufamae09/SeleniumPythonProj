import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("https://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath("//*[@id='HTML9']/div[1]/button").click()
time.sleep(5)

#driver.switch_to.alert.accept()   # closes alert window using OK button
driver.switch_to.alert.dismiss()  # closes alert window using Cancel button


driver.quit()