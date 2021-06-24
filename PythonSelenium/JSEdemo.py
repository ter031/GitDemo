#JS DOM cna access all webpage elements on a webpage just like selenium does
#selenium have a method to execute javascript code in it
from selenium import webdriver


driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("hello")
#print(driver.find_element_by_name("name").text)
print(driver.find_element_by_name("name").get_attribute("value"))
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

shopButton = driver.find_element_by_css_selector("a[href='/angularpractice/shop']")
driver.execute_script("arguments[0].click();",shopButton)

driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")