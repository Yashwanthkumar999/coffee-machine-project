from data import MENU, resources
global choice


def check_choice(choice):
    if choice == "espresso":
        print(f"{choice} cost is :$", MENU[choice]["cost"])

    elif choice == "latte":
        print(f"{choice} cost is :$", MENU[choice]["cost"])

    elif choice == "cappuccino":
        print(f"{choice} cost is :$", MENU[choice]["cost"])
