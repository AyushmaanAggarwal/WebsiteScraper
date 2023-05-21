import os
import time
import schedule
import courseScraper
from sendEmail import gmail_send_message


def job():
    courseScraper.run(os.path.abspath(os.getcwd())+'/')
    print("Completed Job")


if __name__ == '__main__':
    gmail_send_message("Script Started", f"Begin scanning websites: {courseScraper.get_sites(os.path.abspath(os.getcwd())+'/')}", os.path.abspath(os.getcwd())+'/')

    startTime = 2*3600
    endTime = 5*3600
    # Run every 2 to 5 hours.
    schedule.every(startTime).to(endTime).seconds.do(job)

    while True:
        schedule.run_pending()
        time.sleep(endTime)
