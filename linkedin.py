from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

firefox_profile = webdriver.FirefoxProfile()
#firefox_profile.set_preference('permissions.default.image', 2)
#firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')

browser = webdriver.Firefox(firefox_profile=firefox_profile)
session_url = browser.command_executor._url      
session_id = browser.session_id 

class linkedin:
    def __init__(self, topics):
        """
        topics - list of hashtags to look for
        """
        self.link_prefix = "https://www.linkedin.com/feed/hashtag/?keywords=%23"
        self.topics = topics
        login_address = 'https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin'
        
        browser.get(self.link_prefix + 'ai')
        try:
            #browser.find_element_by_id("email-address").send_keys("franklinselva10@gmail.com")
            browser.find_element_by_xpath('//*[@id="email-address"]').send_keys('franklinselva10@gmail.com')
        except:
            print("Moving to signing in section")
            browser.find_element_by_xpath('/html/body/div/div/div/div/div[2]/div[1]/div[1]/div[2]/p/a').click()
        else:
            browser.find_element_by_id("email-address").send_keys("franklinselva10@gmail.com")
            browser.find_element_by_id ("password").send_keys("lonelyangel1219")
            browser.find_element_by_class_name("login__form_action_container").click()
    

    def parse(self):
        for topic in self.topics:
            page = requests.get('')
            soup = BeautifulSoup(page.content, 'lxml')
            dropDown = soup.find_all(class_  = 'sort-dropdown__list')
            print (dropDown)
            break