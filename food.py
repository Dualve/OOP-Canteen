from datetime import datetime
from random import randint


class Food(object):
    """Еда в столовой"""

    def __init__(self, name, cost, kkal):
        self.name = name
        self.cost = cost
        self.kkal = kkal
        year = 2019
        month = randint(2, 6)
        day = randint(1, 28)
        self.time = datetime(year, month, day)

    def __str__(self):
        rep = self.name + " цена: " + str(self.cost) + "."
        rep += " Ккал - " + str(self.kkal) + ". Годно до:" + self.time.strftime("%d.%m.%Y")
        return rep

    __repr__ = __str__
