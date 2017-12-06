#CodeCounter

import datetime as dt

def date():
	date = dt.datetime.now()
	date = str(date)
	date = date.split('.')[0]
	return date
	
def time():
	print('How much time have you spent coding today, broke down to hours and minutes?')
	hours = raw_input('How many hours spent coding:  ')
	minutes = raw_input('How many minutes spent coding:  ')
	return hours, minutes
	
def comments():
	comment = raw_input('What were you working on? (Eg. project, course, ...)')
	learn = raw_input('What new module or coding did you learn about?  ')
	return comment, learn


hour, min = time()
comment, learnt = comments()
day = date()
	
	

storage = open('CodeCounterStorage.txt','a+')
storage.write( day + ',' +  hour + ',' + min + ',' + comment + ' ' + learnt + '\n')
storage.close()
