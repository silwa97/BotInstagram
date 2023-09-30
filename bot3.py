from selenium import webdriver
import time
class BotInstagram3():
    
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
        
    def entrar_link(self, link):
        self.driver.get(link)   
        
        bot = BotInstagram3()
        bot.entrar_link("https://www.instagram.com/") 