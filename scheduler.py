import schedule
import scraper
from datetime import datetime, timedelta, time

def job():
    scraper.run()

if __name__ == '__main__':
    startTime = 2*3600
    endTime = 5*3600
    # Run every 2 to 5 hours.
    schedule.every(startTime).to(endTime).seconds.do(job)