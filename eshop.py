from selenium import webdriver
import eshop_def as df
driver = webdriver.Chrome()
eshop_url = "https://www.mall.cz/"
category_url = eshop_url + df.product_categories["mobily"]
driver.get(category_url)

df.filter_expensive(driver)

# for some reason the first selected product is not the most expensive one
# even if I select 5 products, 4 of them will be from expensive list, but the first one not
# unfortuantelly I was not able to handle this issue
df.pick_up_products(driver, 2)

