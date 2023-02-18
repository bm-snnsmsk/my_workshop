from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.chrome.service import Service
from userInfo import username, password



class Instagram :
    def __init__(self,username,password) :
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option("prefs",{'intl.accept_languages':'en,en_US'})
        self.browser_service = Service(executable_path="C:/programlarim/chromedriver.exe")
        self.browser = webdriver.Chrome(service=self.browser_service,chrome_options=self.browserProfile) 
        self.username = username 
        self.password = password

    def signIn(self) :
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(2)
        usernameInput = self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[1]/div/label/input")
        passwordInput = self.browser.find_element(By.XPATH,"//*[@id='loginForm']/div/div[2]/div/label/input")

        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(2)

    def getFollowers(self, max):
        self.browser.get(f"https://www.instagram.com/{self.username}/follower")
        time.sleep(2)
        self.browser.find_element(By.XPATH,"//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a").click() ## takipçiler linkini tıkla
        time.sleep(2)

        dialog = self.browser.find_element(By.CSS_SELECTOR,"div[role=dialog] ul")
        followersCount = len(dialog.find_elements(By.CSS_SELECTOR,"li"))
        print(f"first count : {followersCount}")

        action = webdriver.ActionChains(self.browser)
        while followersCount < 50 :
            dialog.click()
            action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
            time.sleep(2)

            newCount = len(dialog.find_elements(By.CSS_SELECTOR,"li"))
            if followersCount != newCount :
                followersCount = newCount
                print(f"second count :{newCount}")
                time.sleep(1)
            else :
                break

        followers = dialog.find_elements(By.CSS_SELECTOR,"li")
        followerList = []
        i = 0
        for i in followers :
            link = i.find_element(By.CSS_SELECTOR,"a").get_attribute("href")
            followerList.append(link)
            i+=1
            if i == max :
                break
        
        with open("followers.txt", "w", encoding="utf-8") as f :
            for i in followerList :
                f.write(i+"\n")

    def followUser(self, username) :
        self.browser.get("https://www.instagram.com/"+username)
        time.sleep(2)
        followButton =self.browser.find_element(By.TAG_NAME,"button")
        ## print(followButton.text)
        if followButton != "Following" :
            followButton.click()
            time.sleep(2)
        else :
            print("Zaten takiptesin")

    def unFollowUser(self, username) :
        self.browser.get("https://www.instagram.com/"+username)
        time.sleep(2)
        followButton =self.browser.find_element(By.TAG_NAME,"button")
        ## print(followButton.text)
        if followButton == "Following" :
            followButton.click()
            time.sleep(2)
            self.browser.find_element(By.XPATH,"//button[text()='Unfollow'").click()
            time.sleep(2)
        else :
            print("Zaten takip etmiyorsun")







instagram = Instagram(username,password)
instagram.signIn()
## instagram.getFollowers(50)  ## bu fonksiyon sistemsel hata veriyor

list = ["kod_evreni","python.hub","zynpsmsk_"]
## takip etmek iin
# for i in list :
#     instagram.followUser(i)
#     time.sleep(2)
## takip etmemek için
for i in list :
    instagram.unFollowUser(i)
    time.sleep(2)
