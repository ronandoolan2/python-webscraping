from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException

#driver = webdriver.Firefox()
baseurl = "http://erosi.saccounty.net"

username = ""
password = ''
date = "20120201"
xpaths = { 'usernameTxtBox' : ".//*[@id='Email']",
           'passwordTxtBox' : ".//*[@id='Passwd']",
           'submitButton' :   ".//*[@id='mainContent']/div[2]/div/form/div[2]/div/div[2]/input",
           'next' : ".//*[@id='next']",
           'datebox' : ".//*[@id='date']"
         }

mydriver = webdriver.Firefox()
mydriver.get(baseurl)
mydriver.maximize_window()

#Clear Username TextBox if already allowed "Remember Me" 
#mydriver.find_element_by_xpath(xpaths['usernameTxtBox']).clear()
import time
time.sleep(10)
mydriver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(2)
#Write Username in Username TextBox
mydriver.find_element_by_xpath(xpaths['datebox']).send_keys(date)

#Clear Password TextBox if already allowed "Remember Me" 
#mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).clear()
time.sleep(5)

#Write Password in password TextBox
#mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password)

#Click Login button
mydriver.find_element_by_xpath(xpaths['submitButton']).click()

time.sleep(5)
records = mydriver.find_element_by_xpath(".//*[@id='mainContent']/div[2]/div/div/div[4]")
print(records.text)
print(records.url)
#Write Password in password TextBox
#mydriver.find_element_by_xpath(xpaths['passwordTxtBox']).send_keys(password)


#mydriver.find_element_by_xpath(xpaths['submitButton']).click()

