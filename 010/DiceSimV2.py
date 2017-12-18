#DiceSimV2

from Tkinter import *
import random


def NumberGen():
	"""Function generates a random number between 1 to 6.
	Then configures a new image on to the buttom according
	to the random number"""
	
	random_number = random.randint(1,6)
	
	if random_number == 1:
		Roll = '#1.gif'
	elif random_number == 2:
		Roll = '#2.gif'
	elif random_number == 3:
		Roll = '#3.gif'
	elif random_number == 4:
		Roll = '#4.gif'
	elif random_number == 5:
		Roll = '#5.gif'
	elif random_number == 6:
		Roll ='#6.gif'
	else:
		Roll ='Dice.gif'
		
	img2 = PhotoImage(file = Roll)
	Dice.configure(image = img2)
	Dice.image = img2

root = Tk()

img = PhotoImage(file= 'Dice.gif')
Dice = Button(root, image = img, command = NumberGen)
#Used to keep a referrence
Dice.image = img
Dice.pack()
root.mainloop()