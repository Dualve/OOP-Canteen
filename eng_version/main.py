#Lab №13(Python and OOP. Classes design and implementation. Creation and manipulation objects)

#CANTEEN
#Created by Dubodelov A.V. and Lebed A.S.
#Version: 1.5
#Group: 10701118
#Date: 10.03.2019


import random

from cook import Cook
from food import Food
from customer import Customer
from government import Government
from messages import *

def input_num():
    while True:
        try:
            num = int(input())
        except:
            print("Error!")
        else:
            return num


def check_element(num_of_dish):
    if num_of_dish <= 0 or num_of_dish > AMOUNT_OF_DISHES:
        print("You have entered the invalid element!")
        return True
    else:
        return False


def print_menu(food):
    print("\t\tOur menu:\n")
    for j in range(AMOUNT_OF_DISHES):
        print(str(j + 1) + ")" + str(food[j]))
    print("\n")


def sell_food(food, food_choice, customer, cook):
    customer.buy_food(food[food_choice - 1])
    cook.add_money(food[food_choice - 1].cost)
    food.pop(food_choice - 1)
    food.append(cook.cook_food())
    print("\n")


def panhandle_action(panhandle_counter, customer, food):
    print(PANHANDLE_TIMES_MESSAGES)
    while (customer.calorie_requirement > 0 and panhandle_counter < MAX_TIMES_OF_PANHANDLE):
        print(
            "Press any key to panhandle! " + str(MAX_TIMES_OF_PANHANDLE - panhandle_counter) + " times are available!")
        input()
        customer.panhandle(food)
        panhandle_counter += 1


def main():

    # creation variables
    cook = Cook(COOK_SURNAME, COOK_NAME)
    government = Government()
    food = []
    panhandle_counter = 0

    # greeting
    print(GREETING_MESSAGE + cook.surname + " " + cook.name + "\n")

    # cooking food
    for i in range(AMOUNT_OF_DISHES):
        food.append(cook.cook_food())
    # the main action
    for i in range(AMOUNT_OF_CUSTOMERS):
        customer = Customer(random.choice(CUSTOMERS_SURNAMES), random.choice(CUSTOMERS_NAMES))
        print(str(customer) + "\n")


        while(customer.calorie_requirement > 0):

            print_menu(food)

            print(PURCHASE_CHOICE_MESSAGE)
            food_choice = input_num()
            if (check_element(food_choice)):
                continue

            if(customer.money >= food[food_choice - 1].cost):
                sell_food(food, food_choice, customer, cook)
                if(customer.health == 0):
                    customer.die()
                    break
            else:
                print(NOT_ENOUGH_MONEY)
                no_money_choice = input_num()
                if(no_money_choice == 1):
                    continue
                elif(no_money_choice == 21):
                    panhandle_action(panhandle_counter, customer, food)
                    if customer.health == 0 or customer.calorie_requirement > 0:
                        customer.die()
                        break
                else:
                    print("You have entered the invalid element!")
                    continue

        if not (customer.health == 0):
            print(THANKS_MESSAGE)

        if random.randint(1, 3) == 1:
            amount_of_seized = government.check_canteen(food, cook)
            if (amount_of_seized > 0):
                for i in range(amount_of_seized):
                    food.append(cook.cook_food())
            if cook.isBankrupt():
                break
    print("Amount of created food: " + str(Food.counter_food()))


if __name__ == "__main__":
    main()
