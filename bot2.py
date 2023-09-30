import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class InstagramBot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path=r"chromedriver.exe")
        
      

    def Login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/')
        time.sleep(2)
        
        jhonatanBot = InstagramBot('IssoVaiMudarOMundo',"aindaBemQueEuSeiCriarUm")
        jhonatanBot.loguin()

      