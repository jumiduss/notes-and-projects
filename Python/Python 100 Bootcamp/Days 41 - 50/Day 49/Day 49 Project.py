from selenium import webdriver
from selenium.webdriver.common.by import By
import time


firefox_options = webdriver.FirefoxOptions()
firefox_options.set_preference("detach", True)


driver = webdriver.Firefox(options=firefox_options)

link = "https://www.linkedin.com/jobs/search/?currentJobId=3826637057&f_AL=true&keywords=python%20developer&origin=JOB_SEARCH_PAGE_JOB_FILTER&refresh=true"

driver.get(link)

signin = driver.find_element(By.XPATH, value="/html/body/div[1]/header/nav/div/a[2]")
signin.click()

user_field = driver.find_element(By.XPATH, value='//*[@id="username"]')
user_field.send_keys('jumiduss@gmail.com')

# Stopped here because of google 2 step verification codes