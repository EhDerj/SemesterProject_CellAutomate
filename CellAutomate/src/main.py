"""Main module."""
from modules.model import Model, LifeMap, RulesNearCells
from modules.controller import Controller
from modules.view import View
import gettext


def initLocale():
    """Init locale."""
    gettext.install("view", "./src/modules/view/locales/")


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
