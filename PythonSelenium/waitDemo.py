#Implicit wait
#Explicit wait
import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element_by_xpath("//input[@type='search']").send_keys("ber")
time.sleep(4)
products = driver.find_elements_by_xpath("//div[@class='products']/div")
print(len(products))
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
print((len(buttons)))
for button in buttons:
    button.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
print(driver.find_element_by_css_selector("span.promoInfo").text)
