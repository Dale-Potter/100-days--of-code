from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
	

def some_job():
    subprocess.call(['python', 'Checkup.py'])

scheduler = BlockingScheduler()
scheduler.add_job(some_job, 'interval', hours = 1)
scheduler.start()




