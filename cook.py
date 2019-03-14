from datetime import datetime
from random import choice, randint
import food as f


class People(object):
    def __init__(self, name, surname, money):
        self.name = name
        self.surname = surname
        self.money = money


class Cook(People):
    """Отвечает за работу поварихи"""

    def __init__(self):
        super(People, self).__init__()

    def create_food(self):
        """Готовка еды поворихой"""
        food = [["Селедка", 2.0, 150], ["Борщ", 0.5, 65], ["Говядина", 3.5, 210], ["Курица", 2.0, 110],
                ["Щи", 0.6, 70], ["Отбивная", 3.0, 310], ["Греча", 1.2, 110], ["Салат 'Морской'", 1.6, 90],
                ["Салат 'Весенний'", 1.10, 67], ["Рис", 1.30, 190]]
        dish = choice(food)
        self.money -= (dish[1]) / 2
        new_dish = f.Food(dish[0], dish[1], dish[2])
        return new_dish

    def get_money(self, food):
        """Заработок поварихи"""
        self.money += food.cost
        print("Сейчас у поварихи: " + str(self.money))

    def __str__(self):
        rep = "Повариха: " + self.name + " " + self.surname + ".\nКоличество денег - " + str(self.money) + "."
        return rep


class Consumer(People):
    """Отвечает за покупаетелей"""

    def __init__(self):
        super(People, self).__init__()
        self.eat = randint(300, 700)
        self.healthy = choice([6, 9])

    def buy_food(self, food, cook):
        """Покупка еды"""
        if self.money >= food.cost:
            self.money = self.money - food.cost
            cook.get_money(food)
            print("Вы съели - " + food.name + ".\n")
            self.__private_eating(food)
            self.__private_poison(food)

    def __private_poison(self, food):
        """Вероятность отравления"""
        if datetime.now() > food.time:
            if choice([0, 1, 0, 0]):
                print("Вы отравились (-3hp).")
                self.__private_hp()

    def free_food(self, food):
        """Попытаться найти еду"""
        find = False
        print("Пытаюсь найти еду...\n")
        if choice([0, 1, 0, 0, 0]):
            print("Вы нашли еду!")
            find = True
        if find:
            food_to_eat = choice(food)
            food.pop(food.index(food_to_eat))
            print("Вы съели " + food_to_eat.name + ".")
            self.__private_eating(food_to_eat)
            self.__private_poison(food_to_eat)
            return food
        else:
            print("Вы не нашли еду.\n")

    def __private_eating(self, food):
        """Кушать"""
        self.eat -= food.kkal
        print("Вам осталось съесть - " + str(self.eat) + ".")

    def __private_hp(self):
        """Отвечает за здоровье"""
        self.healthy -= 3
        if self.healthy == 0:
            print("Вы умерли прямо в столовой ... \n")
        else:
            print(str(self.healthy) + " - здоровье.")

    def __str__(self):
        rep = "покупатель:\n " + self.name + " " + self.surname + ". Количество денег - " + str(self.money) + "."
        rep += "Cколько нужно съесть - " + str(self.eat) + "."
        rep += "Здоровье - " + str(self.healthy) + "."
        return rep

    __repr__ = __str__
