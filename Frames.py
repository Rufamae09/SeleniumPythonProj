import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.maximize_window()
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html")

driver.switch_to.frame("packageListFrame")   # frist frame
driver.find_element_by_link_text("org.openqa.selenium").click()
time.sleep(3)
driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")  # second frame
driver.find_element_by_link_text("WebDriver").click()
time.sleep(3)

driver.switch_to.default_content()
time.sleep(3)
driver.switch_to.frame("classFrame")  # third frame
driver.find_element_by_xpath("/html/body/header/nav/div[1]/div[1]/ul/li[6]/a").click()

driver.quit()
