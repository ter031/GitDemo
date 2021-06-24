import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://www.amazon.in/")
driver.maximize_window()
driver.find_element_by_id("twotabsearchtextbox").send_keys("face masks")
driver.find_element_by_id("nav-search-submit-button").click()
AllFaceMasks = driver.find_elements_by_xpath("//div[@class='s-expand-height s-include-content-margin s-border-bottom s-latency-cf-section']/div/span/a/div/img")
print(len(AllFaceMasks))

for facemask in AllFaceMasks:
    facemask.click()

driver.quit()



