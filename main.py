import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.common.keys import Keys


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.service = Service(executable_path=r'C:\Program Files (x86)\SeleniumWrapper\chromedriver.exe')
        self.driver = webdriver.Chrome(service=self.service)

    def Login(self):
        self.driver.get('https://www.instagram.com/')
        time.sleep(2)

        user_element = self.driver.find_element(By.XPATH, "//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)

        password_element = self.driver.find_element(By.XPATH, "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        password_element.send_keys(Keys.RETURN)
        self.Curtir('memesBR')


    def Curtir(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/'+ hashtag +'/')
        time.sleep(5)
        for i in range(1,3):
            driver.execute_script("window.scrollTo(0, document.body.scrolHeight);")


    time.sleep(120000000)
anderson = InstagramBot(username='worldmart480@gmail.com', password='125074728565aA@')
anderson.Login()

