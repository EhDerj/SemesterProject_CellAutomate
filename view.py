'''
Tkinter skeleton app
'''
import tkinter as tk
from CellAutomate.colors import Colors
from collections import namedtuple


MAP_SIZE = namedtuple('RectangleSize', ['width', 'height'])(50, 50)
CELL_SIZE = 10
colors = [color for color in Colors().colors][1:len(Colors().colors)//2]


class CellAutomateGUI(tk.Frame):
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

    self.chosenColor = tk.IntVar()
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

    # Init state
    self.map = [[0] * MAP_SIZE.width for i in range(MAP_SIZE.height)]
    self.iteration = 0

    # Set up window
    self.master.title('Клеточный мир!')
    self.destroyAllWidgets()
    
    # Set up widgets
    self.cvsCells = tk.Canvas(self, width=MAP_SIZE.width * CELL_SIZE, height=MAP_SIZE.height * CELL_SIZE)
    self.btnExit = tk.Button(self, text='Exit!', command=self.showWelcomeWindow)
    self.cvsCells.grid()
    self.btnExit.grid()

    self.refreshMap()
    self.refreshScene()

  def refreshScene(self):
    '''Refresh cells.'''
    for i, row in enumerate(self.map):
      for j, colorIndex in enumerate(row):
        x0, y0 = j * CELL_SIZE, i * CELL_SIZE
        color = ['white', *colors][colorIndex]
        self.cvsCells.create_rectangle(x0, y0, x0 + CELL_SIZE, y0 + CELL_SIZE, fill=color, outline='#eee')
  
  def refreshMap(self):
    self.iteration += 1
    self.map = [[(i + j + self.iteration) % 2 for j in range(MAP_SIZE.width)] for i in range(MAP_SIZE.height)]

