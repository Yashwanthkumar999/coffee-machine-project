from data import resources,MENU
def modify_values(choice):

     choice1= choice
     resources["water"] -=int(MENU[choice1]["ingredients"]["water"])
     resources["milk"]  -=int(MENU[choice1]["ingredients"]["milk"])
     resources["coffee"] -=int(MENU[choice1]["ingredients"]["coffee"])

