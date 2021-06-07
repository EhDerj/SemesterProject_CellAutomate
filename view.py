'''
Tkinter skeleton app
'''
import tkinter as tk


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

    # Create widgets
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
    self.btnEnter = tk.Button(self, text='Enter!', command=self.showMainWindow)
    self.btnEnter.grid()
    
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


