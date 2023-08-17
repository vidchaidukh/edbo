from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def grab(offer):
    driver = webdriver.Firefox()
    driver.get(offer[1])
    try:
        element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "request-status-6"))
        )
    except:
        print("Page is down")

    with open('html/'+offer[0]+'.html', 'w', encoding="utf-8") as f:
        f.write(driver.page_source)
    driver.close()