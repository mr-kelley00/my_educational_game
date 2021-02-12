# <The Lewis and Clark Expedition Simulator>, <Ryan Kelley>, <9:20AM> <02/11/21>, <Version 1.5.0>

# TO-DO List [Update as necessary.]
# Create a how_fast() function to determine how fast the group is traveling. 
# Create a how_far() function to determine how far between each location. 
# Create a how_long() function to determine how long it will take to travel. 
# In buy_item() what happens if the player cannot afford the item? 
# In sell_item() what happens if the player does not have enough items to sell? 
# Create calc_scores() function to determine player score. 
# Create high_scores() function to display previous high scores.   


# Player Variables
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

# main_menu()
        
# Game Information Function
def game_info():
    print("""
        Update to actual paragraph of historical facts and game play tips.
        """)

# disp_info() 

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
    {num_wheels} wagon wheels can be used for repairs.
    {num_axles} wagon axles are sturdy enough for use. 
    \n
    """)

# show_inventory()

# Trading Functions

def buy_item():
    
    # how much $ do I have?
    # cost of the item, 
    # amount of item available
    # calculate total cost (num of items * cost per item)
    # pay for it (money - total cost) 
    # add it to inventory (num_wheels += 1 or num_bullets += 50)

    global money, amt_water, amt_food, num_clothing, num_guns, num_bullets, amt_rope
    global num_horses, num_boats, num_wagons, num_wheels, num_axles
           
    if current_location == "St. Louis, Missouri":
        store_name = "Sally's St. Louis General Goods Emporium"
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
                                        {store_name}
            Balance: ${money}
            [+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++]
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

def sell_item(): 
    # how much $ does the vendor have?
    # value of the item
    # amount of item I have 
    # sell it (value_item * num_items) 
    # subtract it to inventory (num_wheels += -1 or num_bullets += -50)

    global money, amt_water, amt_food, num_clothing, num_guns, num_bullets, amt_rope
    global num_horses, num_boats, num_wagons, num_wheels, num_axles
        
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

# Display Map -- Open the OS image program and display map graphics.  

def display_map():
    from PIL import Image

    # Display different map based on current location of player. 
    if current_location == "St. Louis, Missouri":
        the_map = Image.open("gfx/world_map_start.png")        
    elif current_location == "Test 0":
        the_map = Image.open("gfx/world_map_0.png")        
    elif current_location == "Test 1":
        the_map = Image.open("gfx/world_map_1.png")        
    elif current_location == "Test 2":
        the_map = Image.open("gfx/world_map_2.png")        
    else:
        the_map = Image.open("gfx/world_map_3.png")

    the_map.show() # .show() method opens the image using the system photo viewer. 

# display_map() # Comment out this function call once it works. 

# Travel: Determine travel speed, calculate distance traveled, check for disasters, consume food / water.

def how_fast(): # Determine how fast the player wants to travel, assign travel speed and resource consumption. 
    print("""
        +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+
        *                     Traveling Speed                       *
        *                                                           *
        * How fast do you want to travel each day?                  *
        * The faster you travel, the more food and water you will   *
        * consume.  The chance of sickness or injury will increase  *
        * as well.                                                  *
        *                                                           *
        * Please choose a traveling speed from the menu below.      *
        *                                                           *
        *   1. Slow [10 miles per day]                              *
        *   2. Medium [20 miles per day]                            *
        *   3. Fast [30 miles per day]                              *
        +=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+    
    \n""")

    global travel_pace, speed, resource_consume
    global chc_sick, chc_break_axle, chc_break_wheel, chc_hostile_native, chc_bad_weather, chc_boat_sink, chc_horse_fall

    travel_pace = int(input("Please enter a number and press enter.\n"))

    if travel_pace == 1: 
        speed = 10
        resource_consume = 1
        chc_sick = 0.05
        chc_break_wheel = 0.05
        chc_break_axle = 0.05
        chc_hostile_native = 0.05
        chc_bad_weather = 0.10
        chc_boat_sink = 0.05
        chc_horse_fall = 0.05
    elif travel_pace == 2: 
        speed = 20 
        resource_consume = 2
        chc_sick = 0.05
        chc_break_wheel = 0.10
        chc_break_axle = 0.10
        chc_hostile_native = 0.10
        chc_bad_weather = 0.20
        chc_boat_sink = 0.25
        chc_horse_fall = 0.15
    else: 
        speed = 30
        resource_consume = 3
        chc_sick = 0.25
        chc_break_wheel = 0.33
        chc_break_axle = 0.33
        chc_hostile_native = 0.33
        chc_bad_weather = 0.25
        chc_boat_sink = 0.33
        chc_horse_fall = 0.33

def disaster(): 
    import random
    # need to add global variables. 
    # need to add global variables. 
    # need to add global variables. 
    # need to add global variables. 
    # need to add global variables. 
    # need to add global variables. 
    # need to add global variables. 
    disaster_type = random.randint(1, 7) # This should have the MAXIMUM value for your possible disasters. 
    d100 = random.uniform(0.01, 1.0) 
    print(d100) 

    if disaster_type == 1: # Chance of sickness. 
        print("Yolo")   
        if chc_sick <= d100: 
            print("Somone in your party has fallen ill.\n  If they do not get help, they will die.\n")
    elif disaster_type == 2: # Chance of breaking a wheel. 
        # YOLO 
        print("Yolo")
        if chc_break_wheel <= d100: 
            print("A wheel has broke on your wagon!\n")
            num_wheels += -1 
    elif disaster_type == 3: # Chance of breaking an axle. 
        # YOLO 
        print("Yolo")
    elif disaster_type == 4: # Chance of hostile native attack. 
        # YOLO 
        print("Yolo")
    elif disaster_type == 5: # Chance of bad weather. 
        # YOLO 
        print("Yolo")
    elif disaster_type == 6: # Chance of boat sinking.
        # YOLO 
        print("Yolo")
    else: # Chance of horse falling.  
        # YOLO 
        print("Yolo")

disaster() 

# how_fast() 

def travel(): 
    # This function will determine how far the party travels each day. 
    global num_days, dist_travel, party_size, amt_food, amt_water
    global player_name, party_member0, party_member1, party_member2, party_member3
    global player_hp, party_member0_hp, party_member1_hp, party_member2_hp, party_member3_hp
    
    do_travel = True 
    
    while do_travel == True: 
        dist_travel += speed
        num_days += 1
        amt_food += -(resource_consume * party_size)
        if amt_food <= 0: 
            amt_food = 0
        
        amt_water += -(resource_consume * party_size)
        if amt_water <= 0: 
            amt_water = 0
          
        print(f"You have traveled {dist_travel} miles in {num_days} days.\n")
        print(f"You have {amt_food} pounds of food and {amt_water} gallons of water remaining.\n")
        
        if amt_food <= 0:  
            player_hp += -5
            party_member0_hp += -5 
            party_member1_hp += -5 
            party_member2_hp += -5 
            party_member3_hp += -5 
        else: 
            player_hp += -2
            party_member0_hp += -2
            party_member1_hp += -2 
            party_member2_hp += -2 
            party_member3_hp += -2

        if amt_water <= 0: 
            player_hp += -10
            party_member0_hp += -10 
            party_member1_hp += -10
            party_member2_hp += -10
            party_member3_hp += -10
        
        do_travel = input("Do you want to continue traveling? [Yes / No]\n")
        if do_travel == "Yes" or do_travel == "yes" or do_travel == "y":
            do_travel = True
        else: 
            do_travel = False 
            print("You decide to stop and rest for the night.\n")
            player_hp += 5
            party_member0_hp += 5 
            party_member1_hp += 5
            party_member2_hp += 5
            party_member3_hp += 5
        print(f"""
        {player_name} has {player_hp} HP remaining.
        {party_member0} has {party_member0_hp} HP remaining.
        {party_member1} has {party_member1_hp} HP remaining.
        {party_member2} has {party_member2_hp} HP remaining.
        {party_member3} has {party_member3_hp} HP remaining.
        
        \n""")

# travel() 


# Win Game: Write the function to determine if the player wins and calculates the final score and saves it to a file in the scores/ directory.

# Play Game Loop
def play_game():
    main_menu()

    if player_choice == 1:
        player_info()
        buy_item()
        how_fast()
        travel()
    elif player_choice == 2:
        game_info()
    elif player_choice == 3:
        # high_scores()
        print("This is a test.\n")
    else:
        print("Come back again sometime.\n")
        exit()

    
# Start Game Loop
# play_game() 