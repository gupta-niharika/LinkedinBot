from selenium import webdriver
import os
import time

class Linkedinbot:

    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.driver = webdriver.Chrome('chromedriver.exe')

        self.login()

        #self.schedule_meeting()

    def login(self):
        self.driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys(self.username)
        self.driver.find_element_by_xpath('//*[@id="password"]').send_keys(self.password)
        self.driver.find_element_by_xpath('//*[@id="app__container"]/main/div[2]/form/div[3]/button').click()
        #by default u get logged into the homepage

        #create a post
        self.driver.find_element_by_xpath('//*[@id="ember47"]/div/div[1]/button').click()
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div/div/div[1]').send_keys('this is post 9 by kitanu')   #/div/div[1]
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div[2]/div[2]/button/span').click()
        self.driver.find_elements_by_xpath('//*[@id="mynetwork-tab-icon"]/li-icon').click()


if __name__ == '__main__':
    loginbot = Linkedinbot('email@gmail.com','pwd')
