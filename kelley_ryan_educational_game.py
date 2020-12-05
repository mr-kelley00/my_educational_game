# <The Lewis and Clark Expedition>, <Ryan Kelley>, <2:41PM> <12/04/20>, <Version 0.51>

# Global Variables

# Player Variables
occupation = ""
start_money = 0
score_bonus = 0
player_name = ""
party_member0 = ""
party_member1 = ""
party_member2 = ""
party_member3 = ""

# Supply Variables
amount_food = 0
amount_water = 0
num_boats = 0
num_guns = 0
num_bullets = 0
num_swords = 0
num_axes = 0
num_horses = 0
num_wagons = 0
num_clothing = 0
num_cows = 0
num_chickens = 0
num_pigs = 0 


# Disaster Variables
chnc_sick = 0.0
chnc_die = 0.0
chnc_injury = 0.0
chnc_hostile_natives = 0.0
chnc_wagon_accident = 0.0
chnc_bear_attack = 0.0 

# main menu function
def main_menu():
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("*                            Lewis and Clark                        *")
    print("*                                  in                               *")
    print("*                   The Western Exploration Extravaganza            *")
    print("*                                  by                               *")
    print("*                             Ryan Kelley                           *")
    print("*                                                                   *")
    print("*                                                                   *")
    print("*    1. Start the Game                                              *")
    print("*    2. Learn more about the Lewis and Clark Expedition             *")
    print("*    3. See High Scores                                             *")
    print("*    4. Exit Game                                                   *")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    global player_choice
    player_choice = int(input("Please type a number and press enter.\n"))
    if player_choice == 1:
        print("Ok, let the journey begin.\n")
    elif player_choice == 2:
        print("Ok, let me tell you a story about Lewis and Clark.\n")
    elif player_choice == 3:
        print("Let's find out who the best explorers have been.\n")
    else:
        print("Sorry to see you go.")
        exit() 
    return player_choice

# Display info about the expedition.  
def disp_info():
    print("""
        Write at least ONE PARAGRAPH of FACTUAL INFORMATION ABOUT YOUR EXPEDITION.\n
        """)

# Player Info Function
def player_info():
    player_name = input("What should I call you?\n")
    print(f"{player_name} is a mighty fine name.  What about the other people in your group?\n")
    party_member0 = input("Who else is traveling with you?\n")
    party_member1 = input("I see you have someone else with you.  What is their name?\n")
    party_member2 = input("A third person is joining?  What do I call them?\n")
    party_member3 = input("Last but not least, who is the fourth person in your group?\n")
    print(f"Ok {player_name}.  I hope that {party_member0}, {party_member1}, {party_member2}, and {party_member3} all arrive safely.\n")
    print(f"""On the Lewis and Clark journey the following jobs were important: scout, cook, and trapper.
    Which job would you like to choose?
    1) Scout
    2) Cook
    3) Trapper
    """)
    
player_info()           
    
    






