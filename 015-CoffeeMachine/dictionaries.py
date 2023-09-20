from decimal import Decimal

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
    "water": 500,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

coins = {
    "nickel": Decimal("0.05"),
    "dime": Decimal("0.10"),
    "quarter": Decimal("0.25"),
}