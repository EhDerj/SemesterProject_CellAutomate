from modules.model import Model, LifeMap, RulesNearCells
from modules.controller import Controller
from modules.view import View


if __name__ == '__main__':
  map = LifeMap((25, 25))
  manager = RulesNearCells({}, 1)

  model = Model(map, manager)
  controller = Controller(model)
  view = View(controller)

  view.mainloop()
