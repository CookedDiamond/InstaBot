from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot:

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox()

    def closeBrowser(self):
        self.driver.close()

    def login(self):

        driver = self.driver
        print("login page")
        driver.get("https://www.instagram.com/accounts/login/?source=auth_switcher")
        time.sleep(2)
        print("enter name: "+self.username+" and password: "+self.password)
        u = driver.find_element_by_xpath("//input[@name='username']")
        u.clear()
        u.send_keys(self.username)

        r = driver.find_element_by_xpath("//input[@name='password']")
        r.clear()
        r.send_keys(self.password)

        r.send_keys(Keys.RETURN)

        time.sleep(4)

        print("nicht jetzt")

        b = driver.find_element_by_xpath("//button[@class='aOOlW   HoLwm ']")
        b.click()
        

        
    def likeAndFollow(self,hashtag):
        print("start to like and follow")
        driver = self.driver
        driver.get("https://www.instagram.com/explore/tags/"+hashtag+"/")
        time.sleep(2)

        pic_hrefs = []
        end = 20;
        for i in range(1, end+1):
            try:
                print("scrolling"+str(i)+"/"+str(end))
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(0.7)
                # get tags
                hrefs_in_view = driver.find_elements_by_tag_name('a')
                # finding relevant hrefs
                hrefs_in_view = [elem.get_attribute('href') for elem in hrefs_in_view
                                 if '.com/p/' in elem.get_attribute('href')]
                # building list of unique photos
                [pic_hrefs.append(href) for href in hrefs_in_view if href not in pic_hrefs]
                print("Check: pic href length " + str(len(pic_hrefs)))
            except Exception:
                continue

        counter = 0   
            # Liking photos
        for pic_href in pic_hrefs:
            counter=counter+1
            driver.get(pic_href)
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                time.sleep(2+random.randint(1,9))
                driver.find_element_by_xpath("//button[@class='dCJp8 afkep']").click()
                
                
                print(" LIKED a photo")
                print("     progress: "+str(counter)+"/"+str(len(pic_hrefs)))
                print("     url:"+pic_href)
                print("     hashtag: "+hashtag)

                if(random.randint(1,4)==4):
                    driver.find_element_by_xpath("//button[@class='oW_lN sqdOP yWX7d        ']").click()
                    print(" FOLLOWED")
                    time.sleep(1)
                time.sleep(2++random.randint(12,18))
                print()    
            except Exception as e:
                print(e)
                

        

IG = InstagramBot("InstaMinecraftMeme.exe@gmx.de","Instagram12345")
IG.login()
IG.likeAndFollow('memes')
IG.likeAndFollow('meme')
IG.likeAndFollow('funny')