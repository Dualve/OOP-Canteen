from random import randint, choice
from constants import *
from messages import *


class Customer:

    def __init__(self, surname, name):
        self.__name = name
        self.__surname = surname
        self.__money = randint(CUSTOMER_MIN_MONEY, CUSTOMER_MAX_MONEY)
        self.__isFat = bool(randint(0,1))
        if self.__isFat:
            self.__calorie_requirement = CALORIE_REQUIREMENT_FOR_FAT
            self.__health = HEALTH_FOR_FAT
        else:
            self.__calorie_requirement = CALORIE_REQUIREMENT
            self.__health = HEALTH

    def __str__(self):
        return self.__surname + " " + self.__name + ": money: " + str(self.__money) + "; isFat: " + str(self.__isFat) + \
               "; health: " + str(self.__health) + "; calorie requirement: "\
               + str(self.__calorie_requirement)

    def buy_food(self, food):
        self.__spend_money(food.cost)

        if(food.isExpired and randint(1,4) == 1):
            self.__reduce_health(POISONING_REDUCTION_OF_HEALTH)
            print("You are poisoned! Health is reduced. " + str(self.health) + " left!")
        else:
            self.__reduce_calorie_requirement(food.calorie)
            print("You have bought " + food.name + "!\n" +
                  "Calorie requirement decreased on " + str(food.calorie) + "\n" +
                  "Calorie requirement left: " + str(self.calorie_requirement) + "\n" +
                  "Money left: " + str(self.money))

    @property
    def money(self):
        return self.__money

    @property
    def calorie_requirement(self):
        return self.__calorie_requirement

    @property
    def health(self):
        return self.__health

    def __reduce_health(self, health):
        if health > 0:
            self.__health -= health
            if(self.__health < 0):
                self.__health = 0

    def __reduce_calorie_requirement(self, calorie_requirement):
        if calorie_requirement > 0:
            self.__calorie_requirement -= calorie_requirement
            if(self.__calorie_requirement < 0):
                self.__calorie_requirement = 0

    def __spend_money(self, money):
        if money > 0:
            self.__money -= money
            self.__money = round(self.__money, 3)

    def panhandle(self, food):
        if(randint(1,5) == 1):
            received_food = choice(food)
            print("Cook has agreed to give you food! She gave you " + received_food.name)
            if (received_food.isExpired and randint(1, 4) == 1):
                self.__reduce_health(POISONING_REDUCTION_OF_HEALTH)
                print("You are poisoned! Health is reduced on 3 points. " + str(self.health) + " left!")
            else:
                self.__reduce_calorie_requirement(received_food.calorie)
                print("Calorie requirement decreased on " + str(received_food.calorie) + "\n" +
                      "Calorie requirement left: " + str(self.calorie_requirement))

        else:
            print("Cook hasn't agreed to give you food!")


    def die(self):
        self.__health = 0
        print(DEATH_MESSAGE)