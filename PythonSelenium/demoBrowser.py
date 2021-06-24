from selenium import webdriver

driver = webdriver.Chrome()
#driver = webdriver.Firefox()
#driver = webdriver.Edge(executable_path="C:\\Users\\deepa\\AppData\\Local\\Programs\\Python\\Python39\\msedgedriver.exe")
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/")
print(driver.title)
print((driver.current_url))
driver.get("https://rahulshettyacademy.com/blog/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()