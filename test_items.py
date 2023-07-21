import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'

def test_checking_languages(browser):
    '''Testing website by finding button "Add to the basket"'''
    browser.get(link)
    try:
        browser.find_element(By.CLASS_NAME, "btn-add-to-basket")
        button_flag = True
    except NoSuchElementException:
        button_flag = False
    assert button_flag, "There isn't button 'Add to the basket' on the website"

if __name__ == '__main__':
    pytest.main()