from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("--ignore-certificate-errors")

driver = webdriver.Chrome(options=chrome_options)
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_css_selector("a[href='/angularpractice/shop']").click()

products = driver.find_elements_by_xpath("//div[@class='card h-100']")
for product in products:
    productName = product.find_element_by_xpath("div/h4/a").text
    if productName == "Blackberry":
        product.find_element_by_xpath("div/button").click()

driver.find_element_by_css_selector("a[class='nav-link btn btn-primary']").click()
driver.find_element_by_css_selector("button[class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("ind")
driver.find_element_by_xpath("/html/body/app-root/app-shop/div/app-checkout/div/div[2]/ul/li/a").click()
print(driver.find_element_by_id("country").get_attribute("value"))
driver.find_element_by_css_selector("label[for='checkbox2']").click()
driver.find_element_by_css_selector("input[class='btn btn-success btn-lg']").click()
successText = driver.find_element_by_css_selector("div[class='alert alert-success alert-dismissible']").text

assert "Success! Thank you!" in successText

driver.get_screenshot_as_file("success.png")