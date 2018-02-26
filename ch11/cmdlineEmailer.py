from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get('https://mail.yahoo.com')

#Enter username
elem = browser.find_element_by_id('login-username')
elem.send_keys('USERNAME')

#Click login button
elem = browser.find_element_by_id('login-signin')
elem.click()

#Enter password
time.sleep(3)
elem = browser.find_element_by_id('login-passwd')
elem.send_keys('PASSWORD')

#Enter login password
elem = browser.find_element_by_id('login-signin')
elem.click()

#Click write email button
time.sleep(3)
elem = browser.find_element_by_class_name('btn-compose')
elem.click()

#Enter receiver email
elem = browser.find_element_by_id('to-field')
elem.send_keys('x24870@gmail.com')

#Enter subject
elem = browser.find_element_by_id('subject-field')
elem.send_keys('Email from cmdlineEmailer.py')

#Enter content
time.sleep(3)
elem = browser.find_element_by_id('rtetext')
elem.send_keys('This email was send from cmdlineEmailer.')

#Click send button
elem = browser.find_element_by_class_name('default')
elem.click()