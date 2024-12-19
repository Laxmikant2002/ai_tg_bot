import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
from config import Config

def fetch_industry_data(industry):
    url = f"https://example.com/industry/{industry}/trends"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        # Extract data from the soup object
        trends = {
            "cpc": soup.find("div", {"id": "cpc"}).text,
            "ctr": soup.find("div", {"id": "ctr"}).text,
            "conversion_rate": soup.find("div", {"id": "conversion_rate"}).text,
        }
        return trends
    else:
        return None

def store_trends_in_db(industry, trends):
    client = MongoClient(Config.DATABASE_URL)
    db = client.trends_db
    collection = db.trends
    collection.update_one({"industry": industry}, {"$set": trends}, upsert=True)

def update_trends(industry):
    trends = fetch_industry_data(industry)
    if trends:
        store_trends_in_db(industry, trends)