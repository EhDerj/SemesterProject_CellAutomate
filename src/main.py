from modules.model import Model, LifeMap, RulesNearCells
from modules.controller import Controller
from modules.view import View


if __name__ == '__main__':
  map = LifeMap((50, 50))
  manager = RulesNearCells(2, None, True, {})

  model = Model(map, manager)
  controller = Controller(model)
  view = View(controller)

  view.mainloop()
