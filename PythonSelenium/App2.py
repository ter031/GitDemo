import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element_by_xpath("//input[@type='search']").send_keys("ber")
time.sleep(3)
products = driver.find_elements_by_xpath("//div[@class='products']/div")
print(len(products))
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
print((len(buttons)))
for button in buttons:
    button.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
totalamnt = int(driver.find_element_by_css_selector("span[class='totAmt']").text)
print(totalamnt)
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
print(driver.find_element_by_css_selector("span.promoInfo").text)
totalafterdiscount = int(driver.find_element_by_css_selector("span[class='discountAmt']").text)
print(totalafterdiscount)

assert totalafterdiscount < totalamnt

sum = 0
values = driver.find_elements_by_xpath("//tr/td[5]/p")
for value in values:
    sum = sum + int(value.text)

print(sum)

assert sum == totalamnt

