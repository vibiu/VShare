from selenium import webdriver

#Following are optional required
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

baseurl = 'http://mail.163.com/'
username = 'username'
password = 'password'

xpaths = {
    'username_box': '//input[@name="username"]',
    'password_box': '//input[@name="password"]',
    'submitButton' : '//button[@id="loginBtn"]'
}

mydriver = webdriver.Firefox()
mydriver.get(baseurl)
mydriver.maximize_window()

mydriver.find_element_by_xpath(xpaths['username_box']).clear()
mydriver.find_element_by_xpath(xpaths['username_box']).send_keys(username)


mydriver.find_element_by_xpath(xpaths['password_box']).clear()
mydriver.find_element_by_xpath(xpaths['password_box']).send_keys(password)

mydriver.find_element_by_xpath(xpaths['submitButton']).click()
