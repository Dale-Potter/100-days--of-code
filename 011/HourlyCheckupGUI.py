#HourlyCheckupGUI

"""from tkinter import *

class HourlyCheckupGUI:

	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		Label(frame, text = 'Rate Concentration...',).grid(row=0, columnspan = 2)
		Scale(frame, from_= 0, to = 5, orient=HORIZONTAL).grid(row=1, columnspan = 2)
		Label(frame, text = 'What are you working on?').grid(row = 2, columnspan = 2)
		self.Comments = StringVar()
		Entry(frame, textvariable = self.Comments).grid(row = 3, columnspan = 2)
		Label(frame, text = 'Any questions or ideas?').grid(row = 4, columnspan = 2)
		self.Questios = StringVar()
		Entry(frame, textvariable = self.Questios).grid(row = 5, columnspan = 2)
		Button(frame, text = 'REPORT', command = root.destroy).grid(row = 6, columnspan = 2)

		
root = Tk()
root.wm_title('Hourly Checkup')
app = HourlyCheckupGUI(root)
root.mainloop()"""

import sys
from tkinter import *

ABOUT_TEXT = """Test1"""

DISCLAIMER = """
Test 2 """

def clickAbout():
	popup = Toplevel()
	label1 = Label(popup, text = 'Rate Concentration...',height=0, width=50)
	label1.pack()
	label2 = Scale(popup, from_= 0, to = 5, orient=HORIZONTAL, width=20)
	label2.pack()
	label3 = Label(popup, text = 'What are you working on?',height=0, wigth = 50)
	label3.pack()
	


app = Tk()
app.title("Hourly Checkup")
app.geometry("350x100+200+200")

label = Label(app, text="Be the person today, who you would want to define your life.", height=0, width=100)
b = Button(app, text="Quit", width=20, command=app.destroy)
button1 = Button(app, text="Track progress", width=20, command=clickAbout)
label.pack()
b.pack(side='bottom',padx=0,pady=0)
button1.pack(side='bottom',padx=5,pady=5)

app.mainloop()
