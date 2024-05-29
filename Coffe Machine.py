MENU = {
    "espresso": {

        "water": 50,
        "coffee": 18,
        "cost": 1.5,
    },
    "latte": {
        "water": 200,
        "milk": 150,
        "coffee": 24,
        "cost": 2.5,
    },
    "cappuccino": {
        "water": 250,
        "milk": 100,
        "coffee": 24,
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def want_another():
    want = input("Do you want another coffe?Y or N").lower()
    if want == "y":
        return True
    else:
        print("Have a great day!")
        return False


def is_giving_money(order):
    print(f'Insert {MENU[order]["cost"]}')
    to_pay = MENU[order]["cost"]
    zece = int(input("Cate de 10 bani?"))
    cinze = int(input("Cate de 50 de bani?"))
    leu = int(input("Cate de un leu?"))
    paid = float((zece * 10 + cinze * 50 + leu * 100)/100)
    if paid >= to_pay:
        resources["money"] += paid
        return True
    else:
        return False

def has_resource(resource,product):
    if resources[resource] < MENU[product][resource]:
        return False
    else:
        return True


def is_working():
    print("\n \n \n \n \n \n \n \n \n \n \n \n \n")
    order = input("Hai la cafea!(espresso/latte/cappuccino)\nAPARATUL NU DA REST \n").lower()
    if order == "espresso":
        if has_resource("water",order):
            if has_resource("coffee",order):
                if is_giving_money(order) == True:
                    resources["water"] -= MENU[order]["water"]
                    resources["coffee"] -= MENU[order]["coffee"]
                    print(f"Here is your {order}")
                    if want_another():
                        is_working()
                else:
                    print("You dont have enough money.")
            else:
                print("Not enough coffee.")
        else:
            print("Not enough water.")

    elif order == "latte":
        if has_resource("water",order):
            if has_resource("coffee",order):
                if has_resource("milk",order):
                    if is_giving_money(order) == True:
                        resources["water"] -= MENU[order]["water"]
                        resources["coffee"] -= MENU[order]["coffee"]
                        print(f"Here is your {order}")
                        if want_another():
                            is_working()
                    else:
                        print("You dont have enough money.")
                else:
                    print("Not enough milk")
            else:
                print("Not enough coffee.")
        else:
            print("Not enough water.")

    elif order == "cappuccino":
        if has_resource("water",order):
            if has_resource("coffee",order):
                if has_resource("milk",order):
                    if is_giving_money(order) == True:
                        resources["water"] -= MENU[order]["water"]
                        resources["coffee"] -= MENU[order]["coffee"]
                        print(f"Here is your {order}")
                        if want_another():
                            is_working()
                    else:
                        print("You dont have enough money.")
                else:
                    print("Not enough milk")
            else:
                print("Not enough coffee.")
        else:
            print("Not enough water.")

    elif order == "report":
        for key in resources:
            print(f"{key} : {resources[key]}")
        if want_another():
            is_working()

    else:  
        print("Invalid Selection")
        is_working()



is_working()