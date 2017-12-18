#DiceSim

from Tkinter import *
import random

class DiceGUI:

	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		self.photo = PhotoImage(file = 'Dice.gif')
		Dice = Button(frame, image = self.photo, command = self.NumberGen)
		Dice.grid(row = 0, column = 0)
		self.result = DoubleVar()
		Label(frame, textvariable = self.result).grid(row=1, column=0)
				
	def NumberGen(self):
		random_number = random.randint(1,6)
		self.result.set(random_number)
				
root = Tk()
root.wm_title('Dice Simulator')
app = DiceGUI(root)
root.mainloop()

