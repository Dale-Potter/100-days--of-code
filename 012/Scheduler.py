#Scheduler

#Import relevant module to allow intervals of 60 minutes
from apscheduler.schedulers.blocking import BlockingScheduler

#Test function
def some_job():
	print ("test") 

#Create block scheduler function
scheduler = BlockingScheduler()

#Assign a job to scheduler, with interval and required time
scheduler.add_job(some_job, 'interval', minutes = 60)

#Start the assigned jobs
scheduler.start()