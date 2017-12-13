#HydraulicDiameter

from Tkinter import *

class HydraulicDiameterGUI:

	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		Label(frame, text = ' Flow Area ').grid(row=0, column = 0)
		self.c_var = DoubleVar()
		Entry(frame, textvariable=self.c_var) .grid(row = 0, column = 1)
		Label(frame, text = ' Wetter Perimeter').grid(row = 1 , column = 0)
		self.p_var = DoubleVar()
		Entry(frame, textvariable=self.p_var).grid(row = 1, column = 1)
		button = Button(frame, text = 'Calculate', command = self.Calculate)	
		button.grid(row = 2, columnspan = 2)
		self.result_var = DoubleVar()
		Label(frame, textvariable=self.result_var).grid(row = 3, columnspan = 2)
		
	def Calculate(self):
		area = float(self.c_var.get())
		perimeter = float(self.p_var.get())
		Answer = float(4 *(area/perimeter))
		self.result_var.set(Answer)
        
	
root = Tk()
root.wm_title('Equivalent Hydraulic Diamter')
app = HydraulicDiameterGUI(root)
root.mainloop()