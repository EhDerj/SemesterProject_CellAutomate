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
          
  def showWelcomeWindow(self):
    '''Show welcome window.'''
    self.master.title('Добро пожаловать в клеточный мир!')
    
  def showMainWindow(self):
    '''Show main window.'''
    self.master.title('Клеточный мир!')


