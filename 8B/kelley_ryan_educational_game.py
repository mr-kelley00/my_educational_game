# <Educational Game>, <Ryan Kelley>, <1:46PM> <12/03/20>, <Version 0.4>

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

# Disaster Variables, % chance of occurrence.
player_sick = 0.0
player_death = 0.0
party_sick = 0.0
party_death = 0.0
bad_weather = 0.0
got_lost = 0.0
wagon_wheel_break = 0.0
wagon_axle_break = 0.0
hostile_natives = 0.0
animal_attack = 0.0 


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
    print("+    4. Exit Game                                             +")
    print("+                                                             +")
    print("+=====++=====++=====++=====++=====++=====++=====++=====++=====+")
    player_choice = int(input("Please type your choice and press enter.  \n"))
    if player_choice == 1:
        print("Ah, brave adventurer!  Good luck on your journey.  Be safe!\n")
    elif player_choice == 2:
        print("Wise choice.  Let us learn more before we depart.\n")
    elif player_choice == 3:
        print("Care to see who has done well before you I see...\n")
    else:
        print("Not all are brave enough for this task.  Farewell!\n") 
        exit() 
    return player_choice

# main_menu()
    
    
