from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_css_selector("input[name='name']").send_keys("deepak")
driver.find_element_by_name("email").send_keys("abc")
driver.find_element_by_id("exampleCheck1").click()
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
driver.find_element_by_name("inlineRadioOptions").click()
driver.find_element_by_xpath("//input[@type='submit']").click()
message = driver.find_element_by_css_selector("div[class='alert alert-success alert-dismissible']").text

assert "Success! The" in message