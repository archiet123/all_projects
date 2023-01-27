from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import requests

# Get the website using the Chrome webbdriver
driver = webdriver.Chrome()
driver.get('https://www.cclonline.com/pc-components/graphics-cards/nvidia-chipset-graphics-cards/')

# #this is for headless chrome
# options = Options()
# options.add_argument('--headless')
# options.add_argument('--disable-gpu')
# driver = webdriver.Chrome('https://www.cclonline.com/pc-components/graphics-cards/nvidia-chipset-graphics-cards/', chrome_options=options)

webhook_url = "https://discord.com/api/webhooks/1068521584769376349/lf6c7SGCwYxX__-_yqk2qSQIcIaA2SlEhV-i3INvThyq_N1XP5DEWU71y_4wwRAasPRj"
#list of element IDs, put in loop and loop through to return multiple prices.

gpu_list = {
    "3050": "ctl28_complexproductlist_rptProducts_productItem_14_priceBox_14_pnlPriceText_14",
    "3060": "ctl28_complexproductlist_rptProducts_productItem_0_priceBox_0_pnlPriceText_0",            
    "3070": "ctl28_complexproductlist_rptProducts_productItem_10_priceBox_10_pnlPriceText_10",
    "3080": "ctl28_complexproductlist_rptProducts_productItem_3_priceBox_3_pnlPriceText_3"
            
    }

#working to find price for 3060
#div = driver.find_element(By.ID, 'ctl28_complexproductlist_rptProducts_productItem_0_priceBox_0_pnlPriceText_0')

#looping through dictionary to get the name of the gpu and more than one item.
total = ""
for key, value in gpu_list.items():
    #searches for html id that is in dictionary
    res = driver.find_element(By.ID, value)    
    #strips down text so that only the price is remaining
    final = res.text[10:16]
    #adds all returned values to string
    total = total + f"Cost of the {key} is £{final}\n"

print(total)

#content is discords the message that is sent to discord, total is the varible of the data
gpu_data = {'content': "<@307952129958477824>\n" + total}
#sending data
x = requests.post(webhook_url, json = gpu_data)

print(x.headers)

# Print out the result
#print("result: " + div.text)

#trying to strip result to just the cost


# Close the browser
time.sleep(3)
driver.close()