from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
actions = ActionChains(driver)
driver.get('https://monkeytype.com/') #the url to the page selenium will read.
time.sleep(2) #wait for page to load

letter_list = []

time.sleep(10)
#accept = driver.find_element(By.CLASS_NAME, 'acceptAll').click()

get_words =  driver.find_element(By.ID,"words") #the parent div that needs to be looped over
words = (get_words.text.split())
print(words)
space = " "   

for i in words:
    actions.send_keys(i)
    actions.send_keys(space)
    actions.perform()

time.sleep(300)
driver.close()