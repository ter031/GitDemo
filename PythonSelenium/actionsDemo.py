from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(5)
#driver.get("https://rahulshettyacademy.com/AutomationPractice/")

#menu = driver.find_element_by_id("mousehover")

#action.move_to_element(menu).perform()
#childmenu = driver.find_element_by_link_text("Top")
#action.move_to_element(childmenu).perform()
#action.click(childmenu).perform()
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
action = ActionChains(driver)
action.context_click(driver.find_element_by_id("double-click")).perform()
#action.double_click(driver.find_element_by_id("double-click")).perform()

#alert = driver.switch_to.alert
#assert "You double clicked me!!!, You got to be kidding me" == alert.text
#alert.accept()