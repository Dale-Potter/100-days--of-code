import sys
if sys.version_info[0] < 3:
    import Tkinter as tk
else:
    import tkinter as tk
	
import numpy as np
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg
from matplotlib.figure import Figure

class grapher_gui(tk.Tk):
    def __init__(self,parent):
        tk.Tk.__init__(self,parent)
        self.parent = parent
        self.graph()

    def graph(self):
        x_vals = np.linspace(0, 2 * np.pi, 50)
        y_vals = np.sin(x_vals)
		
        toplevel = tk.Toplevel(width=2000)
        figure = Figure(figsize=(10,5))
        ax = figure.add_subplot(111)
        plot = ax.plot(x_vals, y_vals, 'k-')
        ax.set_xlabel('Time')
        ax.set_ylabel('Numbers')
        ax.set_title('Title')

        canvas = FigureCanvasTkAgg(figure, master=toplevel)
        canvas.show()
        canvas.get_tk_widget().grid(row=0)            
        toolbar = NavigationToolbar2TkAgg(canvas, toplevel)
        toolbar.grid(row=1, sticky=tk.W) 
        toolbar.update() 
        toplevel.mainloop()

if __name__ == "__main__":
    app = grapher_gui(None)
    app.title('Plotter')
    app.mainloop()