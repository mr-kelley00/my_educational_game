# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# TRAVEL FUNCTIONS
# show_inventory() simply prints a list of items in the player's inventory. 
# buy_item() allows players to buy items from stores.  We are assuming all items are available in unlimited supply at each store. 
# sell_item() allows players to sell items to stores.  Assuming vendors have unlimited money as long as player has supply. 
# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# DISPLAY MAP -- NEEDS IMPROVEMENT 
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

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

# //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# HOW FAST -- NEEDS IMPROVEMENT 
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

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
        chc_sick = 5 # This is the % chance of it happening.  
        chc_break_wheel = 5
        chc_break_axle = 5
        chc_hostile_native = 5
        chc_bad_weather = 10
        chc_boat_sink = 5
        chc_horse_fall = 5
    elif travel_pace == 2: 
        speed = 20 
        resource_consume = 2
        chc_sick = 5
        chc_break_wheel = 10
        chc_break_axle = 10
        chc_hostile_native = 10
        chc_bad_weather = 20
        chc_boat_sink = 25
        chc_horse_fall = 15
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

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# DETERMINE DISASTERS -- UNFINISHED
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

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

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# MAIN TRAVEL LOOP -- UNFINISHED
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

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