from datetime import datetime, timedelta
from random import randint


class Food:
    __food_counter = 0

    @classmethod
    def counter_food(cls):
        return Food.__food_counter

    def __init__(self, name, cost, calorie):
        self.__name = name
        self.__cost = cost
        self.__calorie = calorie
        self.__shelf_life = datetime.now() + timedelta(days=randint(-10, 20))
        if (self.__shelf_life < datetime.now()):
            self.__cost /= 2
            self.__isExpired = True
        else:
            self.__isExpired = False
        Food.__food_counter += 1

    def __str__(self):
        string = self.__name + ": cost: " + str(self.__cost) + \
                 "; calorie: " + str(self.__calorie) + "; shelf life: " + self.__shelf_life.strftime("%d.%m.%Y")
        if self.__isExpired:
            string += "(expired)"
        return string


    @property
    def cost(self):
        return self.__cost

    @property
    def name(self):
        return self.__name

    @property
    def calorie(self):
        return self.__calorie

    @property
    def isExpired(self):
        return self.__isExpired
