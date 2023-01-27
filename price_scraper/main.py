from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Get the website using the Chrome webbdriver
driver = webdriver.Chrome()
driver.get('https://www.cclonline.com/pc-components/graphics-cards/nvidia-chipset-graphics-cards/')

#list of element IDs, put in loop and loop through to return multiple prices.

#res = driver.find_element(By.XPATH, '/html/body/div[14]/form/div[5]/div[2]/div[2]/div/div/div[1]/div[2]/div[2]/div/p/span[2]')
div = driver.find_element(By.ID, 'ctl28_complexproductlist_rptProducts_productItem_0_priceBox_0_pnlPriceText_0')


stripped = div

# Print out the result
#print("result: " + div.text)

#trying to strip result to just the cost
final = div.text[10:16]
print(f"Cost of the gpu is £{final}")

# Close the browser
time.sleep(3)
driver.close()