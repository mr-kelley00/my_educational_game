# <Educational Game>, <Ryan Kelley>, <2:35PM> <12/01/20>, <Version 0.3>

# Player Variables
player_name = ""
party_member0 = ""
party_member1 = ""
party_member2 = ""
party_member3 = ""
starting_role = ""
score_bonus = 0

# Inventory Variables
amt_food = 0
amt_water = 0
num_wagons = 0
num_boats = 0
num_guns = 0
num_bullets = 0
num_horses = 0
num_wagon_wheel = 0
num_wagon_axle = 0
num_pelts = 0
num_beads = 0
num_traps = 0
money = 0 

# Main Menu
def main_menu():
    print("+=====++=====++=====++=====++=====++=====++=====++=====++=====+")
    print("+                          Ryan Kelley Games                  +")
    print("+                                presents                     +")
    print("+                           Lewis and Clark                   +")
    print("+                                 in                          +")
    print("+                        \"WHERE THE HECK ARE WE?\"             +")
    print("+                                                             +")
    print("+    Please choose an option from the menu.                   +")
    print("+    1. Begin your journey.                                   +")
    print("+    2. Learn more about the journey.                         +")
    print("+    3. See the high scores.                                  +")
    print("+    4. Enable / Disable Sound                                +")
    print("+    5. Exit Game                                             +")
    print("+                                                             +")
    print("+=====++=====++=====++=====++=====++=====++=====++=====++=====+")
    player_choice = int(input("Please type your choice and press enter.  \n"))
    if player_choice == 1:
        do_this
    elif player_choice == 2:
        do_that
    elif player_choice == 3:
        do_this_other_thing
    elif player_choice == 4:
        do_something_else
    else:
        exit() 

main_menu()
    
    
