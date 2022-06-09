
#%%

from ast import Break
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

    """ 
    This class is used to scrape good reads website

    Attributes:
    url (str): url of the webite. Here we have used goodreads


    """


    def __init__(self,book: str, url:str):
        self.book = book 
        self.driver = Chrome()
        self.driver.get(url)




    def click_search_bar(self, xpath: str = '//div[@class="auto_complete_field_wrapper"]'):
        """
        This function clicks the search bar on the webpage.

        Args:
            xpath (str): xpath of the search bar
        """
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,xpath)))
            self.driver.find_element(By.XPATH, xpath).click()
            #self.driver.find_element(By.XPATH,xpath).send_keys('stephen king')
            

        except TimeoutException:
            print("couldn't find search bar")
            


    def search(self, xpath:str = '//input[@id="sitesearch_field"]'):
        """
        This function asks the user input on what to seach eg. book, author.

        Args:
            xpath (str): xpath of the search input
        """
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,xpath)))
            self.driver.find_element(By.XPATH,xpath).send_keys(self.book)

        except TimeoutException:
            print("couldn't type the word in")




    def click_search_button(self, xpath:str= '//*[@id="headerSearchForm"]/a/img'): #'//img[@title="Title / Author / ISBN"]'
        """
        This function clicks the search button to start the searching.

        Args:
            xpath (str): xpath of the search button
        """
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,xpath)))
            self.driver.find_element(By.XPATH,xpath).click()

        except TimeoutException:
            print("couldn't find the search button")




    def close_login_popup(self, xpath:str= '//button[@class= "gr-iconButton"]'):
        """
        This function refreshes the page to close the login pop-up.

        Args:
            xpath (str): xpath of the refresh button
        """
        try:
            #self.driver.switch_to.frame('//div[@id="overlay"]')
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,xpath)))
            self.driver.refresh()
        
        except TimeoutException:
            print("no log-in pop up")


    def click_more_author(self, xpath:str= '/html/body/div[2]/div[3]/div[1]/div[2]/div[2]/table/tbody/tr[12]/td[2]/span[2]/div/a/span'): #//*[@id="description"]/a

        """
        This function clicks the click more button. This can be used to get the author details.

        Args:
            xpath (str): xpath of the click more button
        """

        self.driver.find_element(By.XPATH,xpath).click()



    '''
    def find_author_details(self, author = False, xpath: str ='a[@class = "authorName"]'):
        """
        This function is used to the information about the author/author of the book we are searching.

        Args:
            author(bool): Here it is False
            xpath (str) : xpath of the author name

        Returns:
            Dictionary: info_dict- with the information of the author.
        """
        
        try:
            WebDriverWait(self.driver,10).until(EC.presence_of_element_located((By.XPATH,xpath)))

            #author_cont = 
            
            self.driver.find_element(By.XPATH,xpath).click()
            #author_cont.self.diver.find_element()

            author == True

            
        except TimeoutException:
            print(" author - time out")
            author == False

        if author == True:
            self.click_more_author()
            author_details = self.driver.find_element(By.XPATH, '//*[@id="freeTextauthor5430144"]')
            info_dict['author details'].append(author_details.text)
        else:
            print('author details not found')

        return info_dict
    '''


    def finding_containers(self, xpath:str= '//table[@class= "tableList"]'):
        """
        This function finds the container which contains the links to all the book present in that page.

        Args:
            xpath (str): xpath of the container

        Returns:
            Container: which has the links
        """
        global container
        container = self.driver.find_element(By.XPATH,xpath)
        return container



    




    def list_books_urls(self,x=True, xpath:str= '//tr'):
        """
        This function uses the container obtained in the previous function to get all the book links needed.

        Args:
            xpath (str): xpath of the links
        """
        global list_urls     
        global list_books
        global l

        global info_dict
        info_dict = {
            'author details' :[],
            'urls' :[],
            'unique ID' :[],
            'book title' :[],
            'author name' :[],
            'rating' :[],
            'book description' :[],
            'book_cover_links' :[],
            'v4 UUID' :[]
            }

        #list_books=[]
        

        #ls = range(10)
        #while n>10:
        list_books = container.find_elements(By.XPATH, xpath)

            #print(f'list of books is : {list_books}')
            #list_books.append(lis_bk)

        n = len(list_books)
        print(f'the number of books url found are {n}')
       # x=x+1
        
        for books in list_books:
            list_urls.append(books.find_element(By.TAG_NAME, 'a').get_attribute('href'))

        l=len(list_urls)

        print(f'total number of books url found are {l}')

        return list_urls

        
        
            #if n==20:
             #   self.next_page()
              #  x==True
               # list_books = None
            #else:
                #x==False
             #   print('out of the while loop')

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
        

    def list_urls_other(self):

        global list_urls
        period=0

        list_urls =[]
        while period<7:
            
            self.finding_containers()
            self.list_books_urls()
            self.next_page()
            if l>125:
                #Break
                print('out of the while loop')
            else:
                
                print('contiues with while loop')
            period+=1

        
        

    def next_page(self,xpath:str='//div/a[@class="next_page"]'):

        try:
            self.driver.find_element(By.XPATH,xpath).click()
        except:
            print('no next page available')


    
    def books_info(self):
        """
        This function uses the book links found in the previous 
        function to get information about the book such as urls,
        book name, author name, ratings, book descriptions and 
        book cover links. Here we are also creating a UUID for
        each book and also finding the unique id for each link.

        """


        #global info_dict




        for urls in list_urls[0:l]:

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

            try:
                self.click_more_book()
                book_description = self.driver.find_element(By.XPATH, '//*[@id="descriptionContainer"]')
                info_dict['book description'].append(book_description.text)
            except:
                print('no book description available!')
            


            try:
                image = self.driver.find_element(By.XPATH, '//*[@id="imagecol"]/div[1]/div[1]/a')
                imag_dic = image.find_element(By.TAG_NAME, 'img').get_attribute('src')
            except:
                print('no book cover found for this book')
                imag_dic = 'no book cover'
            info_dict['book_cover_links'].append(imag_dic)

            
            #self.driver.get(urls)
            #print(f'image is {image}')
            #print( f'imag dic {imag_dic}')
            #print(image)
            #img= image.get_attribute('src')



            uu_id = uuid.uuid4()
            uuid_str = str(uu_id)
            info_dict['v4 UUID'].append(uuid_str)

            #return info_dict

        #print(info_dict)




    def click_more_book(self, xpath:str= '//*[@id="description"]/a'): #
        """
        This function clicks the click more button. This can be used to get the full book description.
        Args:
            xpath (str): xpath of the click more button
        """

        self.driver.find_element(By.XPATH,xpath).click()

    def save_injson(self):

        """
        This function used to create a json file in a new folder 
        and add the informations found in the previous function.
        n
        """

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
        """
        This function downloads the book cover using the links found in the 
        book_info function. The book covers are stored in a folder named images.

        """
        folder = r'/home/pramika/Documents/Aicore/data_collection_project/raw_data/images'
        if not os.path.exists(folder):
            os.makedirs(folder)

        book_links = info_dict["book_cover_links"]
        #print(book_links)

        for i,lst in enumerate(book_links):
            try:
                self.driver.get(lst)
                urllib.request.urlretrieve(lst,f'/home/pramika/Documents/Aicore/data_collection_project/raw_data/images/{bot.book}{i}.jpg')
            except:
                print('no book cover available')

    





            

if __name__ == '__main__':
    bot = scraper('Colleen Hoover','https://www.goodreads.com/')
    bot.click_search_bar()
    bot.search()
    bot.click_search_button()
    bot.close_login_popup()
    #bot.click_more_author()
    #bot.find_author_details()
    #bot.finding_containers()
    #bot.list_books_urls()
    bot.list_urls_other()
    bot.next_page()
    bot.books_info()
    #bot.click_more_book()
    bot.save_injson()
    bot.download_images()





# %%

'div[@class = "authorName_container"]'
'''

git branch -m main master
git fetch origin
git branch -u origin/master master
git remote set-head origin -a

'''