from data import MENU,resources
from modify import modify_values
from check_choice import check_choice
from time import sleep
from art import logo
verify_status = ""

def cont():
    global verify_status
    # This will check whether the user want to continue
    x = input("do you want to continue 'yes' or 'no':").lower()
    if x == "yes":
        verify_status = ""
        coffee()
    elif x == "no":
        print("Thank you ✌✌")



def check_money(choice):
    global verify_status

    def verify():
        global verify_status
        miss = ""
        for key in resources:

            if int(resources[key]) < int(MENU[choice]["ingredients"][key]):
                miss=key
        if miss != "":
            sleep(2)
            print(f"'sorry ☹' {miss} is insufficient to make {choice}.")
            print("TRY TO CHOOSE ANOTHER DRINK TYPE")
            sleep(1)
            cont()
        else:
            verify_status="ok"


    verify()
    def money(choice):
        money = float((input("please insert the money : $")))
        if money < float(MENU[choice]["cost"]):
            print("Money is insufficient \n collect your money back and try again with sufficient amount.")
            cont()
        elif money > float(MENU[choice]["cost"]):
            change = round(money - float(MENU[choice]["cost"]), 2)
            print(f"Please collect your change : ${change} \n Your coffee is getting prepared, please wait a moment ")
            sleep(3)
            print("Here you go ! 'enjoy your coffee ☕'")
            sleep(2)
            modify_values(choice)
            cont()
        elif money == float(MENU[choice]["cost"]):
            print(" Your coffee is getting prepared, please wait a moment ")
            print("Here you go ! 'Enjoy your coffee ☕'")
            sleep(2)
            modify_values(choice)
            cont()

    if verify_status == "ok":
        money(choice)
        verify_status = ""
# this coffee function will will be the user interface
# In this
def coffee():
    sleep(1)


    choice = input("Enter your desired drink type 'Espresso' or 'Latte' or 'Cappuccino' OR\n"
                   "type 'report' to know about available resources :").lower()

    check_choice(choice)

    if choice == "report":
        print(resources)
        cont()

    else:
        check_money(choice)


print(logo)
print("welcome to COFFEE ZONE")

coffee()



