
#%%

import selenium
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



class scraper():


    def __init__(self, url: str='https://www.goodreads.com/'):
        self.driver = Chrome()
        self.driver.get(url)

    def click_search_bar(self, xpath: str = '//div[@class="auto_complete_field_wrapper"]'):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,xpath)))
            self.driver.find_element(By.XPATH, xpath).click()
            #self.driver.find_element(By.XPATH,xpath).send_keys('stephen king')
            

        except TimeoutException:
            print("couldn't find search bar")
            
    def search(self, xpath:str = '//input[@id="sitesearch_field"]'):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,xpath)))
            self.driver.find_element(By.XPATH,xpath).send_keys(input())

        except TimeoutException:
            print("couldn't type the word in")

    def click_search_button(self, xpath:str= '//img[@title="Title / Author / ISBN"]'):
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,xpath)))
            self.driver.find_element(By.XPATH,xpath).click()

        except TimeoutException:
            print("couldn't find the search button")

    def close_login_popup(self, xpath:str= '//button[@class= "gr-iconButton"]'):
        try:
            #self.driver.switch_to.frame('//div[@id="overlay"]')
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,xpath)))
            self.driver.refresh()
        
        except TimeoutException:
            print("no log-in pop up")

    def finding_containers(self, xpath:str= '//table[@class= "tableList"]'):
        return self.driver.find_element(By.XPATH,xpath)
            


            

        
            

if __name__ == '__main__':
    bot = scraper()
    bot.click_search_bar()
    bot.search()
    bot.click_search_button()
    bot.close_login_popup()
    bot.finding_containers()
    




# %%
