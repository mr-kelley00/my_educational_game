# <The Lewis and Clark Expedition>, <Ryan Kelley>, <12:39PM> <01/11/21>, <Version 1.0.0>

# Player Variables
player_role = ""
money = 0
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
    # Declare these variables as global so they are saved for the whole program.
    global player_name
    global party_member0
    global party_member1
    global party_member2
    global player_role
    global money
    global score_bonus
    
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
        money = 1000
        score_bonus = 0.5
        player_role = 0
    elif player_role == "Cook" or player_role == "cook" or player_role == "COOK":
        print("You have selected cook.\n")
        money = 750
        score_bonus = 1.0
        player_role = 1
    elif player_role == "Trapper" or player_role == "trapper" or player_role == "TRAPPER":
        print("You have selected trapper.\n")
        money = 500
        score_bonus = 1.5
        player_role = 2
    else:
        print("You will just be a pot scrubber.\n")
        money = 250
        score_bonus = 2.0
        player_role = 3
    print(f"You will have {money} dollars and receive a {score_bonus} score multiplier.\n")
    return player_name, party_member0, party_member1, party_member2, money, score_bonus

player_info() 

# Buying and Selling Items
def show_inventory():
    print(f"""
{player_name}, this is what you have in your inventory right now:
    {amt_food} pounds of food remain in your stores.
    {amt_water} gallons of fresh water remaining.  
    {amt_clothing} sets of clothing remain for you and your party. 
    {amt_wagons} wagons are still operational.  
    {amt_boats} boats are safe for travel.
    {amt_horses} horses fit and healthy to ride.
    {num_guns} guns available for defense and hunting.
    {num_bullets} bullets still remain in our ammo locker.
    {num_wagon_wheel} wheels left in case of emergency repairs.
    {num_wagon_axle} axles are in good working order.
    {num_boat_oar} oars still exist in our supplies.
    {num_pelts} animal pelts are available for trade. 
    \n
    """)

show_inventory()

# Trading Functions

def buy_item():
    # check player money balance
    # what is for sale?
    # how much is it?
    # how many are available?
    # pay for it.  (player_money - cost)
    # add the items to the player inventory
    # remove from vendor inventory (optional, bonus points if you can make it work.)

    global money
    global amt_food 
    global amt_water
    global amt_clothing
    global amt_wagons 
    global amt_boats 
    global amt_horses 
    global num_guns 
    global num_bullets
    global num_wagon_wheel 
    global num_wagon_axle 
    global num_boat_oar 
    global num_pelts 
    

def sell_item(): 
    # check vendor balance
    # what does the player have to sell? is it worth anything?
    # what value does the item have?
    # how many to buy from player?
    # pay player (player_money += item_value)
    # remove from player inventory
    # (optional) add to vendor inventory 

    
