# <The Lewis and Clark Expedition>, <Ryan Kelley>, <2:57PM> <02/25/21>, <Version 1.2.5>

# Player Variables
occupation = "" 
money = 0
score_bonus = 0
player_name = ""
party_member0 = ""
party_member1 = ""
party_member2 = ""
party_member3 = ""

party_size = 5
player_hp = 100
party_member0_hp = 100
party_member1_hp = 100
party_member2_hp = 100
party_member3_hp = 100

# Supply Variables
amount_food = 0
amount_water = 0
num_boats = 0
num_guns = 0
num_bullets = 0
num_horses = 0
num_wagons = 0
num_clothing = 0
num_cows = 0
num_chickens = 0
num_pigs = 0

# Costs of Supplies
cost_food = 0
cost_water = 0
cost_boats = 0
cost_guns = 0
cost_bullets = 0
cost_horses = 0
cost_wagons = 0
cost_clothing = 0
cost_cows = 0
cost_chickens = 0
cost_pigs = 0

# Location Variables
starting_point = "St. Louis, Missouri"
ending_point = "Fort Calstop"
location0 = "Test 1"
location1 = "Test 2"
location2 = "Test 3"
current_location = starting_point 


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

#main_menu() 

# Display info about the expedition.  
def disp_info():
    print("""
        Write at least ONE PARAGRAPH of FACTUAL INFORMATION ABOUT YOUR EXPEDITION.\n
        """)
#disp_info()

# Player Info Function
def player_info():
    global player_name, party_member0, party_member1, party_member2, party_member3
    global score_bonus, money, occupation
    
    player_name = input("What should I call you?\n")
    print(f"{player_name} is a mighty fine name.  What about the other people in your group?\n")
    party_member0 = input("Who else is traveling with you?\n")
    party_member1 = input("I see you have someone else with you.  What is their name?\n")
    party_member2 = input("A third person is joining?  What do I call them?\n")
    party_member3 = input("Last but not least, who is the fourth person in your group?\n")
    print(f"Ok {player_name}.  I hope that {party_member0}, {party_member1}, {party_member2}, and {party_member3} all arrive safely.\n")
    print(f"""On the Lewis and Clark journey the following jobs were important: scout, cook, and trapper.
    Which job would you like to choose?
    -- Scout
    -- Cook
    -- Trapper
    """)
    occupation = input("Which job do you want to choose?\n")
    print(occupation)
    if occupation == "Scout" or occupation == "scout" or occupation == "SCOUT":
        print("You have chosen the scout role.  You will get the most amount of money and highest score bonus.\n") 
        score_bonus = 3
        money = 1000
    elif occupation == "Cook" or occupation == "cook" or occupation == "COOK":
        print("You have chosen the cook role.  You will get a higher amount of money and score bonus.\n")
        score_bonus = 2
        money = 750
    elif occupation == "Trapper" or occupation == "trapper" or occupation == "TRAPPER":
        print("You have chosen the trapper role.  You will get more money and small score bonus.\n")
        score_bonus = 1
        money = 500
    else:
        print("You did not choose a job from the list so you will be a dishwasher.  You get nothing.\n")
        score_bonus = 0
        money = 250
    print(f"{player_name}, you will have {money} DOLLARS / YEN / GOLD.\n")
    print(f"You will also receive a score multiplier of {score_bonus} when you finish.\n")   
    
# player_info()

# Show Inventory Function 
def show_inventory():
    print(f"""
{amount_food} pounds of food. 
{amount_water} gallons of water.
{num_boats} boats that sail. 
{num_guns} guns that go pew pew!
{num_bullets} bullets available for defense.
{num_horses} healthy horses.
{num_wagons} working wagons.
{num_clothing} comfortable sets of clothing. 
\n
""")

# show_inventory() 
    
# Trading Transactions

def buy_item():
        
    global amount_food
    global amount_water 
    global num_guns 
    global num_bullets 
    global num_horses 
    global num_wagons 
    global num_boats 
    global num_clothing 
    global num_cows 
    global num_chickens 
    global num_pigs
    global money 

    if current_location == "St. Louis, Missouri":
        store_name = "Sally's St. Louis Super Mart!\n"
        cost_multi = 0.75
    elif current_location == "Test 0":
        store_name = "Test 0 Store Name\n"
        cost_multi = 1.0
    elif current_location == "Test 1":
        store_name = "Test 1 Store Name\n"
        cost_multi = 1.5
    else:
        store_name = "Test 2 Store Name\n"
        cost_multi = 2.0

    while True:
        print(f"""
                                {store_name}
        Current Balance: ${money}
        \n
        +=============================================================+
        |               Available Inventory for Sale                  |
        |                                                             |
        | 0) Food    1) Water    2) Guns  3) Bullets                  |
        | 4) Horses  5) Wagons   6) Boat  7) Clothing                 |
        | 8) Cows    9) Chickens 10) Pigs                             |
        | 20) Exit Store                                              |
        +=============================================================+
        \n
        """)
        # Write the code here to let the player select an item.  Save it as an INTEGER.  
        item_buy = int(input("What do you want to buy?  Type the number and press enter.\n"))

        # The following code will most likely work better as a loop.  Start at index[0], iterate through item list until match is found, assign correct values for transaction. 

        if item_buy == 0: # Water
            item_cost = cost_water * cost_multi
            print(f"That will cost ${item_cost} each.")
            how_many = int(input("How many would you like to buy?\n"))
            total_cost = item_cost * how_many
            print(f"That will be ${total_cost}.\n")
            purchase = input("Do you still want to buy it? Yes / No\n")
            if purchase == "yes" or purchase == "y" or purchase == "Yes":
                money = money - total_cost
                amt_water += how_many
                print(f"You now have {amt_water} gallons of water.\n")
            else:
                print("Ok, perhaps another item?\n") 
        elif item_buy == 1: # Food
            item_cost = cost_food * cost_multi
            print(f"That will cost ${item_cost} each.")
            how_many = int(input("How many would you like to buy?\n"))
            total_cost = item_cost * how_many
            print(f"That will be ${total_cost}.\n")
            purchase = input("Do you still want to buy it? Yes / No\n")
            if purchase == "yes" or purchase == "y" or purchase == "Yes":
                money = money - total_cost
                amt_food += how_many
                print(f"You now have {amt_food} pounds of food.\n")
            else:
                print("Ok, perhaps another item?\n")            
        elif item_buy == 2: # Clothing
            item_cost = cost_clothing * cost_multi
            print(f"That will cost ${item_cost} each.")
            how_many = int(input("How many would you like to buy?\n"))
            total_cost = item_cost * how_many
            print(f"That will be ${total_cost}.\n")
            purchase = input("Do you still want to buy it? Yes / No\n")
            if purchase == "yes" or purchase == "y" or purchase == "Yes":
                money = money - total_cost
                num_clothing += how_many
                print(f"You now have {num_clothing} sets of clothing.\n")
            else:
                print("Ok, perhaps another item?\n")            
        elif item_buy == 3: # Guns
            item_cost = cost_guns * cost_multi
            print(f"That will cost ${item_cost} each.")
            how_many = int(input("How many would you like to buy?\n"))
            total_cost = item_cost * how_many
            print(f"That will be ${total_cost}.\n")
            purchase = input("Do you still want to buy it? Yes / No\n")
            if purchase == "yes" or purchase == "y" or purchase == "Yes":
                money = money - total_cost
                num_guns += how_many
                print(f"You now have {num_guns} guns.\n")
            else:
                print("Ok, perhaps another item?\n")            
        elif item_buy == 4: # Bullets
            item_cost = cost_bullets * cost_multi
            print(f"That will cost ${item_cost} each.")
            how_many = int(input("How many would you like to buy?\n"))
            total_cost = item_cost * how_many
            print(f"That will be ${total_cost}.\n")
            purchase = input("Do you still want to buy it? Yes / No\n")
            if purchase == "yes" or purchase == "y" or purchase == "Yes":
                money = money - total_cost
                num_bullets += how_many
                print(f"You now have {num_bullets} bullets.\n")
            else:
                print("Ok, perhaps another item?\n")            
        elif item_buy == 5: # Rope
            item_cost = cost_rope * cost_multi
            print(f"That will cost ${item_cost} each.")
            how_many = int(input("How many would you like to buy?\n"))
            total_cost = item_cost * how_many
            print(f"That will be ${total_cost}.\n")
            purchase = input("Do you still want to buy it? Yes / No\n")
            if purchase == "yes" or purchase == "y" or purchase == "Yes":
                money = money - total_cost
                amt_rope += how_many
                print(f"You now have {amt_rope} feet of rope.\n")
            else:
                print("Ok, perhaps another item?\n")            
        elif item_buy == 6: # Horses
            item_cost = cost_horses * cost_multi
            print(f"That will cost ${item_cost} each.")
            how_many = int(input("How many would you like to buy?\n"))
            total_cost = item_cost * how_many
            print(f"That will be ${total_cost}.\n")
            purchase = input("Do you still want to buy it? Yes / No\n")
            if purchase == "yes" or purchase == "y" or purchase == "Yes":
                money = money - total_cost
                num_horses += how_many
                print(f"You now have {num_horses} horses.\n")
            else:
                print("Ok, perhaps another item?\n")            
        elif item_buy == 7: # Boats
            item_cost = cost_boats * cost_multi
            print(f"That will cost ${item_cost} each.")
            how_many = int(input("How many would you like to buy?\n"))
            total_cost = item_cost * how_many
            print(f"That will be ${total_cost}.\n")
            purchase = input("Do you still want to buy it? Yes / No\n")
            if purchase == "yes" or purchase == "y" or purchase == "Yes":
                money = money - total_cost
                num_boats += how_many
                print(f"You now have {num_boats} boats.\n")
            else:
                print("Ok, perhaps another item?\n")            
        elif item_buy == 8: # Wagons
            item_cost = cost_wagons * cost_multi
            print(f"That will cost ${item_cost} each.")
            how_many = int(input("How many would you like to buy?\n"))
            total_cost = item_cost * how_many
            print(f"That will be ${total_cost}.\n")
            purchase = input("Do you still want to buy it? Yes / No\n")
            if purchase == "yes" or purchase == "y" or purchase == "Yes":
                money = money - total_cost
                num_wagons += how_many
                print(f"You now have {num_wagons} wagons.\n")
            else:
                print("Ok, perhaps another item?\n")            
        elif item_buy == 9: # Wheels
            item_cost = cost_wagon_wheel * cost_multi
            print(f"That will cost ${item_cost} each.")
            how_many = int(input("How many would you like to buy?\n"))
            total_cost = item_cost * how_many
            print(f"That will be ${total_cost}.\n")
            purchase = input("Do you still want to buy it? Yes / No\n")
            if purchase == "yes" or purchase == "y" or purchase == "Yes":
                money = money - total_cost
                num_wheels += how_many
                print(f"You now have {num_wheels} spare wagon wheels.\n")
            else:
                print("Ok, perhaps another item?\n")            
        elif item_buy == 10: # Axles
            item_cost = cost_wagon_axle * cost_multi
            print(f"That will cost ${item_cost} each.")
            how_many = int(input("How many would you like to buy?\n"))
            total_cost = item_cost * how_many
            print(f"That will be ${total_cost}.\n")
            purchase = input("Do you still want to buy it? Yes / No\n")
            if purchase == "yes" or purchase == "y" or purchase == "Yes":
                money = money - total_cost
                num_axles += how_many
                print(f"You now have {num_axles} spare wagon axles.\n")
            else:
                print("Ok, perhaps another item?\n")            
        else:
            print("Thanks for shopping.  Come back any time!\n")
            break

# buy_item()


# Display Map
def display_map():
    from PIL import Image 

    if current_location == "St. Louis, Missouri":
        the_map = Image.open("gfx/world_map.png") 
    elif current_location == "Test 0":
        the_map = Image.open("gfx/world_map0.png") 
    elif current_location == "Test 1":
        the_map = Image.open("gfx/world_map1.png")
    elif current_location == "Test 2":
        the_map = Image.open("gfx/world_map2.png") 
    else:
        the_map = Image.open("gfx/world_map3png")

    the_map.show()

# display_map() # Function call for display map. 

# Travel Functions 
def how_fast(): 
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("*                            Traveling Speed                        *")
    print("*                                                                   *")
    print("*  On this menu you can choose how fast you want to travel.         *")
    print("*                                                                   *")
    print("*  WARNING:  The faster you travel, the more food & water you use.  *")
    print("*  Traveling at high rates of speed also increases the chance of    *")
    print("*  accidents or other disasters.                                    *")
    print("*                                                                   *")
    print("*                                                                   *")
    print("*    1. Slow [15 Miles Daily]                                       *")
    print("*    2. Moderate [30 Miles Daily]                                   *")
    print("*    3. Fast [60 Miles Daily]                                       *")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")

    global travel_pace, speed, resource_consume 
    global chnc_sick, chnc_die, chnc_injury, chnc_hostile_natives, chnc_wagon_accident, chnc_bear_attack

    travel_pace = int(input("Please choose a number from the menu and press enter.\n"))
    print(travel_pace)

    if travel_pace == 1: 
        speed = 15
        resource_consume = 1.0
        chnc_sick = 10 # 10% Chance 
        chnc_die = 25 # 25% Chance 
        chnc_injury = 50 # 50% Chance
        chnc_hostile_natives = 60 = # 60% Chance
        chnc_wagon_accident = 0 # 0% Chance
        chnc_bear_attack = 100 # 100% Chance 
    elif ?: 
        ?
        ?
        ?
        ?
        ?
        ?
        ?
        ?
    else: 
        ?
        ?
        ?
        ?
        ?
        ?
        ?
        ?



how_fast()




# Calculate Final Score 
def calc_score(): 
    
    
    # num_boats = 0
    #num_3guns = 0
    # num_bullets = 0
    # num_horses = 0
    #   num_wagons = 0
    #num_clothing = 0
    #num_cows = 0
    #num_chickens = 0
    #num_pigs = 0
    final_score = (money * 5) + (party_size * 100) + (amount_food * 0.25) + (amount_water * 0.25) # Finish
    final_score = final_score * score_bonus
    print(f"You have finished with {final_score} points!\n")
    
# calc_score()        
        
        
        




