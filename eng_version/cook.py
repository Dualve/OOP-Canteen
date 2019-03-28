import random
from constants import *
from food import Food


class Cook:

    def __init__(self, surname, name):
        self.__name = name
        self.__surname = surname
        self.__money = random.randint(COOK_MIN_MONEY, COOK_MAX_MONEY)

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname

    @property
    def money(self):
        return self.__money

    def add_money(self, money):
        if money > 0:
            self.__money += money

    def take_money(self, money):
        if money > 0:
            self.__money -= money
            self.__money = round(self.__money,3)
            if(self.__money < 0):
                self.__money = 0


    def cook_food(self):
        name = random.choice(DISHES_NAMES)
        food = Food(name, DISHES_COST[DISHES_NAMES.index(name)], DISHES_CALORIE[DISHES_NAMES.index(name)])
        self.take_money(food.cost/2)
        return food

    def isBankrupt(self):
        return self.__money == 0