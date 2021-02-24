# <The Lewis and Clark Expedition>, <Ryan Kelley>, <10:49PM> <02/23/2021>, <Version 1.0.1>

# Player Variables 
starting_role = " "
money = 0 
score_bonus = 0 
player_name = " "
party_member0 = " "
party_member1 = " "
party_member2 = " "
party_member3 = " "

# Health Variables 
player_hp = 100
party_member0_hp = 100
party_member1_hp = 100
party_member2_hp = 100
party_member3_hp = 100
party_size = 5


# Inventory Variables 
amt_water = 0 
amt_food = 0
num_clothing = 0
num_guns = 0
num_bullets = 0
amt_rope = 0
num_horses = 0
num_boats = 0
num_wagons = 0
num_wagon_wheel = 0
num_wagon_axle = 0

# Cost Variables 
cost_water = 0.10 
cost_food = 0.25
cost_clothing = 1.25
cost_guns = 3.5
cost_bullets = 1.0
cost_rope = 0.5
cost_horses = 1.0
cost_boats = 5.0
cost_wagons = 10.0
cost_wagon_wheel = 1.50
cost_wagon_axle = 1.0

# Location Variables 
starting_point = "Name of starting location."
ending_point = "Where it ended."
location0 = "Fill in the Name"
location1 = "Fill in the Name"
location2 = "Fill in the Name"
location3 = "Fill in the Name"
current_location = starting_point 

# Disaster Variables 
chc_sick = 0.0
chc_break_wheel = 0.0
chc_break_axle = 0.0
chc_hostile_native = 0.0
chc_bad_weather = 0.0
chc_boat_sink = 0.0
chc_horse_fall = 0.0
chc_bandits = 0.0 

# Travel Variables 
num_days = 0 
dist_travel = 0 
travel_pace = 0 # Determine travel pace (slow, medium, fast). 
speed = 0 

# Main Menu Function 

def main_menu():
    global player_choice # The keyword global tells Python to save any changes to this variable for the whole program to access.  

    print("""
        +=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+
        *                        Ryan Kelley Game Studios                *
        *                               presents                         *
        *                     The Lewis and Clark Expedition             *
        *                                                                *
        *   1) Start the Expedition                                      *
        *   2) Learn more about the Expedition                           *
        *   3) High Scores                                               * 
        *   4) Exit Game                                                 *
        *                                                                *
        +=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-+
    \n""")

    player_choice = int(input("Please type a number from the menu and press enter.\n"))

    if player_choice == 1: 
        print("The adventure begins!  Good luck on your journey!\n")
    elif player_choice == 2: 
        print("Wise choice, it is important to know what you are facing on this expedition!\n")
    elif player_choice == 3:
        print("You want to see who has gone before you and done well?  Let's see those scores!\n")
    else: 
        print("I am sorry to see you go.  You would have made a brave explorer.\n")
        exit() 

# main_menu() # This is a FUNCTION CALL.  

# Display Information 

def display_info():
    import webbrowser
    
    print("""
    THIS PRINT STATEMENT SHOULD HAVE INFORMATION ABOUT THE GAME ITSELF. IT SHOULD BE ONE PARAGRAPH AT LEAST. 
    \n""")

    print("I can open a web browser and provide more historical information about this expedition if you want.\n")
    learn_more = input("Do you want me to open the browser for you? Please type yes or no.\n")

    if learn_more == "Yes" or learn_more == "yes" or learn_more == "y":
        webbrowser.open('https://kids.nationalgeographic.com/explore/history/lewis-and-clark/')
    else: 
        print("Perhaps another time.\n")

display_info() 

# Player Information 
def player_info():
    global money, score_bonus
    global player_name, party_member0, party_member1, party_member2, party_member3_hp

    player_name = input("What is your name?\n")
    print(f"Greetings {player_name}.  That is a fine name for someone so brave!\n")

    party_member0 = input("What is the name of the first person traveling with you?\n")
    party_member1 = input("What is the name of the second person traveling with you?\n")
    party_member2 = input("What is the name of the third person traveling with you?\n")
    party_member3 = input("What is the name of the fourth person traveling with you?\n")

    print(f"{player_name}, good luck.  The lives of {party_member0}, {party_member1}, {party_member2}, {party_member3} depend on your skill!\n ")