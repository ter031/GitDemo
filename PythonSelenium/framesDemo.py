from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/frames")
driver.find_element_by_link_text("iFrame").click()
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_id("tinymce").clear()
driver.find_element_by_id("tinymce").send_keys("you are a fool")
driver.switch_to.default_content()

assert driver.find_element_by_tag_name("h3").text == "An iFrame containing the TinyMCE WYSIWYG Editor"