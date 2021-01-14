# <Lewis and Clark Expedition Extravaganza>, <Ryan Kelley>, <01/14/21> <12:25PM>, <Version 1.0.0>

# Player Variables 
player_score = 0
player_name = ""
party_member0 = ""
party_member1 = ""
party_member2 = ""
party_member3 = ""
player_job = ""
money = 0

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

# disp_info()           

# Player Info. Function
def player_info():

    global player_name
    global party_member0
    global party_member1
    global party_member2
    global party_member3
    
    player_name = input("Greetings brave traveler!  What should I call you?\n")
    party_member0 = input("I see you have a second person with you.  What is their name?\n")
    party_member1 = input("You have a third?  By what name are they known?\n")
    party_member2 = input("Four people makes quite the crowd. Do they have a name?\n")
    party_member3 = input("Now five of you?  Any more will be too many.  What do I call them?\n")
    print(f"{player_name}, you are a brave leader.  Good luck to you and {party_member0}, {party_member1}, {party_member2}, and {party_member3}.\n")
    print("""
The Lewis and Clark expedition had many important job roles.  Each person had to do their share
to ensure that the trip went safely.  One of the most important roles was that of translator.  Lewis
and Clark would encounter many native tribes along the journey, communicating with them was extremely
important. The trappers that accompanied Lewis and Clark were able to provide food and pelts, both of
which could be used as valuable trade items with the tribes.  Finally, the cooks were also important
members of the group.  Keeping the expedition well fed meant better health for everyone.

What job would you like?
-- Translator
-- Trapper
-- Cook

    """)
    global player_job
    player_job = input("Please type the name of the job and press enter.\n")
    global score_bonus
    
    if player_job == "translator" or player_job == "Translator" or player_job == "TRANSLATOR":
        print("You have chosen to be a translator.\n")
        score_bonus = 1
        money = 1000
    elif player_job == "trapper" or player_job == "Trapper" or player_job == "TRAPPER":
        print("You have chosen to be a trapper.\n")
        score_bonus = 2
        money = 750
    else:
        print("You have chosen to be a cook.\n")
        score_bonus = 3
        money = 500
    print(f"You will start with a score bonus of {score_bonus} and ${money} dollars.\n") 
    
    
player_info()


# Trading Transactions

def buy_item():
    # figure out player money
    # cost of the items
    # menu of items
    # total cost = number of items * cost of item
    # pay for item (subtract total cost from player balance)
    # add the item to player inventory
    
    global num_boats 
    global num_guns 
    global num_bullets 
    global num_food 
    global num_water 
    global num_horses 
    global num_wagon_wheel 
    global num_wagon_axle 
    global num_pelts 
    global num_traps 
    
    
    
