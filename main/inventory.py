# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# INVENTORY AND TRADE FUNCTIONS
# show_inventory() simply prints a list of items in the player's inventory. 
# buy_item() allows players to buy items from stores.  We are assuming all items are available in unlimited supply at each store. 
# sell_item() allows players to sell items to stores.  Assuming vendors have unlimited money as long as player has supply. 
# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# SHOW INVENTORY -- FUNCTIONAL
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

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

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# BUY ITEM -- FUNCTIONAL 
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def buy_item():
    
    global money, amt_water, amt_food, num_clothing, num_guns, num_bullets, amt_rope
    global num_horses, num_boats, num_wagons, num_wheels, num_axles, current_location
           
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

# ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
# SELL ITEM -- FUNCTIONAL 
# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

def sell_item(): 
    
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