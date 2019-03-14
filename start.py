from random import choice, randint
import goverment as g
import food as f
import cook as c


def main():
    AMOUNT_OF_CONSUMERS = 5
    COUNTER_OF_FOOD = 10
    answer = {"Yes": True, "No": False}

    print("Доброе пожаловать в столовую.\nСтоловая может обслужить 5 человек в день.\n")
    while True:

        cook = create_cook()
        gov = create_goverment()
        food = []
        customers = []

        print("В столовую приходят посетители!\n")
        for i in range(AMOUNT_OF_CONSUMERS):
            customers.append(create_customer())

        for i in range(AMOUNT_OF_CONSUMERS):

            counter_of_begging = 0

            while True:
                is_little_food(COUNTER_OF_FOOD, food, cook)
                print(cook, "\n")

                print("К кассе подошёл " + str(customers[i]) + "\n")
                print("Что будете брать(Введите номер элемента):")
                for k in range(COUNTER_OF_FOOD):
                    print(k + 1, ")", food[k])

                print("\nУ вас осталось:", customers[i].money, "рублей.\n")

                num_of_dish = input_num()
                if check_element(num_of_dish):
                    continue

                if customers[i].money >= food[num_of_dish - 1].cost:
                    customers[i].buy_food(food[num_of_dish - 1], cook)
                    food.pop(num_of_dish - 1)
                elif counter_of_begging < 3:
                    print("Денег на еду не хватило, стоит попросить её у поварихи...(yes/no)")
                    if yes_or_no():
                        customers[i].free_food(food)
                        counter_of_begging += 1

                check(gov, cook, food)

                if change_of_turn(customers, i, counter_of_begging, cook):
                    break

            if cook.money < 0.25:
                break

        print("Очередь закончилась. Хотите начать еще один день?(yes/no)")
        if not answer.get(yes_or_no()):
            break


def check_element(num_of_dish):
    """Проверка на элемент в массиве"""
    if num_of_dish <= 0 or num_of_dish > 10:
        print("Введен неверный элемент меню!\n")
        return True
    else:
        return False


def input_num():
    """Ввод числа из меню"""
    while True:
        try:
            num_of_dish = int(input())
        except:
            print("Введена не цифра!")
        else:
            return num_of_dish


def change_of_turn(customers, i, counter_of_begging, cook):
    """Вероятность перехода очереди"""
    if customers[i].eat <= 0:
        print("Вы наелись.\n")
        return True
    elif customers[i].healthy == 0:
        print("Вы умерли от голода.\n")
        return True
    elif counter_of_begging == 3:
        print("Повариха выперла Вас из столовой.\n")
        return True
    elif cook.money < 0.25:
        print("Повариха обонкротилась.\n")
        return True


def yes_or_no():
    while True:
        yes_or_no = input().title()
        if yes_or_no == "Yes" or yes_or_no == "No":
            return yes_or_no
        else:
            print("Введен неверный пункт содержимиого меню!")


def check(gov, cook, food):
    """Производит провекру"""
    gov.take_money(cook)
    if choice([0, 0, 1, 0]):
        print("В столовую пришла проверка.\n")
        gov.sell_by_date(food, cook)
    print(gov)


def is_little_food(COUNTER_OF_FOOD, food, cook):
    """Дополняет список еды, если в нем меньше 10 элементов"""
    if len(food) < COUNTER_OF_FOOD:
        for i in range(COUNTER_OF_FOOD - len(food)):
            food.append(cook.create_food())
        return food


def create_goverment():
    """Создает объект правительсвто"""
    gov = g.Goverment(randint(1000, 10000))
    return gov


def create_customer():
    """Создает объект клиент"""
    n_c = c.Consumer()
    n_c.name = choice(["Alex", "Maksim", "Sergey", "Boris", "Nikita", "Vladimir", "Soveliy", "Stas"])
    n_c.surname = choice(["Godunov", "Pushkin", "Bagration", "Suhoi", "Tarashkevich", "Poznak", "Statkevich"])
    n_c.money = float(randint(2, 8))
    return n_c


def create_cook():
    """Создает объект повариха"""
    cook = c.Cook()
    cook.name = choice(["Галя", "Авдотья", "Валя", "Марфа"])
    cook.surname = choice(["Петровна", "Зарэченска", "Дорофеева", "Багинская"])
    cook.money = float(randint(70, 150))
    return cook


main()
