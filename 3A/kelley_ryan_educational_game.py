# <Lewis and Clark Expedition Extravaganza>, <Ryan Kelley>, <12/08/20> <1:10PM>, <Version 0.47>

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
amount_food = 0
amount_water = 0
num_wagons = 0
num_horses = 0
num_wagon_wheel = 0
num_wagon_axle = 0
num_clothing = 0
num_pelts = 0
num_traps = 0 

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
    
player_info()

