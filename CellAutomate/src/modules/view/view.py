"""Cell automate view."""
import tkinter as tk
from tkinter import ttk, END
from tkinter import messagebox
from utils.types import RectangleSize


class View(tk.Frame):
    """Cell automate GUI."""

    CELL_SIZE = 15
    LIFE_DELAY = 250

    def __init__(self, controller):
        """Create root window with frame, tune weight and resize."""
        super().__init__(None)
        self.controller = controller

        # Set up grid
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.grid(sticky="NEWS")
        for column in range(self.grid_size()[0]):
            self.columnconfigure(column, weight=1)
        for row in range(self.grid_size()[1]):
            self.rowconfigure(row, weight=1)

        self.isLifeStarted = False
        self.showWelcomeWindow()

    def destroyAllWidgets(self):
        """Destroy all widgets at window frame."""
        for widget in self.winfo_children():
            widget.destroy()

    # Welcome

    def showWelcomeWindow(self):
        """Show welcome window."""
        self.stopLife()
        self.controller.model.setLifeMap()
        self.synRuleSetupList()

        # Set up window
        self.master.title(_('Welcome to the Cell World!')) # noqa
        self.destroyAllWidgets()

        # Set up widgets
        self.lbRuleSetups = tk.Listbox(self, width=60)
        self.lbRuleSetups.bind(
            '<<ListboxSelect>>',
            self.on_lbRuleSetups_Select,
        )
        self.refreshLbRuleSetups()
        self.lbRuleSetups.pack(
            padx=20,
            pady=20,
        )

        self.lbColors = tk.Listbox(self, selectmode='multiple')
        self.lbColors.bind('<<ListboxSelect>>', self.on_lbColors_Select)
        # self.lbColors.pack() # Hide for uselessness

        self.btnEnter = tk.Button(
            self,
            text=_('Enter!'), # noqa
            command=self.showMainWindow
        )
        self.btnEnter.pack(
            padx=20,
            pady=20,
        )

        self.lbRuleSetups.selection_set(0, 0)
        self.on_lbRuleSetups_Select(None)
        self.on_lbColors_Select(None)

    def refreshLbRuleSetups(self):
        """Refresh listbox rule setups."""
        self.lbRuleSetups.delete(0, 'END')
        for index, ruleSetup in enumerate(self.ruleSetupList):
            ruleSourceFilename = ruleSetup[0]
            self.lbRuleSetups.insert(index, ruleSourceFilename)

    def refreshLbColors(self):
        """Refresh listbox rule setups."""
        selectedRuleSetup = self.ruleSetupList[self.selectedRuleSetupIndex]
        colorsInstance = selectedRuleSetup[2]
        self.colorMap = colorsInstance.colors
        self.colors = colorsInstance.colorSeq[1:]

        self.lbColors.delete(0, END)
        for i, color in enumerate(self.colors):
            self.lbColors.insert(i, color)
        self.lbColors.selection_set(0, END)

    def synRuleSetupList(self):
        """Refresh rule setup list."""
        self.ruleSetupList = self.controller.getRuleFiles()

    def on_lbRuleSetups_Select(self, e):
        """Handle rule setups list box select."""
        curSelection = self.lbRuleSetups.curselection()
        if len(curSelection) > 0:
            self.selectedRuleSetupIndex = curSelection[0]
            self.refreshLbColors()

    def on_lbColors_Select(self, e):
        """Handle colors list box select."""
        curSelection = self.lbColors.curselection()
        if len(curSelection) > 0:
            self.chosenColors = list(curSelection)

    # Main

    def showMainWindow(self):
        """Show main window."""
        hasAnyColor = hasattr(self, "chosenColors")
        if not hasAnyColor:
            messagebox.showerror(
                _('No chosen colors'), # noqa
                _('Choose any color to continue') # noqa
            )
            return

        # Init state
        self.lifemapSize = RectangleSize(*self.controller.getLifemapSize())
        self.map = []
        for i in range(self.lifemapSize.height):
            self.map.append([0] * self.lifemapSize.width)
        self.iteration = 0
        chosenColorIndices = list(map(lambda x: 1 + x, self.chosenColors))
        self.mapColorIndices = chosenColorIndices
        self.controller.initModel(self.selectedRuleSetupIndex, len(self.chosenColors) + 1)
        self.lifemapSize = RectangleSize(*self.controller.getLifemapSize())

        # Set up window
        self.master.title(_('Cell World...')) # noqa
        self.destroyAllWidgets()

        # Init widgets
        self.cvsCells = tk.Canvas(
            self,
            width=self.lifemapSize.width * View.CELL_SIZE,
            height=self.lifemapSize.height * View.CELL_SIZE
        )
        self.cvsCells.bind('<B1-Motion>', self.on_CvsCells_HoldingMouseOver)
        self.cvsCells.bind('<ButtonPress-1>', self.on_CvsCells_HoldingMouseOver)
        self.btnStart = tk.Button(self, text=_('Start'), command=self.startLife) # noqa
        self.btnStop = tk.Button(
            self,
            text=_('Stop'), # noqa
            command=self.stopLife,
            state='disabled'
        )
        self.btnExit = tk.Button(
            self,
            text=_('Exit'), # noqa
            command=self.showWelcomeWindow
        )
        cbValues = [
            'White',
            *map(lambda x: self.colorMap[x], self.mapColorIndices),
        ]
        self.cbDrawColor = ttk.Combobox(
            self,
            values=cbValues,
            state='readonly'
        )
        self.cbDrawColor.current(1)

        # Place widgets
        self.cvsCells.grid(columnspan=4)
        self.cbDrawColor.grid(row=1, column=0, pady=8)
        self.btnStart.grid(row=1, column=1, pady=8)
        self.btnStop.grid(row=1, column=2, pady=8)
        self.btnExit.grid(row=1, column=3, pady=8)

        self.refreshMap()
        self.refreshScene()

    def checkOutbounds(self, i, j):
        """Check i, j places at lifemap."""
        width, height = self.lifemapSize
        return i >= 0 and i < height and j >= 0 and j < width

    def draw(self, i, j, colorIndex):
        """Fill (i,j) cell with color with colorIndex."""
        if self.checkOutbounds(i, j):
            x0, y0 = j * View.CELL_SIZE, i * View.CELL_SIZE
            x1, y1 = x0 + View.CELL_SIZE, y0 + View.CELL_SIZE
            color = self.colorMap[colorIndex]
            return self.cvsCells.create_rectangle(
                x0, y0, x1, y1, fill=color, outline='#eee')
        else:
            return None

    def refreshScene(self):
        """Refresh cells."""
        self.cvsCells.delete('all')
        for i, row in enumerate(self.map):
            for j, colorIndex in enumerate(row):
                self.draw(i, j, colorIndex)

    def refreshMap(self):
        """Request fresh map from model."""
        self.iteration += 1
        self.map = self.controller.getMap().getCellMatrix()

    def iterateLifeLoop(self):
        """Iterate life by refreshing map and scene."""
        self.controller.makeStep()
        self.refreshMap()
        self.refreshScene()
        self.lifeLoopId = self.after(View.LIFE_DELAY, self.iterateLifeLoop)

        self.btnStart['state'] = 'disabled'
        self.btnStop['state'] = 'normal'

    def startLife(self):
        """Start life."""
        self.isLifeStarted = True
        self.controller.setCellMatrix(self.map)
        self.iterateLifeLoop()

    def stopLife(self):
        """Start life."""
        if self.isLifeStarted:
            self.isLifeStarted = False
            self.after_cancel(self.lifeLoopId)

            self.btnStart['state'] = 'normal'
            self.btnStop['state'] = 'disabled'

    def on_CvsCells_HoldingMouseOver(self, e):
        """Handle mouse motion on canvas with holded left button."""
        if self.isLifeStarted:
            messagebox.showwarning(
                'Give them freedom, kingbird!',
                'Drawing on living cells is denied')
            return

        i, j = e.y // View.CELL_SIZE, e.x // View.CELL_SIZE
        if self.checkOutbounds(i, j):
            color = self.cbDrawColor.get() or 'Black'
            colorIndex = self.colorMap[color]
            self.map[i][j] = colorIndex
            self.draw(i, j, colorIndex)
