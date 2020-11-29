from selenium import webdriver

driver = webdriver.Firefox()
driver.get("https://github.com/login")

username = "write your username here"
password = "write your pass here"

username_path = '//*[@id="login_field"]'
password_path = '//*[@id="password"]'
loginbutton_path = '/html/body/div[3]/main/div/form/div[4]/input[12]'

username_element = driver.find_element_by_xpath(username_path)
pass_element = driver.find_element_by_xpath(password_path)
button_element = driver.find_element_by_xpath(loginbutton_path)

username_element.send_keys(username)
pass_element.send_keys(password)
button_element.submit()
