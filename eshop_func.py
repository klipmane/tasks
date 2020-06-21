import time
import datetime
import os

def pick_up_products(driver, amount):
    in_cart = 0
    element = 1
    while in_cart != amount:
        try:
            product = driver.find_element_by_xpath(f'//main[@id="content"]/section//article[{element}]//button')
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
    time.sleep(2)
    return driver


def filter_cheapest(driver):
    cheap_list = driver.find_element_by_xpath('//a[contains(text(), "Nejnižší ceny")]')
    driver.execute_script("arguments[0].click();", cheap_list)
    time.sleep(2)
    return driver


def create_log_file():
    time = datetime.datetime.now()
    time = time.strftime("%Y_%m_%d__%H_%M")
    script_name = os.path.splitext(__file__)[-2]
    log_name = script_name + "_" + time + ".log"
    file = open(log_name, "w")
    file.close()
    return log_name


def add_log(log_file, text):
    with open(log_file, mode="a", newline="", encoding="utf-8") as log:
        print(text, file=log)
        return log_file


def assert_title(driver, correct_title, log_file):
    try:
        assert driver.title==correct_title, f"Error! Page Title is not equal: {correct_title}"
        add_log(log_file, f"{correct_title} is succesfully opened")
        driver.get_screenshot_as_file(f"correct_{correct_title[0:15]}.png")
    except AssertionError as err:
        add_log(log_file, str(err))
        driver.get_screenshot_as_file(f"error_{correct_title[0:15]}.png")
        driver.close()
    except Exception as error:
        add_log(log_file, str(error))
        driver.get_screenshot_as_file(f"error_{correct_title[0:15]}.png")
        driver.close()

def assert_sorting(driver, sorting, log_file):
    try:
        assert driver.find_element_by_xpath(f'//a[contains(@class, "sort-item-link sort-item-link--active dark")][contains(text(), "{sorting}")]'), f"Sorting by {sorting} is not active"
        add_log(log_file, f"Sorting by {sorting} is succesful")
        # driver.get_screenshot_as_file(f"correct_{sorting[0:15]}.png")
    except AssertionError as err:
        add_log(log_file, str(err))
        # driver.get_screenshot_as_file(f"error_{sorting[0:15]}.png")
        driver.close()
    except Exception as error:
        add_log(log_file, str(error))
        # driver.get_screenshot_as_file(f"error_{sorting[0:15]}.png")
        driver.close()


def assert_cart(driver, ActionChains, amount, log_file):
    try:
        assert driver.find_element_by_xpath(f'//span[@class="con-notification con-bold" and @data-is-notification-active="true"][contains(text(), "{amount}")]'), f"{amount} elements not fount in the card"
        add_log(log_file, f"{amount} products were added to the cart")
        cart = driver.find_element_by_xpath('//a[@href="/kosik"]')
        hover = ActionChains(driver).move_to_element(cart)
        hover.perform()
        driver.get_screenshot_as_file(f"correct_cart.png")
    except AssertionError as err:
        add_log(log_file, str(err))
        driver.get_screenshot_as_file(f"error_cart.png")
        driver.close()
    except Exception as error:
        add_log(log_file, str(error))
        driver.get_screenshot_as_file(f"error_cart.png")
        driver.close()