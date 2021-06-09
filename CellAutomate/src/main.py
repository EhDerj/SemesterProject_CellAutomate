"""Main module."""
from modules.model import Model, LifeMap, RulesNearCells
from modules.controller import Controller
from modules.view import View
import os
import gettext


def initLocale():
    """Init locale."""
    gettext.install("base", os.path.dirname("./src/modules/view/ru"))


def initModel():
    """Init model instance."""
    map = LifeMap((50, 50))
    manager = RulesNearCells(2, None, True, {})
    return Model(map, manager)


def initController(model):
    """Init controller instance."""
    return Controller(model)


def initView(controller):
    """Init view instance."""
    return View(controller)


if __name__ == '__main__':
    initLocale()

    model = initModel()
    controller = initController(model)
    view = initView(controller)

    view.mainloop()
