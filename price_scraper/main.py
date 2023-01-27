from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Get the website using the Chrome webbdriver
driver = webdriver.Chrome()
driver.get('https://www.cclonline.com/pc-components/graphics-cards/nvidia-chipset-graphics-cards/')

#list of element IDs, put in loop and loop through to return multiple prices.

gpu_list = {
    #"3050": "ctl28_complexproductlist_rptProducts_productItem_14_priceBox_14_pnlPriceText_14",
    #"3060": "ctl28_complexproductlist_rptProducts_productItem_0_priceBox_0_pnlPriceText_0",            
    #"3070": "ctl28_complexproductlist_rptProducts_productItem_10_priceBox_10_pnlPriceText_10",
    "3080": "ctl28_complexproductlist_rptProducts_productItem_1_priceBox_1_pnlPriceText_1"
            
    }

#working to find price for 3060
#div = driver.find_element(By.ID, 'ctl28_complexproductlist_rptProducts_productItem_0_priceBox_0_pnlPriceText_0')

#looping through dictionary to get the name of the gpu and more than one item.
total = ""
for items in gpu_list.values():
    #searches for html id that is in dictionary
    res = driver.find_element(By.ID, items) 
    print(res)
    #strips down text so that only the price is remaining
    final = res.text[10:16]
    #adds all returned values to string
    total = total + f"Cost of the gpu is £{final}\n"
    
print(total)





# Print out the result
#print("result: " + div.text)

#trying to strip result to just the cost


# Close the browser
time.sleep(3)
driver.close()