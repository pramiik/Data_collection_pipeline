
#%%

from http.cookies import BaseCookie
from typing import Container
import selenium
from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import re
import uuid
from uuid import UUID

import os
import json

import urllib.request








class scraper():


    def __init__(self,book, url: str='https://www.goodreads.com/'):
        self.book = book 
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
        global container
        container = self.driver.find_element(By.XPATH,xpath)
        return container

    def list_books_urls(self, xpath:str= '//tr'):
        global list_urls

        list_books = container.find_elements(By.XPATH, xpath)
        print(f'the number of books url found are {len(list_books)}')

        list_urls = []
            
        for books in list_books:
            list_urls.append(books.find_element(By.TAG_NAME, 'a').get_attribute('href'))

        #print(list_urls)

        '''
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,xpath)))
            list_books = self.containers.find_elements(By.XPATH, '//tr')
            len(list_books)

            
            
            for books in list_books:
                list_urls.append(books.find_element(By.TAG_NAME, 'a').get_attribute('href'))

        except TimeoutException:
            print('cannot find the list urls')

        '''
    
    
    def books_info(self):

        global info_dict


        info_dict = {
                'urls' :[],
                'unique ID' :[],
                'book title' :[],
                'author name' :[],
                'rating' :[],
                'book description' :[],
                'book_cover_links' :[],
                'v4 UUID' :[]
                }



        for urls in list_urls[0:20]:

            self.driver.get(urls)
            info_dict['urls'].append(urls)


            ur = re.findall('\d+', urls)
            info_dict['unique ID'].append(ur[0])
            

            book_title = self.driver.find_element(By.XPATH, '//*[@id="bookTitle"]')
            info_dict['book title'].append(book_title.text)

            author_name = self.driver.find_element(By.XPATH, '//*[@id="bookAuthors"]')
            info_dict['author name'].append(author_name.text)

            rating = self.driver.find_element(By.XPATH, '//*[@id="bookMeta"]/span[2]')
            info_dict['rating'].append(rating.text)

            book_description = self.driver.find_element(By.XPATH, '//*[@id="descriptionContainer"]')
            info_dict['book description'].append(book_description.text)



            #self.driver.get(urls)
            image = self.driver.find_element(By.XPATH, '//*[@id="imagecol"]/div[1]/div[1]/a')
            #print(f'image is {image}')
            imag_dic = image.find_element(By.TAG_NAME, 'img').get_attribute('src')
            #print( f'imag dic {imag_dic}')
            #print(image)
            #img= image.get_attribute('src')
            info_dict['book_cover_links'].append(imag_dic)



            uu_id = uuid.uuid4()
            uuid_str = str(uu_id)
            info_dict['v4 UUID'].append(uuid_str)

        #print(info_dict)

    def save_injson(self):

        folder = r'raw_data'
        if not os.path.exists(folder):
            os.makedirs(folder)

        with open("/home/pramika/Documents/Aicore/data_collection_project/raw_data/data.json", "w+") as f:
            json.dump(info_dict, f)

    '''
    def saving_images(self):

        folder = r'/home/pramika/Documents/Aicore/data_collection_project/raw_data/images'
        if not os.path.exists(folder):
            os.makedirs(folder)

    '''

    def download_images(self):
        folder = r'/home/pramika/Documents/Aicore/data_collection_project/raw_data/images'
        if not os.path.exists(folder):
            os.makedirs(folder)

        book_links = info_dict["book_cover_links"]
        #print(book_links)

        for i,lst in enumerate(book_links):
            self.driver.get(lst)
            urllib.request.urlretrieve(lst,f'/home/pramika/Documents/Aicore/data_collection_project/raw_data/images/{bot.book}{i}.jpg')


            

if __name__ == '__main__':
    bot = scraper('stephen_king')
    bot.click_search_bar()
    bot.search()
    bot.click_search_button()
    bot.close_login_popup()
    bot.finding_containers()
    bot.list_books_urls()
    bot.books_info()
    bot.save_injson()




# %%
