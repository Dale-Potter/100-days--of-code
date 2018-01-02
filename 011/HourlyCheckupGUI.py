#HourlyCheckupGUI

from tkinter import *

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
root.mainloop()


