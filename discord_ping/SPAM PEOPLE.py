from datetime import datetime
from dotenv import load_dotenv
import requests
import os
import time

load_dotenv()

webhook_url = os.environ.get("WEBHOOK")

for i in range(1):        
    message = "now i can send announcements"
    post_message = {
        'content': "<@619595048031485984><@243765211473903616><@609340913147445254><@430696042015490048><@282156061069148160>\n" + message
    }
    requests.post(webhook_url, json = post_message)
    time.sleep(10)

