#test
from apscheduler.schedulers.blocking import BlockingScheduler

def some_job():
    print ("test")

scheduler = BlockingScheduler()
scheduler.add_job(some_job, 'interval', seconds = 5)
scheduler.start()