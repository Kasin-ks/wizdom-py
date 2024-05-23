from generation_llama2_13b import caching_news_mechanism
from web_scraping import scrape
import requests
import os

API_TOKEN = os.environ["TELEGRAM_API_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

def send_message(event=None, context=None):
    scrape_result = scrape()
    summarized_news = caching_news_mechanism(scrape_result)
    message = summarized_news
    
    url = f"https://api.telegram.org/bot{API_TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
    req = requests.get(url)


if __name__ == '__main__':
    send_message()
