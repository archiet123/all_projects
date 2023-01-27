from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import requests

webhook_url = "https://discord.com/api/webhooks/1068521584769376349/lf6c7SGCwYxX__-_yqk2qSQIcIaA2SlEhV-i3INvThyq_N1XP5DEWU71y_4wwRAasPRj"

driver = webdriver.Chrome()
driver.get('https://www.cclonline.com/pc-components/graphics-cards/nvidia-chipset-graphics-cards/attributeslist/1069698,1069694,1069691,1069711,1069692/')

products =  driver.find_elements(By.CLASS_NAME,"productListOverlayWrapper")

def formatElements(elm):
    return elm.text

discordMessage = []
for product in products:#this will loop 20 times for the amount of itmes on the page

    title = product.find_element(By.CLASS_NAME, "productList_Middle_Left").find_element(By.TAG_NAME, "a") #this gets the "a" tag where the name for gpu is
 
    name = title.get_attribute("title")
    url = title.get_attribute("href")

    try:
        # Get price
        spans = product.find_element(By.CLASS_NAME, "price-value-container").find_elements(By.TAG_NAME, "span")#this gets the span where the price for gpu is
        priceValues = map(formatElements, spans)#will run formatElements, every item in spans is passed in. This is to get the text inside of the span
    except: 
        continue
    price = ""
    for j in priceValues:
        if j.startswith("Was") or j.startswith("inc"):#formatting what is returned
            continue
        price += j

    #formatting what is returned, removing £ 
    price = price.replace("£", "")
    discordMessage.append({
        "name": f"{name}",
        "value": f"Price: {price}\n [Link]({url})"
        
    })


print(discordMessage)
#content is discords the message that is sent to discord, total is the varible of the data
gpu_data = {
    # 'content': "<@307952129958477824>\n" + discordMessage
    "embeds": [
        {
            "title": "GPU Prices",
            # "description": discordMessage
            "fields": discordMessage
        }
    ]
    }
#sending data
x = requests.post(webhook_url, json = gpu_data)

print("DONE")