# <The Lewis and Clark Expedition Simulator>, <Ryan Kelley>, <9:23AM> <01/05/21>, <Version 0.60>

# Player Variables
starting_role = ""
starting_money = 0
score_bonus = 0
player_name = ""
party_member0 = ""
party_member1 = ""
party_member2 = ""
party_member3 = ""

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

# Inventory Costs
cost_water = 0.10 
cost_food = 0.25
cost_clothing = 1.25
cost_guns = 3.50
cost_bullets = 1.0
cost_rope = 0.5
cost_horses = 1.0
cost_boats = 5.0
cost_wagons = 10.0
cost_wagon_wheel = 1.50
cost_wagon_axle = 1.50

# Location Variables
starting_point = "St. Louis, Missouri"
ending_point = "Fort Calstop"
location0 =  " "
location1 =  " "
location2 =  " "
location3 =  " "

# Disaster Variables, % chance it occurs.  
chc_sick = 0.0
chc_break_wheel = 0.0
chc_break_axle = 0.0
chc_hostile_native = 0.0
chc_bad_weather = 0.0
chc_boat_sink = 0.0
chc_horse_fall = 0.0

# Main Menu Function

def main_menu():
    print("""
        +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
        *                        Ryan Kelley Game Studios           *
        *                               presents                    *
        *                           Lewis and Clark                 *
        *                                 in                        *
        *                           Are We There Yet?!              *
        *                                                           *
        *   1. Start your journey.                                  *
        *   2. Learn more about the expedition.                     *
        *   3. See the high scores.                                 *
        *   4. Exit game.                                           *
        *                                                           *
        +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
        """)
    global player_choice
    player_choice = int(input("Please type a number from the menu and press enter.\n"))
    # print(player_choice)
    if player_choice == 1:
        print("The adventure awaits!  Let's get going...\n")
    elif player_choice == 2:
        print("Wise choice, let us learn more before we go.\n")
    elif player_choice == 3:
        print("Want to see who were the greatest explorers before you eh?\n")
    else:
        print("Ahh, no heart for adventure today I see.  Farewell, until next time.\n")
        exit()
# main_menu()
# print(player_choice)
        
# Display Info Function
def disp_info():
    print("""
        Update to actual paragraph of historical facts and game play tips.
        """)
# disp_info() 

# High Scores
# def high_scores():
# Read high_scores save file.
# print high scores to the screen.
# exit after printing high scores.

def player_info():
    player_name = input("What is your name brave explorer?\n")
    print(f"Greetings {player_name}.  That is a fine name for a brave explorer such as yourself!\n")
    party_member0 = input("I see another soul is joining you.  What should I call them?\n")
    party_member1 = input("You have a third person in the group. What is their name?\n")
    party_member2 = input("Four people so far, eh?! By what name are they known?\n")
    party_member3 = input("Ok, last but not least, what name does the last person go by?\n")
    print(f"{player_name}, you will be joined by {party_member0}, {party_member1}, {party_member2}, and {party_member3}.\n")
    print("Good luck.  It is a dangerous world to explore.\n")
    # The next lines of code should allow the player to choose a starting job role.
    print(f"""
        For this journey, Lewis and Clark will need people with different skills and experience. {player_name}, you will need to
        choose one of these roles.  They are as follows:
        
        -- Cook
        -- Trapper
        -- Interpreter
        
        Each role brings certain benefits and drawbacks to the journey.  Choose carefully.\n
        """) 
    starting_role = input("Which job role do you want?\n")
    if starting_role == "Cook" or starting_role == "cook" or starting_role == "COOK":
        print("You have chosen the role of cook.\n")
        starting_money = 500
        score_bonus = 3.0
    elif starting_role == "Trapper" or starting_role == "trapper" or starting_role == "TRAPPER":
        print("You have chosen the role of trapper.\n")
        starting_money = 750
        score_bonus = 2.0
    elif starting_role == "Interpreter" or starting_role == "interpreter" or starting_role == "INTERPRETER":
        print("You have chosen the role of interpreter.\n")
        starting_money = 1000
        score_bonus = 1.0
    else:
        print("You did not pick a role correctly.  You wil be washing pots and pans.\n")
        starting_money = 250
        score_bonus = 0.5 
    print(f"You will start with ${starting_money} dollars and a {score_bonus} score multiplier.\n")     
   
# player_info() 

def show_inventory():
    print(f"""
    {amt_water} gallons of water remain.
    {amt_food} pounds of food are safe to eat.
    {num_clothing} sets of clothing are clean.
    {num_guns} guns are operational.
    {num_bullets} bullets are available to the expedition. 
    {amt_rope} feet of rope are safe and secure.
    {num_horses} healthy horses are at our service.
    {num_boats} boats float safely for river crossings.
    {num_wagons} working wagons are ready for transport.
    {num_wagon_wheel} wagon wheels can be used for repairs.
    {num_wagon_axle} wagon axles are sturdy enough for use. 
    \n
    """)

show_inventory()
