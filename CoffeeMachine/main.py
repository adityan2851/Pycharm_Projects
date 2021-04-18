MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def call(cost, w, c, m):
    print(f"Its Cost {cost}$")
    quarters = int(input("Enter the quarters")) * 0.25
    dimes = int(input("Enter the dimes")) * 0.10
    nickles = int(input("Enter the nickles")) * 0.05
    pennies = int(input("Enter the pennies")) * 0.01
    total = quarters + dimes + nickles + pennies
    if total >= cost:
        if total - cost != 0:
            change = total - cost
            print(f"Thanks, Here is the change ", {change})
        if resources["water"] >= w and resources["coffee"] >= c and resources["milk"] >= m:
            resources["water"] -= w
            resources["coffee"] -= c
            resources["milk"] -= m
        else:
            print("Sorry, resources didn't enough to make")
    else:
        print("Not Enough Credits, Money Refunded")


while True:
    drink = input("What would you like?(espresso/latte/cappuccino) ")
    if drink == "off":
        break
    if drink == "latte":
        call(2.5, 200, 24, 150)
        print("Here is your latte, Enjoy!")
    if drink == "cappuccino":
        call(2, 250, 24, 100)
        print("Here is your latte, Enjoy!")
    if drink == "espresso":
        call(1, 50, 18, 0)
        print("Here is your latte, Enjoy!")
    print("Water:", resources["water"])
    print("Milk:", resources["milk"])
    print("Coffee:", resources["coffee"])
