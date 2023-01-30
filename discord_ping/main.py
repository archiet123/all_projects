from datetime import datetime
import requests

url_webhook = "https://discord.com/api/webhooks/1069570843807596595/W5t99ZaTbWbDitxpQgcdqDD9GkLc1qdtAk52tKSkFlcAhagsPcMbG7cE33uzO5fPSuy8" #my server

#url_webhook = "https://discord.com/api/webhooks/1069573236821590057/KpcBeoNtPTYmkYw8g_Rzc3vgruwYDp9whtO6vfuvMGzlMiFOK9VLijyK9qTmZqxSKqrU"#T level server

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