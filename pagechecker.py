import requests
from bs4 import BeautifulSoup
import time
import hashlib

TOKEN = "TelegramToken"
CHAT_ID = "TelegramChatID"
URL = "URLToCheck"

def get_page_content(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return str(soup)

def send_telegram_message(message):
    base_url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
    response = requests.get(base_url)
    return response.json()

def monitor_website():
    old_hash = ''
    while True:
        current_page = get_page_content(URL)
        current_hash = hashlib.md5(current_page.encode()).hexdigest()
        if old_hash != current_hash:
            print("PrintOnConsole")
            send_telegram_message("MessageOfYourChoice")
            old_hash = current_hash
        time.sleep(5)  # check every 5 seconds

monitor_website()
