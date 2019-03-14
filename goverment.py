from datetime import datetime


class Goverment(object):
    """Отвечает за работу правительства"""

    def __init__(self, money):
        self.money = money

    def take_money(self, cook):
        """Берет налог у поварихи"""
        print("Государство взяло налог В размере 1%.\n")
        PERCENT = 0.01
        self.money += cook.money * PERCENT
        cook.money -= cook.money * PERCENT

    def sell_by_date(self, food, cook):
        """Проверяет срок годности продукции"""
        COUNTER_OF_FOOD = 9
        pop_list = []
        print("Будет изъято по 25р за каждый просроченый товар.\n")
        for i in range(COUNTER_OF_FOOD):
            if food[i].time < datetime.now():
                print("Инспекция нашла просроченную еду!")
                pop_list.append(i)
                self.__private_fine(cook)
        return (self.__private_delete_bad_food(pop_list, food))

    def __private_delete_bad_food(self, pop_list, food):
        """Удаление просроченной еды"""
        pop_list.reverse()
        for i in range(len(pop_list)):
            food.pop(pop_list[i])
        return food

    def __private_fine(self, cook):
        """Берёт таксу за просрок"""
        FINE = 25
        self.money += FINE
        cook.money -= FINE

    def __str__(self):
        rep = "Сейчас в казне правительства: " + str(self.money)
        return rep
