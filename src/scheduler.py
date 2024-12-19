from apscheduler.schedulers.blocking import BlockingScheduler
from scraping.scraper import update_trends

def scheduled_job():
    industries = ["tech", "finance", "healthcare"]
    for industry in industries:
        update_trends(industry)

if __name__ == '__main__':
    scheduler = BlockingScheduler()
    scheduler.add_job(scheduled_job, 'interval', hours=24)
    scheduler.start()