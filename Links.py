from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://www.microsoft.com/en-hk/")
driver.maximize_window()

links = driver.find_elements(By.TAG_NAME, "a")
print("Number of links present:", len(links))  # print how many links in page

for link in links:
    print(link.text)   # Print all the links in text

#clicking on the link
driver.find_element_by_link_text("Microsoft 365").click()


