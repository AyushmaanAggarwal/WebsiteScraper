import schedule
import courseScraper
import time
from datetime import datetime, timedelta


def job():
    courseScraper.run()
    print("Completed Job")


if __name__ == '__main__':
    startTime = 2*3600
    endTime = 5*3600
    # Run every 2 to 5 hours.
    schedule.every(startTime).to(endTime).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(endTime)
