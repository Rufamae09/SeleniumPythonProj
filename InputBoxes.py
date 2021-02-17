
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="C:\Drivers\chromedriver_win32\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()

# How to find how many inputboxes present in web page
input_boxes=driver.find_elements(By.CLASS_NAME, 'text_field')
print(len(input_boxes))   #6

# How to know the status of the text box
status = driver.find_element_by_id("RESULT_TextField-1").is_displayed()
print("Displayed or not:", status)   # true/false

status = driver.find_element_by_id("RESULT_TextField-1").is_enabled()
print("Enabled or not:", status)   # true/false


# How to provide value into text box
driver.find_element_by_id("RESULT_TextField-1").send_keys("George")  # Input first name
driver.find_element_by_id("RESULT_TextField-2").send_keys("Washington")  # Input last name
driver.find_element_by_id("RESULT_TextField-3").send_keys("7709231111")  # Input Phone
driver.find_element_by_id("RESULT_TextField-4").send_keys("United States")  # Input Country
driver.find_element_by_id("RESULT_TextField-5").send_keys("Atlanta")  # Input State
driver.find_element_by_id("RESULT_TextField-6").send_keys("georgew@test.com")  # Input Email
driver.find_element_by_xpath("//*[@id='q26']/table/tbody/tr[1]/td/label").click()  # Click Male radio button
driver. find_element_by_xpath("//*[@id='q15']/table/tbody/tr[1]/td/label").click()  # Click Sunday checkbox
driver.find_element_by_xpath("//*[@id='q15']/table/tbody/tr[2]/td/label").click()   # Click Monday checkbox
driver.find_element_by_xpath("//*[@id='RESULT_RadioButton-9']").click()  # Click drop down arrow
driver.find_element_by_xpath("//*[@id='RESULT_RadioButton-9']/option[2]").click()  # Select Morning in the drop down options

driver.find_element_by_id("FSsubmit").click()  # Click Submit button

driver.quit()




