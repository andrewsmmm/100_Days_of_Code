print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')

name = input("What is your name? ")
print(f"Welcome to Treasure Island, {name}!")
print("Your mission is to find the treasure.")
choice_1 = input("You come to a fork in the road. "
                 "Do your want to go (type) left or right? ").lower()
if choice_1 == "left":
    choice_2 = input("You have come to a fast flowing river. "
                     "Do you wade across or wait for the ferryman? "
                     "Enter ferryman or wade: ").lower()

    if choice_2 == "ferryman":
        print("Sadly, the ferryman is death. GAME OVER!")
    elif choice_2 == "wade":
        print("You get washed downstream but end up on the other side of the river!")
        print("You walk on a little further and come to an old cottage with three "
              "coloured doors. One red, one yellow and one white. "
              "Which door do you choose? ")
        choice_3 = input("Enter red, yellow or white: ").lower()
        if choice_3 == "red":
            print("You are engulfed in fire. GAME OVER!")
        elif choice_3 == "yellow":
            print("You have woken the dragon and are eaten. GAME OVER!")
        elif choice_3 == "white":
            print("You have found the treasure! YOU WIN!")
        else:
            print("Invalid choice. GAME OVER!")


elif choice_1 == "right":
    choice_4 = input("You have come to a deep ravine. You can either climb down the rope or use the rickety bridge. "
                     "Enter climb or bridge: ").lower()
    if choice_4 == "climb":
        print("The rope snapped and you fall to your death. GAME OVER!")
    elif choice_4 == "bridge":
        print("You made it across the rickety bridge but only just. ")
        print("You have reached an old cottage with three coloured doors")
        choice_5 = input("One red, one yellow and one white. Which door do you choose? "
                         "Enter red, yellow or white: ").lower()
        if choice_5 == "red":
            print("You are engulfed in fire. GAME OVER!")
        elif choice_5 == "yellow":
            print("You have woken the dragon and are eaten. GAME OVER!")
        elif choice_5 == "white":
            print("You have found the treasure! YOU WIN!")
        else:
            print("Invalid choice. GAME OVER!")