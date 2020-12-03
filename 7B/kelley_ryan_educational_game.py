# <Educational Game>, <Ryan Kelley>, <12:47PM> <12/03/20>, <Version 0.35>

# Player Variables
player_role = ""
starting_resources = 0
score_bonus = 0
player_name = ""
party_member0 = ""
party_member1 = ""
party_member2 = ""
party_member3 = ""
party_member4 = ""

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
        [                                                     ]
        [                                                     ]
        [=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=]
        """)

main_menu() # This is known as CALLING the function.     


