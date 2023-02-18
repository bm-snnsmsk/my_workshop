from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "http://github.com"
driver.get(url)

time.sleep(2)

print(driver.title) ## sayfanın title bilgisi
driver.maximize_window() ## sayfayı tam ekran
driver.save_screenshot("aaa.png") ## 
url = "http://github.com/bm-snnsmsk"
driver.get(url)
time.sleep(2)
driver.back() ## geri sayfaya gitme
time.sleep(2)
driver.forward() ## geri sayfaya gitme

time.sleep(12)
driver.close()