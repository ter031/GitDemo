import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")
driver.find_element_by_xpath("//input[@type='search']").send_keys("ber")
time.sleep(4)
list1 = []
list2 = []
products = driver.find_elements_by_xpath("//div[@class='products']/div")
print(len(products))
texts = driver.find_elements_by_xpath("//div[@class='product']/h4")
for vegname in texts:
    list1.append(vegname.text)
print(list1)

buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
print((len(buttons)))
for button in buttons:
    button.click()

driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

texts1 = driver.find_elements_by_css_selector("p.product-name")
print(len(texts1))
for a in texts1:
    print(a.text)
    list2.append(a.text)
#print(list2)
del list2[3:6]
print(list2)

assert list1 == list2