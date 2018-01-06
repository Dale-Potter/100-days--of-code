#Import modules needed for GUI
import sys
from Tkinter import *
import datetime as dt

#Function to create popup, currently opened with button.
def clickAbout():
	popup = Toplevel()
	label1 = Label(popup, text = 'Rate Concentration...',height=0, width=50)
	label1.pack()
	scale = Scale(popup, from_= 0, to = 5, orient=HORIZONTAL, width=20)
	scale.pack()
	label3 = Label(popup, text = 'What are you working on?',height=0, width = 50)
	label3.pack()
	Comments = StringVar()
	Text1 = Entry(popup, textvariable = Comments,width = 50)
	Text1.pack()
	label4 = Label(popup, text = 'Any questions or ideas?')
	label4.pack()
	Questions = StringVar()
	Text2 = Entry(popup, textvariable = Questions, width = 50)
	Text2.pack()
	Button3 = Button(popup, text = 'REPORT', command = lambda : DATA.write(str(dt.datetime.now()) + '|' + str(scale.get())+ '|' + str(Comments.get()) + '|' + str(Questions.get()) + '\n'), width = 20)
	Button3.pack()

#Create tkinter GUI
#Including title and geometry size
app = Tk()
app.title("Hourly Checkup")
app.geometry("350x100+200+200")

#Create main GUI which allows you to access pop up and exit the program
label = Label(app, text="Be the person today, who you would want to define your life.", height=0, width=100)
button1 = Button(app, text="Quit", width=20, command=app.destroy)
button2 = Button(app, text="Track progress", width=20, command=clickAbout)
label.pack()
button1.pack(side='bottom',padx=0,pady=0)
button2.pack(side='bottom',padx=5,pady=5)

#Open DATA file for scale and input fields
DATA = open('DATA.txt','a')


app.mainloop()