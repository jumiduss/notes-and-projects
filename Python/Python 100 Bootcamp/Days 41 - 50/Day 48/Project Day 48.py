from selenium import webdriver
from selenium.webdriver.common.by import By
import time


firefox_options = webdriver.FirefoxOptions()
firefox_options.set_preference("detach", True)


driver = webdriver.Firefox(options=firefox_options)

driver.get("https://orteil.dashnet.org/cookieclicker/")

time.sleep(2)
language = driver.find_element(By.XPATH, value='//*[@id="langSelect-EN"]')
language.click()
time.sleep(2)

cookie = driver.find_element(By.ID, value="bigCookie")

count=0
running=True

def click_buy():
    try:
        upgrade_set_mouse = driver.find_element(By.CSS_SELECTOR, value="#upgrades")
        mup = upgrade_set_mouse.find_elements(By.CSS_SELECTOR, value=".enabled")        
        mouse = mup[-1]
        mouse.click()
        click_buy()
    except Exception:
        pass 
    try:
        upgrade_set_products = driver.find_element(By.CSS_SELECTOR, value="#products")
        pup = upgrade_set_products.find_elements(By.CSS_SELECTOR, value=".enabled")
        product = pup[-1]
        product.click()
        click_buy()
    except Exception:
        pass
    
timeout = time.time() + 5
five_min = time.time() + 60*5
    
while running:
    if time.time() > five_min:
        break
    cookie.click()
    if time.time() >= timeout:
        click_buy()
        timeout += 5
    
cookies_per_second = driver.find_element(By.XPATH, value='//*[@id="cookies"]')

print(cookies_per_second.text)