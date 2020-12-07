# <Educational Game>, <Ryan Kelley>, <12:44PM> <12/03/20>, <Version 0.47>

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
    
    
player_info() 
