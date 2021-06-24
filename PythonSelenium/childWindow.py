from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element_by_css_selector("a[href='/windows/new']").click()
childwindow = driver.window_handles[1]
parentwindow = driver.window_handles[0]
driver.switch_to.window(childwindow)
print(driver.find_element_by_tag_name("h3").text)
driver.switch_to.window(parentwindow)
print(driver.title)
driver.quit()