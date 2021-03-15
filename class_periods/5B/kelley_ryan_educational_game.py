# <The Lewis and Clark Expedition Simulator>, <Ryan Kelley>, <8:55AM> <03/15/21>, <Version 1.5.0>

# Player Variables
starting_role = ""
money = 0
score_bonus = 0
player_name = ""
party_member0 = ""
party_member1 = ""
party_member2 = ""
party_member3 = ""

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
num_rope = 0
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
cost_multi = 1.0 

# Location Variables
starting_point = "St. Louis, Missouri"
ending_point = "Fort Calstop"
location0 =  "Test 0"
location1 =  "Test 1"
location2 =  "Test 2"
location3 =  "Test 3"
current_location = starting_point

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
        
# Display Info Function
def disp_info():
    print("""
        Update to actual paragraph of historical facts and game play tips.
        """)

# disp_info() 

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
        money = 500
        score_bonus = 3.0
    elif starting_role == "Trapper" or starting_role == "trapper" or starting_role == "TRAPPER":
        print("You have chosen the role of trapper.\n")
        money = 750
        score_bonus = 2.0
    elif starting_role == "Interpreter" or starting_role == "interpreter" or starting_role == "INTERPRETER":
        print("You have chosen the role of interpreter.\n")
        money = 1000
        score_bonus = 1.0
    else:
        print("You did not pick a role correctly.  You wil be washing pots and pans.\n")
        money = 250
        score_bonus = 0.5 
    print(f"You will start with ${money} dollars and a {score_bonus} score multiplier.\n")     
  
# Display Map
def display_map():
    from PIL import Image
    # Select map based on location of player. 
    if current_location == "St. Louis, Missouri":
        current_map = Image.open("gfx/maps/world_map.png")
    elif current_location == "Test 0":
        current_map = Image.open("gfx/maps/world_map0.png")
    elif current_location == "Test 1":
        current_map = Image.open("gfx/maps/world_map1.png")
    elif current_location == "Test 2":
        current_map = Image.open("gfx/maps/world_map2.png")
    else:
        current_map = Image.open("gfx/maps/world_map3.png")
    
    current_map.show()
    # Need to update code to display map based on current location.  

# Calculate Final Score 
def calc_score(): 

    final_score = (party_size * 250) + (money * 50) + (amt_water * 0.5) + (amt_food * 0.5) + (num_clothing * 1.0)  
    final_score += (num_guns * 2.0) + (num_bullets * 0.25) + (num_rope * 1.0) + (num_horses * 5.0) + (num_boats * 25.0)  
    final_score += (num_wagons * 10.0) + (num_wagon_wheel * 2.5) + (num_wagon_axle * 2.5)
    final_score = final_score * score_bonus # Multiply final_score by the score_bonus.  

    print(final_score)

