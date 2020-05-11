from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from price_updater import scraper

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(scraper.updatePrices, 'interval', minutes=60*24)
    scheduler.start()