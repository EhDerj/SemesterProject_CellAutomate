'''
Tkinter skeleton app
'''
import tkinter as tk
from CellAutomate.colors import Colors


colors = [color for color in Colors().colors][1:len(Colors().colors)//2]


class CellAutomate(tk.Frame):
  '''Cell automate GUI.'''

  def __init__(self, master=None, **kwargs):
    '''Create root window with frame, tune weight and resize.'''
    super().__init__(master, **kwargs)

    # Set up grid
    self.master.columnconfigure(0, weight=1)
    self.master.rowconfigure(0, weight=1)
    self.grid(sticky="NEWS")
    for column in range(self.grid_size()[0]):
      self.columnconfigure(column, weight=1)
    for row in range(self.grid_size()[1]):
      self.rowconfigure(row, weight=1)

    self.chosenColor = tk.IntVar(None)
    self.showWelcomeWindow()

  def destroyAllWidgets(self):
    '''Destroy all widgets at window frame.'''
    for widget in self.winfo_children():
       widget.destroy()
          
  def showWelcomeWindow(self):
    '''Show welcome window.'''
    
    # Set up window
    self.master.title('Добро пожаловать в клеточный мир!')
    self.destroyAllWidgets()

    # Set up widgets
    self.rbColors = []
    for i, color in enumerate(colors):
      rbColor = tk.Radiobutton(self, text = color, variable = self.chosenColor, value = i)
      rbColor.pack()
      self.rbColors.append(rbColor)
    self.btnEnter = tk.Button(self, text='Enter!', command=self.showMainWindow)
    self.btnEnter.pack()
    
  def showMainWindow(self):
    '''Show main window.'''

    # Set up window
    self.master.title('Клеточный мир!')
    self.destroyAllWidgets()
    
    # Set up widgets
    self.cvsMap = tk.Canvas(self)
    self.btnExit = tk.Button(self, text='Exit!', command=self.showWelcomeWindow)
    self.cvsMap.grid()
    self.btnExit.grid()

  

