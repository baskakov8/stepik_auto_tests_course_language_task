import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

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