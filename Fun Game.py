import random
import time

condition = True
contestants = {}
contestants_list = []
random_contestant_list = [0, 1, 2, 3 ,4]
while condition == True:
    print("""
    Welcome to the Hunger Games Simulator!

    0 - Exit
    1 - Enter your contestants
    2 - Play the damn game

    """)
    menu_choice = (input("Enter a menu option: "))
    if menu_choice == "0":
        input("Press enter to exit. ")
        condition == False
        break
    elif menu_choice == "1":
        while len(contestants) != 5:
            print(contestants)
            contestant_add = input("\nWhat is the name of your contestant?")
            if contestant_add not in contestants:
                contestant_district = input("Where is your contestant from?")
                contestants[contestant_add] = contestant_district
                contestants_list += contestant_add
                print("\n", contestant_add, " has been added.")
    elif menu_choice == "2":
        if len(contestants) != 5:
            print("You cannot start the game without five contestants, kiddo. ")
            input("Press enter to return to the menu. ")
            continue
        elif len(conestants) == 5:
            random_contestant_number = random.choice(random_contestant_list)
            random_contestant_list.remove(random_contestant_number)
            random_contestant = contestants_list[random_contestant_number]
            random_contestant_number = a

            random_contestant_number_1 = random.choice(random_contestant_list)
            random_contestant_list.remove(random_contestant_number)
            random_contestant = contestants_list[random_contestant_number]
            random_contestant_number_1 = b

            random_contestant_number_2 = random.choice(random_contestant_list)
            random_contestant_list.remove(random_contestant_number)
            random_contestant = contestants_list[random_contestant_number]
            random_contestant_number_2 = c

            random_contestant_number_3 = random.choice(random_contestant_list)
            random_contestant_list.remove(random_contestant_number)
            random_contestant = contestants_list[random_contestant_number]
            random_contestant_number_3 = d

            random_contestant_number_4 = random.choice(random_contestant_list)
            random_contestant_list.remove(random_contestant_number)
            random_contestant = contestants_list[random_contestant_number]
            random_contestant_number_4 = e

            print(a, " runs to the cornucopia and gets a dad", "\n", b, " instantly dies due to hylophobia (fear of trees). ", "\n", c, " runs to the cornucopia and finds their long lost pet 'Grant' the Croissant", "\n", d, " runs into the forest screaming 'REEEEE IM PICKLE RICK REEEEE", "\n", e, " runs to the cornucopia and eats a grenade, hoping it was a Chom Chom. ", e, " dies.")

            print(a, "'s dad kills them with a trebuchet.", "\n", c, " bumps into Dwayne 'The Rock Hard' Johnson and rides him as if he were cavalry.", "\n", d, " crawls on the floor and continues to scream 'REEEEE IM PICKLE RICK REEEEE")

            print(c, " and ", d, " get into a massive tickle fight but Dwayne 'The Rock Hard' Johnson kills them both and wins the hunger games.")
            time.sleep(5)
            print("Congratulations Dwayne!")

