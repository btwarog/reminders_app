import requests
import time
import os
from datetime import datetime
import pytz
from dotenv import load_dotenv

# Load environment variables from .env file if it exists
load_dotenv()

# Config - get from environment variables with fallback to defaults
BOT_TOKEN = os.getenv('BOT_TOKEN')
CHAT_ID = os.getenv('CHAT_ID')

# Const
INTERVAL_MINUTES = 10

def send_telegram_message(message):
    url = f'https://api.telegram.org/bot{BOT_TOKEN}/sendMessage'
    payload = {
        'chat_id': CHAT_ID,
        'text': message,
        'disable_notification': True  # brak dźwięku
    }
    response = requests.post(url, data=payload)
    return response.status_code == 200

def is_within_active_hours():
    warsaw_tz = pytz.timezone('Europe/Warsaw')
    now = datetime.now(warsaw_tz)
    return 7 <= now.hour <= 22

def main():
    warsaw_tz = pytz.timezone('Europe/Warsaw')
    print("⏳ Bot uruchomiony.")
    while True:
        if is_within_active_hours():
            success = send_telegram_message("🔔 Przypomnienie!")
            print(f"[{datetime.now(warsaw_tz)}] Wysłano: {success}")
        else:
            print(f"[{datetime.now(warsaw_tz)}] Poza godzinami – brak powiadomienia.")
        time.sleep(INTERVAL_MINUTES * 60)

if __name__ == '__main__':
    main()
