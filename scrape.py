import os
import sys
import requests
import urllib2
import itertools
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('/usr/bin/chromedriver')
driver.get('https://members.junglescout.com/#/login')
driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/div/div[2]/input[1]').send_keys('e-mail address')
driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/div/div[2]/input[2]').send_keys('password')
'''click "product database"'''
driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/div/div[2]/div/button/div').click()
driver.implicitly_wait(10)

'''?'''
driver.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div[1]/div/div/div[2]/div[1]/div/a[2]').click()
driver.implicitly_wait(5)

'''click arrow for selection'''
driver.find_element_by_xpath('//*[@id="app-content"]/div/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/span[2]').click()
'''driver.find_element_by_xpath('//*[@id="app-content"]/div/div[1]/div[3]/div[1]/div[1]/div[2]/div[1]/img').click()'''

driver.implicitly_wait(5)

'''click German flag'''
driver.find_element_by_xpath('//*[@id="app-content"]/div/div[1]/div[3]/div[1]/div[1]/div[2]/div[2]/div[3]').click()

'''Criteria:'''
'''- Min Price 50'''
driver.find_element_by_xpath('//*[@id="app-content"]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[1]/input[1]').send_keys('50')
'''- Rank 500-2000'''
driver.find_element_by_xpath('//*[@id="app-content"]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[5]/input[1]').send_keys('500')
driver.find_element_by_xpath('//*[@id="app-content"]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[5]/input[2]').send_keys('2000')
'''- Min Sales 300'''
driver.find_element_by_xpath('//*[@id="app-content"]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[7]/input[1]').send_keys('300')
'''- Min Revenue 6000'''
driver.find_element_by_xpath('//*[@id="app-content"]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[9]/input[1]').send_keys('6000')
'''- Max Reviews 80'''
driver.find_element_by_xpath('//*[@id="app-content"]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[2]/input[2]').send_keys('80')
'''- Max LQS 7'''
driver.find_element_by_xpath('//*[@id="app-content"]/div/div[1]/div[3]/div[2]/div[2]/div[2]/div[10]/input[2]').send_keys('7')

'''waits until filter options are there'''
wait1 = WebDriverWait(driver,10)
'''clicks to start search'''
element1 = wait1.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-content"]/div/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]')))

'''csv page 1''' 
driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div[1]/button/div').click()
'''next''' 
driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/ul/li[9]').click()

'''loop starts'''
'''csv page 2, waits until some element is there''' 
for _ in itertools.repeat(None,26):
	element2 = WebDriverWait(driver,20000).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="app-content"]/div/div[1]/div[4]/div[2]/button[2]/div')))
	try:
		driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div[1]/button/div').click()
	except:
		driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/div[1]/button').click()
	driver.implicitly_wait(15)
	'''next''' 
	try:
		driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/ul/li[9]').click()
	except:
		(driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/ul/li[10]').click(),
		driver.find_element_by_xpath('//*[@id="app-content"]/div/div[3]/ul/li[11]').click())

		


