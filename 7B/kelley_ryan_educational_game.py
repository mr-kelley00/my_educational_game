# <The Lewis and Clark Expedition>, <Ryan Kelley>, <1:17PM> <12/09/20>, <Version 0.51>

# Player Variables
player_role = ""
starting_resources = 0
score_bonus = 0
player_name = ""
party_member0 = ""
party_member1 = ""
party_member2 = ""

# Inventory Variables
amt_food = 0
amt_water = 0
amt_clothing = 0
amt_wagons = 0 
amt_boats = 0
amt_horses = 0
num_guns = 0
num_bullets = 0
num_wagon_wheel = 0
num_wagon_axle = 0
num_boat_oar = 0
num_pelts = 0

# Cost Variables
cost_food = 0.20 # per pound. 
cost_water = 0.10 # per gallon
cost_clothing = 1.0 # per set
cost_wagons = 10.0 # each 
cost_boats = 20.0 # each 
cost_horses = 5.0 # each
cost_guns = 2.0 # each
cost_bullets = 1.25 # per box of 20.
cost_wagon_wheel = 2.50 # each
cost_wagon_axle = 3.50 # each...Lochness Monster! 
cost_boat_oar = 1.0 # each
cost_pelts = 0.75 # each
cost_mult = 1.0 

# Disaster Variables, as a percentage chance of happening. 
chnc_sick = 0.0
chnc_death = 0.0
chnc_bad_weather = 0.0
chnc_transport_accident = 0.0
chnc_native_attack = 0.0
chnc_bear_attack = 0.0
chnc_bandit_attack = 0.0
chnc_mutiny = 0.0
chnc_lost_path = 0.0

# Location Variables
starting_point = "St. Louis, Missouri"
end_point = "Fort Clatsop"
location0 = "St. Charles, Missouri"
loc0_dist = 0
location1 = "Missouri and Bad River Crossing"
loc1_dist = 0
location2 = "Lehmi Pass"
loc2_dist = 0
location3 = "Fort Mandan"
loc3_dist = 0
location4 = "Mount Hood" 
loc4_dist = 0 

# Main Menu Function
def main_menu():
    print("""
        [=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=]
        [                  Ryan Kelley Game Studios           ]
        [                          presents                   ]
        [                      Lewis and Clark                ]
        [                             in                      ]
        [                      ARE WE THERE YET?              ]
        [                                                     ]
        [    1.  Start the Journey                            ]
        [    2.  Learn More About the Expedition              ]
        [    3.  Check the High Scores                        ]
        [    4.  Exit the Game                                ]
        [=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=]
        """)
    global player_choice # global tells Python that the WHOLE PROGRAM can access this variable.
    player_choice = int(input("Please type your choice from the menu and press enter.\n"))
    # print(player_choice)
    if player_choice == 1:
        print("Brave! Let our journey begin.  Good luck!\n")
    elif player_choice == 2:
        print("Wise, you have decided to learn more about this journey.\n")
    elif player_choice == 3:
        print("Let us see who has gone before you and done well.\n")
    else:
        print("Not all of us are brave enough for this adventure.  Farewell!\n")
        exit()
    return player_choice

# main_menu() # This is known as CALLING the function.     

# Display Info. Function
def disp_info():
    print("""
        You need to write a PARAGRAPH in your OWN WORDS that provides information about your
        expedition.
        """)

# Player Info. Function
def player_info():
    player_name = input("Please give me your name brave adventurer.  What should I call you?\n")
    print(f"Wow!  I have never met anyone named {player_name}.  It's great to meet you!\n")
    # Next few lines of code will need to get the names of the other people in the party.
    party_member0 = input("You have another joining you.  What is their name?\n")
    party_member1 = input("I see you have a third member of the party.  What should I call them?\n")
    party_member2 = input("Four people will be with you?  By what name are they known?\n")
    print(f"{player_name} will joined by {party_member0}, {party_member1}, and {party_member2}.\n")
    print("""
Lewis and Clark had many skilled explorers and craftsmen on their journey west.  Each job
played an important role for the group.  One of the most important jobs for this expedition was
that of interpreter or translator to communicate with the native tribes encountered.  The role
of cook was also extremely important.  A well fed expedition will stay healthy and be able to
make the journey in a shorter period of time.  Finally, one of the other job roles that was quite
important was that of a trapper.  Lewis and Clark knew they would be able to eat the meat from
each animal but could also trade the pelts along the way for important supplies.

Which job would you like to pick?
    -- Translator
    -- Cook
    -- Trapper
    """)
    player_role = input("Please type a job name and press enter.\n")
    if player_role == "Translator" or player_role == "translator" or player_role == "TRANSLATOR": 
        print("You have selected translator.\n")
    elif player_role == "Cook" or player_role == "cook" or player_role == "COOK":
        print("You have selected cook.\n")
    elif player_role == "Trapper" or player_role == "trapper" or player_role == "TRAPPER":
        print("You have selected trapper.\n")
    else: 
    
player_info() 
