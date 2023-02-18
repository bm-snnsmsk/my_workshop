from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service


deriver_service = Service(executable_path="C:/programlarim/chromedriver.exe")
driver = webdriver.Chrome(service=deriver_service)

url = "https://google.com"
driver.get(url)
driver.find_element(By.NAME,"q").send_keys("selenium")
time.sleep(1)


# searchElement = driver.find_element(By.NAME,"q")
# time.sleep(1)
# searchElement.send_keys("python")
# time.sleep(2)
# searchElement.send_keys(Keys.ENTER) ## enter' bas
# time.sleep(2)

# ### alternatif yol
# # result = driver.page_source
# # print(result)

# result = driver.find_elements(By.CSS_SELECTOR,".repo-list-item a")
# for i in result:
#     print(i.text)

# result = driver.page_source
# ##print(driver.page_source)
# soup = BeautifulSoup(result,"html.parser")

# for i in soup.find_all("h3",{"class":"wb-break-all"}):
#     ## print()
#     el = i.find("a")
#     if el.text == "python" :
#         el.send_keys(Keys.ENTER)
#         time.sleep(2)


driver.close()