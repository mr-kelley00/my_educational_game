# <Lewis and Clark Expedition Extravaganza>, <Ryan Kelley>, <02/04/21> <12:31PM>, <Version 1.3.1>

# To-Do List 
# Create variables to track the health (HP) for each person in the group. 
# In buy_item() what will happen if the player does not have enough money to make a purchase? 
# In sell_item() what will happen if the player doees not have enough of an item to sell back? 
# Create how_fast() function to determine how fast the group is traveling and its effects (hunger, thirst, etc.)
# Create how_far() function to determine how far each location is and amount of distance traveled. 
# Create how_long() function to determine amount of time it takes to travel (DISTANCE / SPEED). 


# Player Variables 
player_score = 0
player_name = ""
player_hp = 100 

party_member0 = ""
party_member0_hp = 100 

party_member1 = ""
party_member1_hp = 100 

party_member2 = ""
party_member2_hp = 100 

party_member3 = ""
party_member3_hp = 100 

player_job = ""
money = 0

# Inventory Variables 
num_boats = 0
num_guns = 0
num_bullets = 0
num_food = 0
num_water = 0
num_wagons = 0
num_horses = 0
num_wagon_wheel = 0
num_wagon_axle = 0
num_clothing = 0
num_pelts = 0
num_traps = 0

# Cost Variables 
cost_boats = 20.0 # Price per boat. 
cost_guns = 5.0 # price per gun. 
cost_bullets = 2.50 # Box of 50. 
cost_food = 0.25 # per pound.
cost_water = 0.10 # per gallon.
cost_wagons = 10.0 # per wagon.
cost_horses = 5.0 # per pair. 
cost_wagon_wheel = 3.50 # each
cost_wagon_axle = 3.50 # each 
cost_clothing = 1.0 # per set
cost_pelts = 2.0 # each 
cost_traps = 1.0 # each

# Location Variables
starting_point = "St. Louis, Missouri"
ending_point = "Fort Calstop" 
location0 = " "
location1 = " "
location2= " "
current_location = starting_point

# Time / Date / Distance Variables 
game_time = 0
game_date = 0
landmark_distance = 0
total_distance = 0 

# Disaster Variables
chnc_sick = 0.0
chnc_die = 0.0
chnc_wheel_break = 0.0
chnc_axle_break = 0.0
chnc_bad_weather = 0.0


# Main Menu
def main_menu():
    print("++==++==++==++==++==++==++==++==++==++==++==++==++==++==++==++==++")
    print("|                      The Lewis and Clark Expedition            |")
    print("|                                 by                             |")
    print("|                        Ryan Kelley Game Studios                |")
    print("|                                                                |")
    print("|   1) Begin Your Journey                                        |")
    print("|   2) Learn More about the Lewis and Clark Expedition           |")
    print("|   3) See the High Scores                                       |")
    print("|   4) Exit Game                                                 |")
    print("|                                                                |")
    print("++==++==++==++==++==++==++==++==++==++==++==++==++==++==++==++==++")
    global player_choice
    player_choice = int(input("Please type a number from the menu and press enter.\n"))
    # print(player_choice)
    if player_choice == 1:
        print("Good luck brave explorer.  Farewell on your journey!\n")
    elif player_choice == 2:
        print("You have decided to study more before adventuring.  Wise choice.\n")
    elif player_choice == 3:
        print("Let us see who has gone before you and done well!\n")
    else:
        print("Not all are brave enough to take this journey.  Perhaps another time?\n")
        exit()
    return player_choice  
    
# main_menu()

# Display Info.
def disp_info():
    print("Make this function print historical information about the journey.\n")
    print("Also make it print some tips and tricks to help the player in the game.\n")
    print("For example, with Oregon trail this part of the game explained the best time to leave.\n")

# disp_info()           

# Player Info. Function
def player_info():

    global player_name
    global party_member0
    global party_member1
    global party_member2
    global party_member3
    global money 
    
    player_name = input("Greetings brave traveler!  What should I call you?\n")
    party_member0 = input("I see you have a second person with you.  What is their name?\n")
    party_member1 = input("You have a third?  By what name are they known?\n")
    party_member2 = input("Four people makes quite the crowd. Do they have a name?\n")
    party_member3 = input("Now five of you?  Any more will be too many.  What do I call them?\n")
    print(f"{player_name}, you are a brave leader.  Good luck to you and {party_member0}, {party_member1}, {party_member2}, and {party_member3}.\n")
    print("""
The Lewis and Clark expedition had many important job roles.  Each person had to do their share
to ensure that the trip went safely.  One of the most important roles was that of translator.  Lewis
and Clark would encounter many native tribes along the journey, communicating with them was extremely
important. The trappers that accompanied Lewis and Clark were able to provide food and pelts, both of
which could be used as valuable trade items with the tribes.  Finally, the cooks were also important
members of the group.  Keeping the expedition well fed meant better health for everyone.

What job would you like?
-- Translator
-- Trapper
-- Cook

    """)
    global player_job
    player_job = input("Please type the name of the job and press enter.\n")
    global score_bonus
    
    if player_job == "translator" or player_job == "Translator" or player_job == "TRANSLATOR":
        print("You have chosen to be a translator.\n")
        score_bonus = 1
        money = 1000
    elif player_job == "trapper" or player_job == "Trapper" or player_job == "TRAPPER":
        print("You have chosen to be a trapper.\n")
        score_bonus = 2
        money = 750
    else:
        print("You have chosen to be a cook.\n")
        score_bonus = 3
        money = 500
    print(f"You will start with a score bonus of {score_bonus} and ${money} dollars.\n") 
    
    
player_info()


# Trading Transactions

def buy_item():
    # figure out player money
    # cost of the items
    # menu of items
    # total cost = number of items * cost of item
    # pay for item (subtract total cost from player balance)
    # add the item to player inventory
    
    global num_boats 
    global num_guns 
    global num_bullets 
    global num_food 
    global num_water 
    global num_horses 
    global num_wagon_wheel 
    global num_wagon_axle 
    global num_pelts 
    global num_traps
    global money

    if current_location == "St. Louis, Missouri":
        store_name = "Sally's St. Louis Super Store!\n"
        cost_multiplier = 0.75
    elif current_location == "Test Location 1":
        store_name = "Test Store #1!\n"
        cost_multiplier = 1.0
    elif current_location == "Test Location 2":
        store_name = "Test Store #2!\n"
        cost_multiplier = 1.25
    elif current_location == "Test Location 3":
        store_name = "Test Store #2!\n"
        cost_multiplier = 1.25
    else: # This will be the LAST location before the end_point.
        store_name = "Last Location before End Point!\n"
        cost_multiplier = 2.0 
        
    while True:
        print(f"""
                            {store_name}
        Your Balance: ${money}
        ++==++==++==++==++==++==++==++==++==++==++==++==++==++==++==++==++
        |                      Available Items for Sale                  |
        |                                                                |
        | 0) Boats    1) Guns     2) Bullets    3) Food                  |
        | 4) Water    5) Horses   6) Wheels     7) Axles                 | 
        | 8) Pelts    9) Traps                                           |
        | 20) Exit Store                                                 |
        ++==++==++==++==++==++==++==++==++==++==++==++==++==++==++==++==++
        \n
        """)
        item_buy = int(input("Please type a number and press enter.\n"))


        if item_buy == 0: # Boats 
            item_cost = cost_boats * cost_multiplier
            print(f"Each boat will cost ${item_cost}.\n")
            how_many = int(input("How many would you like to purchase?\n"))
            total_cost = item_cost * how_many
            print(f"The total cost will be ${total_cost}.\n")
            purchase = input("Do you still want to buy it?  Yes / No\n")
            if purchase == "yes" or purchase == "y" or purchase == "Yes":
                money = money - total_cost 
                num_boats += how_many 
                print(f"You now have {num_boats} available.\n")
            else: 
                print("Ok, perhaps something else?\n")
        elif item_buy == 1: # Guns 
            item_cost = cost_guns * cost_multiplier
            print(f"Each gun will cost ${item_cost}.\n")
            how_many = int(input("How many would you like to purchase?\n"))
            total_cost = item_cost * how_many
            print(f"The total cost will be ${total_cost}.\n")
            purchase = input("Do you still want to buy it?  Yes / No\n")
            if purchase == "yes" or purchase == "y" or purchase == "Yes":
                money = money - total_cost 
                num_guns += how_many 
                print(f"You now have {num_guns} available.\n")
            else: 
                print("Ok, perhaps something else?\n")
        elif item_buy == 2: # Guns 
            item_cost = cost_guns * cost_multiplier
            print(f"Each gun will cost ${item_cost}.\n")
            how_many = int(input("How many would you like to purchase?\n"))
            total_cost = item_cost * how_many
            print(f"The total cost will be ${total_cost}.\n")
            purchase = input("Do you still want to buy it?  Yes / No\n")
            if purchase == "yes" or purchase == "y" or purchase == "Yes":
                money = money - total_cost 
                num_guns += how_many 
                print(f"You now have {num_guns} available.\n")
            else: 
                print("Ok, perhaps something else?\n")
        elif item_buy == 3: # Guns 
            item_cost = cost_guns * cost_multiplier
            print(f"Each gun will cost ${item_cost}.\n")
            how_many = int(input("How many would you like to purchase?\n"))
            total_cost = item_cost * how_many
            print(f"The total cost will be ${total_cost}.\n")
            purchase = input("Do you still want to buy it?  Yes / No\n")
            if purchase == "yes" or purchase == "y" or purchase == "Yes":
                money = money - total_cost 
                num_guns += how_many 
                print(f"You now have {num_guns} available.\n")
            else: 
                print("Ok, perhaps something else?\n")
        elif item_buy == 4: # Guns 
            item_cost = cost_guns * cost_multiplier
            print(f"Each gun will cost ${item_cost}.\n")
            how_many = int(input("How many would you like to purchase?\n"))
            total_cost = item_cost * how_many
            print(f"The total cost will be ${total_cost}.\n")
            purchase = input("Do you still want to buy it?  Yes / No\n")
            if purchase == "yes" or purchase == "y" or purchase == "Yes":
                money = money - total_cost 
                num_guns += how_many 
                print(f"You now have {num_guns} available.\n")
            else: 
                print("Ok, perhaps something else?\n")
        elif item_buy == 5: # Guns 
            item_cost = cost_guns * cost_multiplier
            print(f"Each gun will cost ${item_cost}.\n")
            how_many = int(input("How many would you like to purchase?\n"))
            total_cost = item_cost * how_many
            print(f"The total cost will be ${total_cost}.\n")
            purchase = input("Do you still want to buy it?  Yes / No\n")
            if purchase == "yes" or purchase == "y" or purchase == "Yes":
                money = money - total_cost 
                num_guns += how_many 
                print(f"You now have {num_guns} available.\n")
            else: 
                print("Ok, perhaps something else?\n")
        elif item_buy == 6: # Guns 
            item_cost = cost_guns * cost_multiplier
            print(f"Each gun will cost ${item_cost}.\n")
            how_many = int(input("How many would you like to purchase?\n"))
            total_cost = item_cost * how_many
            print(f"The total cost will be ${total_cost}.\n")
            purchase = input("Do you still want to buy it?  Yes / No\n")
            if purchase == "yes" or purchase == "y" or purchase == "Yes":
                money = money - total_cost 
                num_guns += how_many 
                print(f"You now have {num_guns} available.\n")
            else: 
                print("Ok, perhaps something else?\n")
        elif item_buy == 7: # Guns 
            item_cost = cost_guns * cost_multiplier
            print(f"Each gun will cost ${item_cost}.\n")
            how_many = int(input("How many would you like to purchase?\n"))
            total_cost = item_cost * how_many
            print(f"The total cost will be ${total_cost}.\n")
            purchase = input("Do you still want to buy it?  Yes / No\n")
            if purchase == "yes" or purchase == "y" or purchase == "Yes":
                money = money - total_cost 
                num_guns += how_many 
                print(f"You now have {num_guns} available.\n")
            else: 
                print("Ok, perhaps something else?\n")
        elif item_buy == 8: # Guns 
            item_cost = cost_guns * cost_multiplier
            print(f"Each gun will cost ${item_cost}.\n")
            how_many = int(input("How many would you like to purchase?\n"))
            total_cost = item_cost * how_many
            print(f"The total cost will be ${total_cost}.\n")
            purchase = input("Do you still want to buy it?  Yes / No\n")
            if purchase == "yes" or purchase == "y" or purchase == "Yes":
                money = money - total_cost 
                num_guns += how_many 
                print(f"You now have {num_guns} available.\n")
            else: 
                print("Ok, perhaps something else?\n")
        elif item_buy == 9: # Guns 
            item_cost = cost_guns * cost_multiplier
            print(f"Each gun will cost ${item_cost}.\n")
            how_many = int(input("How many would you like to purchase?\n"))
            total_cost = item_cost * how_many
            print(f"The total cost will be ${total_cost}.\n")
            purchase = input("Do you still want to buy it?  Yes / No\n")
            if purchase == "yes" or purchase == "y" or purchase == "Yes":
                money = money - total_cost 
                num_guns += how_many 
                print(f"You now have {num_guns} available.\n")
            else: 
                print("Ok, perhaps something else?\n")
        else: 
            print("Thank you for shopping.  Come back any time!\n")
            break 

     
buy_item() 


# Map Display 
def display_map(): 
    from PIL import Image 

    if current_location == "St. Louis, Missouri":
        the_map = Image.open("gfx/world_map.png")
    elif current_location == "Test Location 1":
        the_map = Image.open("gfx/world_map_1.png")
    elif current_location == "Test Location 2":
        the_map = Image.open("gfx/world_map_2.png")
    elif current_location == "Test Location 3":
        the_map = Image.open("gfx/world_map_3.png")
    else: # This will be the LAST location before the end_point.
        the_map = Image.open("gfx/world_map_4.png")

    the_map.show() 

display_map() 




        
    
    
    
