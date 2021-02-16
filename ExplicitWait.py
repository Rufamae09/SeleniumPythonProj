import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.expedia.com/")

driver.find_element_by_xpath("//*[@id='uitk-tabs-button-container']/li[2]/a").click()  # click Flights button

driver.find_element_by_css_selector('button[aria-label = "Leaving from"]').send_keys("New York (JFK - John F. Kennedy Intl.")  # click Leaving from and enter current place
time.sleep(2)
driver.find_element_by_xpath("//*[@id='location-field-leg1-origin-menu']/div[2]/ul/li[1]/button/div/div[1]").click()  # click the the place in the dropdown options
driver.find_element_by_css_selector('button[aria-label = "Going to"]').send_keys("Universal Studios Florida")  # click Going to and enter destination
time.sleep(2)
driver.find_element_by_xpath("//*[@id='location-field-leg1-destination-menu']/div[2]/ul/li[1]/button/div/div[1]").click()  # click destination on the dropdown options
driver.find_element_by_css_selector('button[class="uitk-faux-input uitk-form-field-trigger"]').click()  # click Departing button
time.sleep(2)
driver.find_element_by_css_selector('button[aria-label = "Mar 10, 2021."]').click()   # Select exact departure date
driver.find_element_by_css_selector('button[data-stid = "apply-date-picker"]').click()  # click Done button
driver.find_element_by_css_selector('button[id = "d2-btn"]').click()  # click Returning button
time.sleep(4)
driver.find_element_by_css_selector('button[data-day = "11"]').click()   # Select exact returning date
driver.find_element_by_css_selector('button[data-stid = "apply-date-picker"]').click()  # click Done button
driver.find_element_by_css_selector('button[type = "submit"]').click()  # click Search button

# ExplicitWait
wait = WebDriverWait(driver, 30)
element = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "[data-test-id='stops-0-label']")))
element.click()
time.sleep(3)

driver.quit()

