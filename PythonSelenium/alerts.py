from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element_by_id("name").send_keys("Option3")
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
assert  "Option3" in alert.text
alert.accept()
