#Two modules used to scheduler execution of app
from apscheduler.schedulers.blocking import BlockingScheduler
import subprocess
	
#Fucntion to run Checkup.py, must also call 'python' for it to run
def Checkup():
    subprocess.call(['python', 'Checkup.py'])

#Create a block to schedule and add the job created earlier
scheduler = BlockingScheduler()
scheduler.add_job(Checkup, 'interval', hours = 1)
scheduler.start()




