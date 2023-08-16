from selenium import webdriver

def grab(offer):
    browser = webdriver.Firefox()
    browser.get(offer[1])
    with open('html/'+offer[0]+'.html', 'w', encoding="utf-8") as f:
        f.write(browser.page_source)
    browser.close()