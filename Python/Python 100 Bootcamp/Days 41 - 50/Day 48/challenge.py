from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

firefox_options = webdriver.FirefoxOptions()
firefox_options.set_preference("detach", True)

driver = webdriver.Firefox(options=firefox_options)
driver.get("https://secure-retreat-92358.herokuapp.com/")
# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# visits = driver.find_element(By.XPATH, value="/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[1]/div[1]/div/div[3]/a[1]")
# visits.click()

# portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# portals.click()
# search_toggle = driver.find_element(By.XPATH, value="/html/body/div[1]/header/div[2]/div/a/span[1]")
# search_toggle.click()
# search = driver.find_element(By.XPATH, value="/html/body/div[1]/header/div[2]/div/div/div/form/div/div/div[1]/input")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)

field = driver.find_element(By.XPATH,value="/html/body/form/input[1]")
field.send_keys("Blah1")

field = driver.find_element(By.XPATH,value="/html/body/form/input[2]")
field.send_keys("Blah2")

field = driver.find_element(By.XPATH,value="/html/body/form/input[3]")
field.send_keys("BLAH@BLAH.com")

button = driver.find_element(By.XPATH, value="/html/body/form/button")
button.click()

# driver.close()