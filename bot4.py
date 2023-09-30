from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://www.instagram.com/')

time.sleep(4)

email_field = driver.find_element(By.XPATH, "//input[@name='username']")
email_field.send_keys('topemagrecimento630@gmail.com')
time.sleep(4)
password_element = driver.find_element (By.XPATH, "//input[@name='password']")
password_element.send_keys('senha123')
password_element.send_keys(Keys.RETURN)
time.sleep(5)



driver.get('https://www.instagram.com/frutasrondonoficial/')
time.sleep(10)

link = driver.find_element(By.XPATH, '//a[@href="/frutasrondonoficial/followers/"]')
time.sleep(15)
link.click()
time.sleep(15)

element = driver.find_element(By.XPATH, '/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/div[1]/div/div[1]/div/div/div/div[3]/div/button')
time.sleep(10)
element.click()




time.sleep(200)

driver.implicitly_wait(10)
webdriver.quit()