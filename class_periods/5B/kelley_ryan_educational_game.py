# <The Lewis and Clark Expedition Simulator>, <Ryan Kelley>, <8:55AM> <02/24/21>, <Version 1.4.0a>

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

# show_inventory()

# Trading Functions

def buy_item():
    
    # how much $ do I have?
    # cost of the item
    # amount of item available
    # pay for it (starting_money - cost) 
    # add it to inventory (num_wheels += 1 or num_bullets += 50)

    global money
    global amt_water
    global amt_food 
    global num_clothing 
    global num_guns 
    global num_bullets 
    global amt_rope 
    global num_horses 
    global num_boats 
    global num_wagons 
    global num_wagon_wheel 
    global num_wagon_axle 
        
    if current_location == "St. Louis, Missouri":
        store_name = "The St. Louis General Goods Emporium"
        cost_multi = 0.75
    elif current_location == "Test 0":
        store_name = "Test 0 General Store"
        cost_multi = 1.25
    elif current_location == "Test 1":
        store_name = "Test 1 General Store"
        cost_multi = 1.50
    elif current_location == "Test 2":
        store_name = "Test 2 General Store"
        cost_multi = 1.50
    else:
        store_name = "Test 3 General Store"
        cost_multi = 2.5
        
    while True:
        
        print(f"""
            [+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]
            [                        {store_name}                       ]
            [                                                           ]
            [ Your Balance: ${money}                                    ]
            [ Inventory for Sale                                        ]
            [ 0) Water                                                  ]
            [ 1) Food                                                   ]
            [ 2) Clothing                                               ]
            [ 3) Guns                                                   ]
            [ 4) Bullets                                                ]
            [ 5) Rope                                                   ]
            [ 6) Horses                                                 ]
            [ 7) Boats                                                  ]
            [ 8) Wagons                                                 ]
            [ 9) Wagon Wheels                                           ]
            [ 10) Wagon Axle                                            ]
            [ 20) Exit Store                                            ]
            [+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]
            \n
            """)
        item_buy = int(input("What do you want to buy?  Type the number and press enter.\n"))

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
                amt_water += how_many
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
                amt_water += how_many
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
                amt_water += how_many
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
                amt_water += how_many
                print(f"You now have {num_rope} coils of rope.\n")
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
                amt_water += how_many
                print(f"You now have {num_horses} healthy horses.\n")
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
                amt_water += how_many
                print(f"You now have {num_boats} boats for river crossings.\n")
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
                amt_water += how_many
                print(f"You now have {num_wagons} wagons.\n")
            else:
                print("Ok, perhaps another item?\n")            
        elif item_buy == 9: # Wagon Wheels
            item_cost = cost_wagon_wheel * cost_multi
            print(f"That will cost ${item_cost} each.")
            how_many = int(input("How many would you like to buy?\n"))
            total_cost = item_cost * how_many
            print(f"That will be ${total_cost}.\n")
            purchase = input("Do you still want to buy it? Yes / No\n")
            if purchase == "yes" or purchase == "y" or purchase == "Yes":
                money = money - total_cost
                amt_water += how_many
                print(f"You now have {num_wagon_wheels} wagon wheels for repairs.\n")
            else:
                print("Ok, perhaps another item?\n")            
        elif item_buy == 10: # Wagon Axles 
            item_cost = cost_wagon_axles * cost_multi
            print(f"That will cost ${item_cost} each.")
            how_many = int(input("How many would you like to buy?\n"))
            total_cost = item_cost * how_many
            print(f"That will be ${total_cost}.\n")
            purchase = input("Do you still want to buy it? Yes / No\n")
            if purchase == "yes" or purchase == "y" or purchase == "Yes":
                money = money - total_cost
                amt_water += how_many
                print(f"You now have {num_wagon_axles} wagon axles for repairs.\n")
            else:
                print("Ok, perhaps another item?\n")            
        else:
            print("Thanks for shopping.  Come back any time!\n")
            break

# buy_item()

def sell_item(): 
    # how much $ does the vendor have?
    # value of the item
    # amount of item I have 
    # sell it (value_item * num_items) 
    # subtract it to inventory (num_wheels += -1 or num_bullets += -50)

    global money
    global amt_water
    global amt_food 
    global num_clothing 
    global num_guns 
    global num_bullets 
    global amt_rope 
    global num_horses 
    global num_boats 
    global num_wagons 
    global num_wheels 
    global num_axles 
        
    if current_location == "St. Louis, Missouri":
        store_name = "Sally's St. Louis General Goods Emporium"
        cost_multi = 0.50 # Selling items back should be worth less than buying. 
    elif current_location == "Test 0":
        store_name = "Test 0 General Store"
        cost_multi = 1.00
    elif current_location == "Test 1":
        store_name = "Test 1 General Store"
        cost_multi = 1.25
    elif current_location == "Test 2":
        store_name = "Test 2 General Store"
        cost_multi = 1.25
    else:
        store_name = "Test 3 General Store"
        cost_multi = 2.0
        
    while True:
        
        print(f"""
                                        {store_name}
            Balance: ${money}
            [+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]
            [ Inventory to Buy                                          ]
            [ 0) Water                                                  ]
            [ 1) Food                                                   ]
            [ 2) Clothing                                               ]
            [ 3) Guns                                                   ]
            [ 4) Bullets                                                ]
            [ 5) Rope                                                   ]
            [ 6) Horses                                                 ]
            [ 7) Boats                                                  ]
            [ 8) Wagons                                                 ]
            [ 9) Wagon Wheels                                           ]
            [ 10) Wagon Axle                                            ]
            [ 20) Exit Store                                            ]
            [+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]
            \n
            """)
        item_sell = int(input("What do you want to sell?  Type the number and press enter.\n"))

        # The following code will most likely work better as a loop.  Start at index[0], iterate through item list until match is found, assign correct values for transaction. 

        if item_sell == 0: # Water
            item_cost = cost_water * cost_multi
            print(f"That will cost ${item_cost} each.")
            how_many = int(input("How many would you like to sell?\n"))
            total_cost = item_cost * how_many
            print(f"That will be ${total_cost}.\n")
            sell = input("Do you still want to sell it? Yes / No\n")
            if sell == "yes" or sell == "y" or sell == "Yes":
                money = money + total_cost
                amt_water += -how_many
                print(f"You now have {amt_water} gallons of water and ${money} dollars.\n")
            else:
                print("Ok, perhaps another item?\n") 
        elif item_sell == 1: # Food
            item_cost = cost_food * cost_multi
            print(f"That will cost ${item_cost} each.")
            how_many = int(input("How many would you like to sell?\n"))
            total_cost = item_cost * how_many
            print(f"That will be ${total_cost}.\n")
            sell = input("Do you still want to sell it? Yes / No\n")
            if sell == "yes" or sell == "y" or sell == "Yes":
                money = money + total_cost
                amt_food += -how_many
                print(f"You now have {amt_food} pounds of food ${money} dollars.\n")
            else:
                print("Ok, perhaps another item?\n")            
        elif item_sell == 2: # Clothing
            item_cost = cost_clothing * cost_multi
            print(f"That will cost ${item_cost} each.")
            how_many = int(input("How many would you like to sell?\n"))
            total_cost = item_cost * how_many
            print(f"That will be ${total_cost}.\n")
            sell = input("Do you still want to sell it? Yes / No\n")
            if sell == "yes" or sell == "y" or sell == "Yes":
                money = money + total_cost
                num_clothing += -how_many
                print(f"You now have {num_clothing} sets of clothing and ${money} dollars.\n")
            else:
                print("Ok, perhaps another item?\n")            
        elif item_sell == 3: # Guns
            item_cost = cost_guns * cost_multi
            print(f"That will cost ${item_cost} each.")
            how_many = int(input("How many would you like to sell?\n"))
            total_cost = item_cost * how_many
            print(f"That will be ${total_cost}.\n")
            sell = input("Do you still want to sell it? Yes / No\n")
            if sell == "yes" or sell == "y" or sell == "Yes":
                money = money + total_cost
                num_guns += -how_many
                print(f"You now have {amt_water} gallons of water.\n")
            else:
                print("Ok, perhaps another item?\n")            
        elif item_sell == 4: # Bullets
            item_cost = cost_bullets * cost_multi
            print(f"That will cost ${item_cost} each.")
            how_many = int(input("How many would you like to sell?\n"))
            total_cost = item_cost * how_many
            print(f"That will be ${total_cost}.\n")
            sell = input("Do you still want to sell it? Yes / No\n")
            if sell == "yes" or sell == "y" or sell == "Yes":
                money = money + total_cost
                num_bullets += -how_many
                print(f"You now have {num_bullets} bullets and ${money} dollars.\n")
            else:
                print("Ok, perhaps another item?\n")            
        elif item_sell == 5: # Rope
            item_cost = cost_rope * cost_multi
            print(f"That will cost ${item_cost} each.")
            how_many = int(input("How many would you like to sell?\n"))
            total_cost = item_cost * how_many
            print(f"That will be ${total_cost}.\n")
            sell = input("Do you still want to sell it? Yes / No\n")
            if sell == "yes" or sell == "y" or sell == "Yes":
                money = money + total_cost
                amt_rope += -how_many
                print(f"You now have {amt_rope} feet of rope and ${money} dollars.\n")
            else:
                print("Ok, perhaps another item?\n")            
        elif item_sell == 6: # Horses
            item_cost = cost_horses * cost_multi
            print(f"That will cost ${item_cost} each.")
            how_many = int(input("How many would you like to sell?\n"))
            total_cost = item_cost * how_many
            print(f"That will be ${total_cost}.\n")
            sell = input("Do you still want to sell it? Yes / No\n")
            if sell == "yes" or sell == "y" or sell == "Yes":
                money = money + total_cost
                num_horses += -how_many
                print(f"You now have {num_horses} horses and ${money} dollars.\n")
            else:
                print("Ok, perhaps another item?\n")            
        elif item_sell == 7: # Boats
            item_cost = cost_boats * cost_multi
            print(f"That will cost ${item_cost} each.")
            how_many = int(input("How many would you like to sell?\n"))
            total_cost = item_cost * how_many
            print(f"That will be ${total_cost}.\n")
            sell = input("Do you still want to sell it? Yes / No\n")
            if sell == "yes" or sell == "y" or sell == "Yes":
                money = money + total_cost
                num_boats += -how_many
                print(f"You now have {num_boats} working boats and ${money} dollars.\n")
            else:
                print("Ok, perhaps another item?\n")            
        elif item_sell == 8: # Wagons
            item_cost = cost_wagons * cost_multi
            print(f"That will cost ${item_cost} each.")
            how_many = int(input("How many would you like to sell?\n"))
            total_cost = item_cost * how_many
            print(f"That will be ${total_cost}.\n")
            sell = input("Do you still want to sell it? Yes / No\n")
            if sell == "yes" or sell == "y" or sell == "Yes":
                money = money + total_cost
                num_wagons += -how_many
                print(f"You now have {num_wagons} wagons and ${money} dollars.\n")
            else:
                print("Ok, perhaps another item?\n")            
        elif item_sell == 9: # Wagon Wheels
            item_cost = cost_wagon_wheel * cost_multi
            print(f"That will cost ${item_cost} each.")
            how_many = int(input("How many would you like to sell?\n"))
            total_cost = item_cost * how_many
            print(f"That will be ${total_cost}.\n")
            sell = input("Do you still want to sell it? Yes / No\n")
            if sell == "yes" or sell == "y" or sell == "Yes":
                money = money + total_cost
                num_wheels += -how_many
                print(f"You now have {num_wheels} spare wagon wheels and ${money} dollars.\n")
            else:
                print("Ok, perhaps another item?\n")            
        elif item_sell == 10: # Wagon Axles 
            item_cost = cost_wagon_axle * cost_multi
            print(f"That will cost ${item_cost} each.")
            how_many = int(input("How many would you like to sell?\n"))
            total_cost = item_cost * how_many
            print(f"That will be ${total_cost}.\n")
            sell = input("Do you still want to sell it? Yes / No\n")
            if sell == "yes" or sell == "y" or sell == "Yes":
                money = money + total_cost
                num_axles += -how_many
                print(f"You now have {num_axles} spare wagon axles and ${money} dollars.\n")
            else:
                print("Ok, perhaps another item?\n")            
        else:
            print("Thanks for shopping.  Come back any time!\n")
            break

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

# display_map() # Uncomment this to test. 
    
# Travel: Determine travel speed, calculate distance traveled, check for disasters, consume food / water.

# Calculate Final Score 
def calc_score(): 

    final_score = (party_size * 250) + (money * 50) + (amt_water * 0.5) + (amt_food * 0.5) + (num_clothing * 1.0)  
    final_score += (num_guns * 2.0) + (num_bullets * 0.25) + (num_rope * 1.0) + (num_horses * 5.0) + (num_boats * 25.0)  
    final_score += (num_wagons * 10.0) + (num_wagon_wheel * 2.5) + (num_wagon_axle * 2.5)
    final_score = final_score * score_bonus # Multiply final_score by the score_bonus.  

    print(final_score)

# player_info() 
# calc_score() 