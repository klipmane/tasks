from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import eshop_func as func
import eshop_data as data

log_file = func.create_log_file()

driver = webdriver.Chrome()
eshop_url = data.eshop_urls["mall"]
category_url = eshop_url + data.product_categories_mall["mobily"]

driver.get(category_url)
func.assert_title(driver, data.mall["category_title"], log_file)

func.filter_expensive(driver)
func.assert_sorting(driver, data.mall["most_expensive"], log_file)

func.pick_up_products(driver, 3)
func.assert_cart(driver, ActionChains, 3, log_file)

driver.close()


