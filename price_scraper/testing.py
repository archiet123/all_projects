from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import requests

driver = webdriver.Chrome()
driver.get('https://www.cclonline.com/pc-components/graphics-cards/nvidia-chipset-graphics-cards/')

header = driver.find_element_by_class("productListContainer pt-3")

for i in range(header):
    