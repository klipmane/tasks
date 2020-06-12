import time
product_categories = {
    "mobily": "mobilni-telefony",
    "tablety": "tablety",
    "e-book ctecky": "e-book",
    "notebooky": "notebooky",
    "pocitace": "pocitace"
    }

def pick_up_products(driver, amount):
    in_cart = 0
    element = 1
    while in_cart != amount:
        try:
            product = driver.find_element_by_xpath(f'//main[@id="content"]//article[{element}]//button')
            driver.execute_script("arguments[0].click();", product)
            element += 1
            in_cart += 1
            time.sleep(2)
        except:
            element += 1
    return driver

def filter_expensive(driver):
    expensive_list = driver.find_element_by_xpath('//a[contains(text(), "Nejvyšší ceny")]')
    driver.execute_script("arguments[0].click();", expensive_list)
    return driver

def filter_cheapest(driver):
    cheap_list = driver.find_element_by_xpath('//a[contains(text(), "Nejnižší ceny")]')
    driver.execute_script("arguments[0].click();", cheap_list)
    return driver

