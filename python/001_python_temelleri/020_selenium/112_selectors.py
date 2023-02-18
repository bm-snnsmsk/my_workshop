from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)

searchElement = driver.find_element_by_css_selector(".form-control js-site-search-focus header-search-input jump-to-field js-jump-to-field")
time.sleep(1)
searchElement.send_keys("python")
time.sleep(2)
searchElement.send_keys(Keys.ENTER) ## enter' bas
time.sleep(2)

### alternatif yol
# result = driver.page_source
# print(result)

result = driver.find_element_by_css_selector(".repo-list-item h3 a")
for i in result:
    print(i.text)

driver.close()