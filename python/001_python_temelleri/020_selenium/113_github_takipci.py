from githubUserInfo import username, password
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.chrome.service import Service





class Github :
    def __init__(self, username, password = "") :
        self.deriver_service = Service(executable_path="C:/programlarim/chromedriver.exe")
        self.browser = webdriver.Chrome(service=self.deriver_service)
        self.username = username
        self.password = password
        self.followers = []

    def signIn(self) :
        self.browser.get("https://github.com/login")
        time.sleep(2)
        self.browser.find_element(By.XPATH,"//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element(By.XPATH,"//*[@id='password']").send_keys(self.password)
        time.sleep(1)
        self.browser.find_element(By.XPATH,"//*[@id='login']/form/div[3]/input[8]").click() ## giriş butonunu tıkla
    
    def loadFollowers(self) :
        items = self.browser.find_elements(By.CLASS_NAME,"d-table")
        for i in items :
            self.followers.append(i.find_element(By.CLASS_NAME,"d-inline-block").text)

    def getFollowers(self) :
        self.browser.get(f"https://github.com/{self.username}?tab=followers")
        time.sleep(2)
        self.loadFollowers()
        
        # while True :
        #     links = self.browser.find_element(By.CLASS_NAME,"pagination").find_elements(By.TAG_NAME,"a")
        #     if len(links) == 1 :
        #         if links[0].text == "Next" :
        #             links[0].click()
        #             time.sleep(1)
        #             self.loadFollowers()
        #         else :
        #             break
        #     else :
        #         for link in links :
        #             if link.text == "Next" :
        #                 link.click()
        #                 time.sleep(1)
        #                 self.loadFollowers()
        #             else : 
        #                 continue

        


github = Github("sadikturan")
## github.signIn()
github.getFollowers()
print(len(github.followers))
print(github.getFollowers())