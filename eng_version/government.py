from random import randint
from constants import *
from messages import *

class Government:

    def __init__(self):
        self.__money = randint(GOVERNMENT_MIN_MONEY, GOVERNMENT_MAX_MONEY)


    def __add_money(self, money):
        if money > 0:
            self.__money += money

    def check_canteen(self, food, cook):
        isExpiredFound = False
        indexes = []
        print(CHECK_CANTEEN_MESSAGE)
        for i in range(AMOUNT_OF_DISHES):
            if(food[i].isExpired):
                isExpiredFound = True
                indexes.append(i)
        indexes.reverse()
        for i in indexes:
            food.pop(i)

        if(isExpiredFound):
            print(EXPIRED_DISHES_MESSAGE)

            cook.take_money(FINE)
            self.__add_money(FINE)

            print("Money left: " + str(cook.money))
            if(cook.isBankrupt()):
                print(BANKRUPT_MESSAGE)

        else:
            print(NO_EXPIRED_DISHES_MESSAGE)

        return len(indexes)
