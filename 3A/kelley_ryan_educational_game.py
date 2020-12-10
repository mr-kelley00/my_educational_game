# <Lewis and Clark Expedition Extravaganza>, <Ryan Kelley>, <12/10/20> <1:02PM>, <Version 0.49>

# Player Variables 
player_score = 0
player_name = ""
party_member0 = ""
party_member1 = ""
party_member2 = ""
party_member3 = ""
player_job = ""
start_money = 0

# Inventory Variables 
num_boats = 0
num_guns = 0
num_bullets = 0
num_food = 0
num_water = 0
num_wagons = 0
num_horses = 0
num_wagon_wheel = 0
num_wagon_axle = 0
num_clothing = 0
num_pelts = 0
num_traps = 0

# Cost Variables 
cost_boats = 20.0 # Price per boat. 
cost_guns = 5.0 # price per gun. 
cost_bullets = 2.50 # Box of 50. 
cost_food = 0.25 # per pound.
cost_water = 0.10 # per gallon.
cost_wagons = 10.0 # per wagon.
cost_horses = 5.0 # per pair. 
cost_wagon_wheel = 3.50 # each
cost_wagon_axle = 3.50 # each 
cost_clothing = 1.0 # per set
cost_pelts = 2.0 # each 
cost_traps = 1.0 # each

# Location Variables
starting_point = "St. Louis, Missouri"
ending_point = "Fort Calstop" 
location0 = " "
location1 = " "
location2= " "

# Time / Date / Distance Variables 
game_time = 0
game_date = 0
landmark_distance = 0
total_distance = 0 

# Disaster Variables
chnc_sick = 0.0
chnc_die = 0.0
chnc_wheel_break = 0.0
chnc_axle_break = 0.0
chnc_bad_weather = 0.0


# Main Menu
def main_menu():
    print("++==++==++==++==++==++==++==++==++==++==++==++==++==++==++==++==++")
    print("|                      The Lewis and Clark Expedition            |")
    print("|                                 by                             |")
    print("|                        Ryan Kelley Game Studios                |")
    print("|                                                                |")
    print("|   1) Begin Your Journey                                        |")
    print("|   2) Learn More about the Lewis and Clark Expedition           |")
    print("|   3) See the High Scores                                       |")
    print("|   4) Exit Game                                                 |")
    print("|                                                                |")
    print("++==++==++==++==++==++==++==++==++==++==++==++==++==++==++==++==++")
    global player_choice
    player_choice = int(input("Please type a number from the menu and press enter.\n"))
    # print(player_choice)
    if player_choice == 1:
        print("Good luck brave explorer.  Farewell on your journey!\n")
    elif player_choice == 2:
        print("You have decided to study more before adventuring.  Wise choice.\n")
    elif player_choice == 3:
        print("Let us see who has gone before you and done well!\n")
    else:
        print("Not all are brave enough to take this journey.  Perhaps another time?\n")
        exit()
    return player_choice  
    
# main_menu()

# Display Info.
def disp_info():
    print("Make this function print historical information about the journey.\n")
    print("Also make it print some tips and tricks to help the player in the game.\n")
    print("For example, with Oregon trail this part of the game explained the best time to leave.\n")

disp_info()           

# Player Info. Function
def player_info():
    player_name = input("Greetings brave traveler!  What should I call you?\n")
    party_member0 = input("I see you have a second person with you.  What is their name?\n")
    party_member1 = input("You have a third?  By what name are they known?\n")
    party_member2 = input("Four people makes quite the crowd. Do they have a name?\n")
    party_member3 = input("Now five of you?  Any more will be too many.  What do I call them?\n")
    print(f"{player_name}, you are a brave leader.  Good luck to you and {party_member0}, {party_member1}, {party_member2}, and {party_member3}.\n")
    print("""
Type your job role information here. 


    """)
player_info()

