

from mimetypes import init
import unittest

from setuptools import setup

from webscraper import scraper

from selenium import webdriver
from selenium.common.exceptions import ElementNotInteractableException
import unittest
import os
#import pandas as pd
#from pandas.testing import assert_frame_equal



class scraperTestCase(unittest.TestCase):
    def setup(self):
        self.bot= scraper('colleen hoover','https://www.goodreads.com/')
        

    def test_bookurl(self):
        expected = 'https://www.goodreads.com/search?q=colleen+hoover'
        self.bot.click_search_bar()
        self.bot.search()
        self.bot.click_search_button()
        actual = self.bot.driver.current_url()
        self.assertEqual(expected, actual)

    def test_finding_container(self):
        self.bot.click_search_bar()
        self.bot.search()
        self.bot.click_search_button()
        self.assertIsNotNone(self.bot.finding_containers)

    def test_list_books_urls(self):
        expected = list
        actual = type(self.bot.list_books_urls())
        self.assertListEqual(expected, actual)

    def test_save_json(self):
        self.bot.save_injson()
        self.assertTrue(os.path.exists('books.json'))

    def test_download_images(self):
        self.bot.download_images()
        self.assertTrue(os.path.exists('images'))
        self.assertTrue(os.path.exists('images/colleen hoover1.jpg'))
        self.assertTrue(os.path.exists('images/colleen hoover2.jpg'))
        self.assertTrue(os.path.exists('images/colleen hoover3.jpg'))
        self.assertTrue(os.path.exists('images/colleen hoover4.jpg'))
        self.assertTrue(os.path.exists('images/colleen hoover5.jpg'))


unittest.main(argv=[''], verbosity=5, exit=False)




















        

