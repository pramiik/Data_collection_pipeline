

from mimetypes import init
import unittest

from setuptools import setup

from webscraper import scraper

from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# selenium 4
from selenium import webdriver
#driver = webdriver.Chrome('/home/user/drivers/chromedriver')
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))



#from selenium.common.exceptions import ElementNotInteractableException
#import pandas as pd
#from pandas.testing import assert_frame_equal

import unittest
import os


class scraperTestCase(unittest.TestCase):
    def setUp(self):
        self.bot= scraper('colleen hoover','https://www.goodreads.com/')
        

    def test_bookurl(self):
        expected = "https://www.goodreads.com/search?utf8=%E2%9C%93&query=colleen+hoover"
        self.bot.click_search_bar()
        self.bot.search()
        self.bot.click_search_button()
        self.bot.close_login_popup()
        actual= self.bot.driver.current_url
        self.assertEqual(expected, actual)

    def test_finding_container(self):
        self.bot.click_search_bar()
        self.bot.search()
        self.bot.click_search_button()
        self.assertIsNotNone(self.bot.finding_containers)

    def test_list_books_urls(self):
        expected = list
        self.bot.click_search_bar()
        self.bot.search()
        self.bot.click_search_button()
        self.bot.finding_containers()
        self.bot.list_urls_other()
        self.bot.list_books_urls()
        actual = type(self.bot.list_books_urls())
        self.assertIs(actual,expected)
        #assertIs

    def test_save_json(self):
        self.bot.click_search_bar()
        self.bot.search()
        self.bot.click_search_button()
        #self.bot.close_login_popup()
        self.bot.finding_containers()
        self.bot.list_urls_other()
        self.bot.list_books_urls()
        #self.bot.books_info()
        self.bot.save_injson()
        self.assertTrue(os.path.exists('/home/pramika/Documents/Aicore/data_collection_project/raw_data/data.json'))

    def test_download_images(self):
        self.bot.click_search_bar()
        self.bot.search()
        self.bot.click_search_button()
        self.bot.finding_containers()
        self.bot.list_urls_other()
        self.bot.list_books_urls()
        self.bot.save_injson()
        self.bot.download_images()
        self.assertTrue(os.path.exists('/home/pramika/Documents/Aicore/data_collection_project/raw_data/images'))
        self.assertTrue(os.path.exists('/home/pramika/Documents/Aicore/data_collection_project/raw_data/images/Colleen Hoover0.jpg'))
        self.assertTrue(os.path.exists('/home/pramika/Documents/Aicore/data_collection_project/raw_data/images/Colleen Hoover1.jpg'))
        self.assertTrue(os.path.exists('/home/pramika/Documents/Aicore/data_collection_project/raw_data/images/Colleen Hoover2.jpg'))
        self.assertTrue(os.path.exists('/home/pramika/Documents/Aicore/data_collection_project/raw_data/images/Colleen Hoover3.jpg'))
        self.assertTrue(os.path.exists('/home/pramika/Documents/Aicore/data_collection_project/raw_data/images/Colleen Hoover4.jpg'))


unittest.main(argv=[''], verbosity=5, exit=False)




















        

