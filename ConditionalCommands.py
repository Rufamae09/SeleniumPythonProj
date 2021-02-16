import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.facebook.com/")
user_ele=driver.find_element_by_name("email")

print(user_ele.is_displayed())   # returns true/false based on element status
print(user_ele.is_enabled())    #returns true/false

pwd_ele=driver.find_element_by_id("pass")
print(pwd_ele.is_displayed())   # returns true/false based on element status
print(pwd_ele.is_enabled())    #returns true/false

user_ele.send_keys("test")
time.sleep(5)
user_ele.clear()
pwd_ele.send_keys("test?")
time.sleep(5)
pwd_ele.clear()

driver.find_element_by_name("login").click()

driver.quit()



#roundtrip_radio=driver.find_element_by_css_selector("input[value=roundtrip]")
#print("status of round trip radio button", roundtrip_radio.is_selected())    # print the status of the radio button

#oneway_radio=driver.find_element_by_css_selector("input[value=oneway]")
#print("status of round trip radio button" , oneway_radio.is_selected())     # print the status of the radio button