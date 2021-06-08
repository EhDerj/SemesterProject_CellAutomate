import tkinter as tk
from utils.colors import Colors
from collections import namedtuple
from tkinter import messagebox


RectangleSize = namedtuple('RectangleSize', ['width', 'height'])

CELL_SIZE = 10
LIFE_DELAY = 500

colors = [color for color in Colors().colors][1:len(Colors().colors)//2]
colorMap = Colors().colors


class View(tk.Frame):
  '''Cell automate GUI.'''

  def __init__(self, controller):
    '''Create root window with frame, tune weight and resize.'''
    super().__init__(None)
    self.controller = controller
    self.lifemapSize = RectangleSize(*controller.getLifemapSize())

    # Set up grid
    self.master.columnconfigure(0, weight=1)
    self.master.rowconfigure(0, weight=1)
    self.grid(sticky="NEWS")
    for column in range(self.grid_size()[0]):
      self.columnconfigure(column, weight=1)
    for row in range(self.grid_size()[1]):
      self.rowconfigure(row, weight=1)

    self.chosenColors = [tk.IntVar(self, int(i == 0)) for i, x in enumerate(colors)]
    self.isLifeStarted = False
    self.showWelcomeWindow()

  def destroyAllWidgets(self):
    '''Destroy all widgets at window frame.'''
    for widget in self.winfo_children():
       widget.destroy()
          
  def showWelcomeWindow(self):
    '''Show welcome window.'''
    self.stopLife()
    
    # Set up window
    self.master.title('Добро пожаловать в клеточный мир!')
    self.destroyAllWidgets()

    # Set up widgets
    self.cbColors = []
    for i, color in enumerate(colors):
      rbColor = tk.Checkbutton(self, text = color, variable = self.chosenColors[i])
      rbColor.pack()
      self.cbColors.append(rbColor)
    self.btnEnter = tk.Button(self, text='Enter!', command=self.showMainWindow)
    self.btnEnter.pack()
    
  def showMainWindow(self):
    '''Show main window.'''
    hasAnyColor = any([isChoosed.get() == 1 for isChoosed in self.chosenColors])
    if not hasAnyColor:
      messagebox.showerror('No chosen colors', 'Choose any color to continue')
      return

    # Init state
    self.map = [[0] * self.lifemapSize.width for i in range(self.lifemapSize.height)]
    self.iteration = 0
    self.mapColorIndices = list(filter(lambda x: x >= 0, [1 + colorIndex if isChoosed.get() == 1 else -1 for colorIndex, isChoosed in enumerate(self.chosenColors)]))

    # Set up window
    self.master.title('Клеточный мир!')
    self.destroyAllWidgets()
    
    # Set up widgets
    self.cvsCells = tk.Canvas(self, width=self.lifemapSize.width * CELL_SIZE, height=self.lifemapSize.height * CELL_SIZE)
    self.cvsCells.bind('<B1-Motion>', self.on_CvsCells_HoldingMouseOver)
    self.btnStart = tk.Button(self, text='Start', command=self.startLife)
    self.btnStop = tk.Button(self, text='Stop', command=self.stopLife, state='disabled')
    self.btnExit = tk.Button(self, text='Exit', command=self.showWelcomeWindow)
    self.cvsCells.grid()
    self.btnStart.grid()
    self.btnStop.grid()
    self.btnExit.grid()

    self.refreshMap()
    self.refreshScene()

  def draw(self, i, j, colorIndex):
    '''Fill (i,j) cell with color with colorIndex'''
    x0, y0 = j * CELL_SIZE, i * CELL_SIZE
    color = colorMap[colorIndex]
    self.cvsCells.create_rectangle(x0, y0, x0 + CELL_SIZE, y0 + CELL_SIZE, fill=color, outline='#eee')

  def refreshScene(self):
    '''Refreshes cells.'''
    self.cvsCells.delete('all')
    for i, row in enumerate(self.map):
      for j, colorIndex in enumerate(row):
        self.draw(i, j, colorIndex)
  
  def refreshMap(self):
    '''Requests fresh map from model.'''
    self.iteration += 1
    self.map = [[[0, *self.mapColorIndices][(i + j + self.iteration) % (len(self.mapColorIndices) + 1)] for j in range(self.lifemapSize.width)] for i in range(self.lifemapSize.height)]

  def iterateLifeLoop(self):
    '''Iterates life by refreshing map and scene.'''
    self.refreshMap()
    self.refreshScene()
    self.lifeLoopId = self.after(LIFE_DELAY, self.iterateLifeLoop)

    self.btnStart['state'] = 'disabled'
    self.btnStop['state'] = 'normal'

  def startLife(self):
    '''Starts life.'''
    self.isLifeStarted = True
    self.iterateLifeLoop()
    
  def stopLife(self):
    '''Starts life.'''
    if self.isLifeStarted:
      self.isLifeStarted = False
      self.after_cancel(self.lifeLoopId)

      self.btnStart['state'] = 'normal'
      self.btnStop['state'] = 'disabled'

  def on_CvsCells_HoldingMouseOver(self, e):
    '''Handling mouse motion on canvas with holded left button'''
    width, height = self.lifemapSize
    i, j = e.y // CELL_SIZE, e.x // CELL_SIZE
    if i >= 0 and i < height and j >= 0 and j < width:
      self.map[i][j] = 2
      self.draw(i, j, 2)
