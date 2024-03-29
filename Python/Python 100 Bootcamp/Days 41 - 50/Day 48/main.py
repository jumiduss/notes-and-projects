from selenium import webdriver
from selenium.webdriver.common.by import By

firefox_options = webdriver.FirefoxOptions()
firefox_options.set_preference("detach", True)


driver = webdriver.Firefox(options=firefox_options)

# driver.get("https://www.amazon.com/Oppenheimer-Ultra-Blu-ray-Digital-UHD/dp/B0CL7JD41F/")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_dollar.text}.{price_cents.text}")

driver.get("https://www.python.org/")

# search_bar = driver.find_element(By.NAME, value='q')
# print(search_bar.get_attribute("placeholder"))

# button = driver.find_element(By.ID, value="submit")
# print(button.size)

# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, value='/html/body/div/footer/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

## Challenge Code

events = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li")

event_dict = {
    i:{
        "date":(event.text)[:10],
        "title":(event.text)[12:]        
    } for i,event in enumerate(events) 
}
    
print(event_dict)

driver.close()

