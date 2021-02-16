import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("http://demo.automationtesting.in/Windows.html")

print(driver.title)   # returns title of the page
print(driver.current_url)  # returns the URL Page

driver.find_element_by_xpath("//*[@id='Tabbed']/a/button").click()

time.sleep(5)

#driver.close() # currently closes focused browser

driver.quit()  # closes all the browsers