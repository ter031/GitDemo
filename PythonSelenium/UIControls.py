from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))

for checkbox in checkboxes:
    print(checkbox.get_attribute('value'))
    if checkbox.get_attribute('value') == 'option2':
        checkbox.click()
        assert checkbox.is_selected()

radiobuttons = driver.find_elements_by_name("radioButton")
print(radiobuttons)
radiobuttons[2].click()
assert radiobuttons[2].is_selected()