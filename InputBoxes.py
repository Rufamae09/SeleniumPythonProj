# Input boxes, radio button, and check box
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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

# Working with the radio button
status = driver.find_element_by_xpath("//*[@id='q26']/table/tbody/tr[1]/td/label").is_selected()  # Returns true/false
print(status)
time.sleep(2)
driver.find_element_by_xpath("//*[@id='q26']/table/tbody/tr[1]/td/label").click()  # Click Male radio button
time.sleep(2)
status = driver.find_element_by_css_selector("input[id='RESULT_RadioButton-7_0']").is_selected()  # Returns true/false
print(status)

# Working with Check Boxes
driver. find_element_by_xpath("//*[@id='q15']/table/tbody/tr[1]/td/label").click()  # Click Sunday checkbox
status = driver.find_element_by_css_selector("input[id='RESULT_CheckBox-8_0']").is_selected()  # Returns true/false
print(status)
driver.find_element_by_xpath("//*[@id='q15']/table/tbody/tr[2]/td/label").click()   # Click Monday checkbox
status = driver.find_element_by_css_selector("input[id='RESULT_CheckBox-8_1']").is_selected()  # Returns true/false
print(status)

# Working with Drop Down
element = driver.find_element_by_id("RESULT_RadioButton-9")  # Click the dropdown
drp = Select(element)
#drp.select_by_index(2)  # Select Afternoon
#drp.select_by_value("Radio-0")  # Select Morning
drp.select_by_visible_text("Evening")

# Count number of options
print(len(drp.options))

# Capture all the Options
all_options = drp.options

for option in all_options:
    print(option.text)


driver.find_element_by_id("FSsubmit").click()  # Click Submit button

driver.quit()




