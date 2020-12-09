# <Educational Game>, <Ryan Kelley>, <2:46PM> <12/09/20>, <Version 0.47a>

# Player Variables
player_name = ""
party_member0 = "" 
party_member1 = ""
party_member2 = ""
party_member3 = ""
starting_role = ""
score_bonus = 0
money = 0

# Inventory Variables
num_food = 0
num_water = 0
num_wagons = 0
num_boats = 0
num_guns = 0
num_bullets = 0
num_horses = 0
num_wagon_wheel = 0
num_wagon_axle = 0
num_pelts = 0
num_beads = 0
num_traps = 0

# Inventory Cost Variables
cost_mult = 1.0
cost_food = 0.25 # per pound
cost_water = 0.50 # per 10 gallons
cost_wagons = 10.0 # each
cost_boats = 20.0 # each
cost_guns = 3.50 # Dang you Lochness Monster! 
cost_bullets = 1.0 # box of 20
cost_horses = 2.50 # each
cost_wagon_wheel = 1.75 # each
cost_wagon_axle = 1.25 # each
cost_pelts = 0.75 # each
cost_beads = 0.10 # each
cost_traps = 1.0 # each

# Location Variables 
starting_point = "St. Louis, Missouri"
ending_point = "Fort Calstop"
locat0 = " "
locat1 = " "
locat2 = " " 

# Disaster Variables, % chance of occurrence.
player_sick = 0.0
player_death = 0.0
party_sick = 0.0
party_death = 0.0
bad_weather = 0.0
got_lost = 0.0
wagon_wheel_break = 0.0
wagon_axle_break = 0.0
hostile_natives = 0.0
animal_attack = 0.0




# Main Menu Function
def main_menu():
    print("+=====++=====++=====++=====++=====++=====++=====++=====++=====+")
    print("+                          Ryan Kelley Games                  +")
    print("+                                presents                     +")
    print("+                           Lewis and Clark                   +")
    print("+                                 in                          +")
    print("+                        \"WHERE THE HECK ARE WE?\"             +")
    print("+                                                             +")
    print("+    Please choose an option from the menu.                   +")
    print("+    1. Begin your journey.                                   +")
    print("+    2. Learn more about the journey.                         +")
    print("+    3. See the high scores.                                  +")
    print("+    4. Exit Game                                             +")
    print("+                                                             +")
    print("+=====++=====++=====++=====++=====++=====++=====++=====++=====+")
    global player_choice
    player_choice = int(input("Please type your choice and press enter.  \n"))
    if player_choice == 1:
        print("Ah, brave adventurer!  Good luck on your journey.  Be safe!\n")
    elif player_choice == 2:
        print("Wise choice.  Let us learn more before we depart.\n")
    elif player_choice == 3:
        print("Care to see who has done well before you I see...\n")
    else:
        print("Not all are brave enough for this task.  Farewell!\n") 
        exit() 
    return player_choice

# main_menu()

# Display Info. Function
def display_info():
    print("""
        YOU NEED TO WRITE AT LEAST ONE PARAGRAPH WITH INFORMATION ABOUT YOUR EXPEDITION THAT WILL
        HELP THE PLAYER.  IT MUST BE FACTUAL AND IN YOUR OWN WORDS.  DO NOT JUST CTRL-C AND CTRL-V
        FROM WIKIPEDIA.
        """) 

# display_info()

# Check High Scores Function
# def high_scores():
    # Open high_scores file from the hard drive.
    # Print high_scores file to the screen.
    # Close high scores file.
    # Exit

# Player Info. Function
def player_info():
    player_name = input("What is your name brave explorer?  Please type your name and press enter.\n")
    print(f"It is nice to meet you {player_name}.  I wish you good luck on your journey.\n")
    party_member0 = input("I see you have another with you.  What is their name?\n") 
    party_member1 = input("You are joined by a third.  What should I call them?\n")
    party_member2 = input("Four people makes quite a crowd.  By what name is this person known?\n")
    party_member3 = input("Ah yes, the fifth and final member.  Give me their name please.\n")
    print(f"You are being joined by {party_member0}, {party_member1}, {party_member2}, and {party_member3}.\n")
    print("""
The Lewis and Clark expedition had many important job roles.  Each person had to do their share to ensure
that the trip went safely.  One of the most important roles was that of translator.  Lewis and Clark would
encounter many different native tribes along the journey.  Communicating with them was extremely important.
Other important roles included the cooks.  Eating healthy food was important to make sure that everyone was
strong enough to make the journey.  Trappers were also vital to the journey as they provided food to eat
and valuable animal pelts to trade for supplies.

What job would you like?
 -- Translator
 -- Cook
 -- Trapper
    """)
    starting_role = input("How would you like to contribute?  Type the job and press enter.\n")
    
    # Fix the following if/elif/else statements with starting_role == for each option. 
    if starting_role == "translator" or "Translator":
        print("You have chosen translator. You will receive the highest score bonus and starting money.\n")
        score_bonus = 1
        money = 1000
    elif starting_role == "trapper" or "Trapper":
        print("You have chosen trapper.  You will receive a good score bonus and more starting money.\n")
        score_bonus = 2
        money = 750
    elif starting_role == "cook" or "Cook":
        print("You have chosen cook.  You will receive the lowest bonus score and starting money.\n")
        score_bonus = 3
        money = 500
    else:
        print("You did not pick a job, so you will be a dishwasher.  You will receive no bonus and the least money.\n"
        score_bonus = 0
        money = 250
    
player_info() 
    




    
    












    
    
    
