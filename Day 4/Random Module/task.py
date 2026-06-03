"""Heads or tails program"""
import random

# rand_num = random.randint(0, 1)
# if rand_num == 1:
#     print("Heads")
# else:
#     print("Tails")

# generating randon floating numbers and adding them to a list
# numbers = []
# while len(numbers)<=10:
#     rand_num_2 = random.uniform(0, 10)
#     numbers.append(rand_num_2)
# print(numbers)

#program to count coin flips based on a pseudo random number generator
# heads_tails = []
# while len(heads_tails)<=10_000_000:
#     rand_num_3 = random.randint(0, 1)
#     heads_tails.append(rand_num_3)
# print(f"Heads count= {heads_tails.count(0)}")
# print(f"Tails count= {heads_tails.count(1)}")

# clocked at 14s

#note Co-Pilot suggested a for loop, which is much more elegant
heads = 0
tails = 0

for _ in range(10_000):
    if random.randint(0, 1) == 0:
        heads += 1
    else:
        tails += 1

print(f"Heads count = {heads}")
print(f"Tails count = {tails}")
# clocked at 13s

# if 2019 - 1991 > 25:
#     year_since_python = 2019 - 1991
#     print(f"Python is {year_since_python} years old - very mature ")

# with walrus operation
if (years_since_python := 2019 - 1991) > 21:
    print(f"Python is {years_since_python} years old - very mature")

#riffing on the walrus operation
year_1 = int(input("Enter value for first year: "))
year_2 = int(input("Enter value for second year: "))
if (years_since_python := (int(year_1)) - (int(year_2))) > 21:
    print(f"Python is {years_since_python} years old")
else:
    print(f"Python is {years_since_python} years old")



