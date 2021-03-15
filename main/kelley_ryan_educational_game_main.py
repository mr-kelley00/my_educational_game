# <The Lewis and Clark Expedition Simulator>, <Ryan Kelley>, <12:52AM> <03/10/21>, <Version 1.6.0a>

# Inventory Amounts
amt_water = 0
amt_food = 0
num_clothing = 0 
num_guns = 0
num_bullets = 0
amt_rope = 0
num_horses = 0
num_boats = 0
num_wagons = 0
num_wheels = 0
num_axles = 0

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

# Player Variables
player_choice = ""
starting_role = ""
money = 0
score_bonus = 0
player_name = ""
player_hp = 100
party_size = 5 # Total number of people in the party to start. 

# Party Member Variables 
party_member0 = ""
party_member0_hp = 100
party_member1 = ""
party_member1_hp = 100
party_member2 = ""
party_member2_hp = 100
party_member3 = ""
party_member3_hp = 100

# Location Variables 
starting_point = "St. Louis, Missouri"
ending_point = "Fort Calstop"
location0 =  "Test 0"
location1 =  "Test 1"
location2 =  "Test 2"
location3 =  "Test 3"
current_location = starting_point

# Travel Variables 
num_days = 0
dist_travel = 0 
travel_pace = 0 
speed = 0
resource_consume = 0

# Disaster Variables, % chance it occurs.  
chc_sick = 0.0
chc_break_wheel = 0.0
chc_break_axle = 0.0
chc_hostile_native = 0.0
chc_bad_weather = 0.0
chc_boat_sink = 0.0
chc_horse_fall = 0.0

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# MAIN MENU -- FUNCTIONAL
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def main_menu():
    global player_choice
    
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
    
    player_choice = int(input("Please type a number from the menu and press enter.\n"))
   
    if player_choice == 1:
        print("The adventure awaits!  Let's get going...\n")
    elif player_choice == 2:
        print("Wise choice, let us learn more before we go.\n")
    elif player_choice == 3:
        print("Want to see who were the greatest explorers before you eh?\n")
    else:
        print("Ahh, no heart for adventure today I see.  Farewell, until next time.\n")
        exit()
     
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# DISPLAY INFO -- FUNCTIONAL 
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

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

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# PLAYER INFO -- FUNCTIONAL 
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def player_info():
    global money, score_bonus 
    global player_name, party_member0, party_member1, party_member2, party_member3

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
   



# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# CALCULATE SCORE -- UNFINISHED
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def calc_score(): 
    score = (amt_food * 0.25) + (amt_water * 0.1) + (num_boats * 2.0) + (num_bullets * 0.05) # +  + (num_guns * ?) 
    score = score * score_bonus 
    print(f"Your final score is {score}.\n") 

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# PLAY GAME -- UNFINISHED
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def play_game():
    main_menu()

    if player_choice == 1:
        player_info()
        buy_item()
        how_fast()
        travel()
    elif player_choice == 2:
        display_info()
    elif player_choice == 3:
        # high_scores()
        print("This is a test.\n")
    else:
        print("Come back again sometime.\n")
        exit()

# !@#$%^&*())(*&^%$#@!!@#$%^&*())(*&^%$#@!!@#$%^&*())(*&^%$#@!!@#$%^&*())(*&^%$#@!
# !@#$%^&*())(*&^%$#@!!@#$%^&*())(*&^%$#@!!@#$%^&*())(*&^%$#@!!@#$%^&*())(*&^%$#@!
# TEST FUNCTION CALLS BELOW THIS LINE 
