from datetime import datetime
from dotenv import load_dotenv
import requests
import os

load_dotenv()

webhook_url = os.environ.get("WEBHOOK")

now = datetime.now()
current_time = now.strftime("%H:%M")
print("Current Time =", current_time)


counter = 0
while current_time != "16:20" and current_time != "04:20" and current_time != "11:16":    
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    counter = 0
else:
    
    if counter == 0:
        counter = 1
        message = "its working"
        post_message = {
         'content': "<@523197640347746325>\n" + message
        }
        x = requests.post(url_webhook, json = post_message)

    else:
        print("already sent")