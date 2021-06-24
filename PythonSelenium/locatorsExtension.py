from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://login.salesforce.com/")
driver.find_element_by_css_selector("#username").send_keys("deepak")
driver.find_element_by_css_selector("#password").send_keys("thakur")
driver.find_element_by_css_selector("#password").clear()
driver.find_element_by_link_text("Forgot Your Password?").click()
driver.find_element_by_xpath("//a[text()='Cancel']").click()
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
print(driver.find_element_by_xpath("//label[@for='password']").text)