print("Welcome to Python Pizza Deliveries!")
bill = 0
size = input("What size pizza do you want? S, M or L: ").lower()
if size == "s":
    bill += 15
elif size == "m":
    bill += 20
elif size == "l":
    bill += 25
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").lower()
if pepperoni == "y":
    if size == "s":
        bill += 2
    else:
        bill += 3
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()
if extra_cheese == "y":
    bill += 1

print(f"Your final bill is: ${bill}.")

#Really please with how this turned out - seemed to understand it better
#than a year ago. Really simplified the code this time around.

#todo: work out how much they need to pay on their size choice

#todo: work out how much to add to their bill based on their peperoni choice

#todo: work out their final amount based on whether if they want extra cheese.


