from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")

driver.get("https://www.selenium.dev/downloads/")

print(driver.title)   # Title of the Page

print(driver.current_url)   # Returns the URL of the page
print(driver.page_source)    # HTML code

driver.close()       # close the browser