import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_id("autosuggest").send_keys("ind")
time.sleep(2)
countries = driver.find_elements_by_xpath("//div[@class='s-expand-height s-include-content-margin s-border-bottom s-latency-cf-section']/div/span/a/div/img")
print(len(countries))

for country in countries:
    if country.text == "India":
        country.click()
        break

print(driver.find_element_by_id("autosuggest").get_attribute('value'))
Cselected = driver.find_element_by_id("autosuggest").get_attribute('value')

assert Cselected == "India"