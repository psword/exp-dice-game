# import randomization with the random module
from itertools import count
import random

#intialize the variables with 0
die1_1 = 0
die2_1 = 0
die3_1 = 0
die1_2 = 0
die2_2 = 0
die3_2 = 0
die1_3 = 0
die2_3 = 0
die3_3 = 0
die_max = 6
die_min = 1


# Let's notify the player of what is about to happen:
input("Hi Player1, we are going to roll the dice 3 times.  We will randomize and give you your roll statistics.  Press the Enter key!\n")

# Since this is only three rolls, I am not going to use a loop.  
# For many rolls, I would integrate a loop.
# Or, I would choose to implement a function, or class.
# First roll
die1_1 = random.randint(die_min,die_max)
print("This is the value of Die 1, the first roll:",die1_1,"\n")
die2_1 = random.randint(die_min,die_max)
print("This is the value of Die 2, the first roll: ",die2_1,"\n")
die3_1 = random.randint(die_min,die_max)
print("This is the value of Die 3, the first roll: ",die3_1,"\n")
print("----------------------------")
input("Press the Enter key to continue!\n")

# Second roll
die1_2 = random.randint(die_min,die_max)
print("This is the value of Die 1, the second roll: ",die1_2,"\n")
die2_2 = random.randint(die_min,die_max)
print("This is the value of Die 2, the second roll: ",die2_2,"\n")
die3_2 = random.randint(die_min,die_max)
print("This is the value of Die 3, the second roll: ",die3_2,"\n")
print("----------------------------")
input("Press the Enter key to continue!\n")

# Third roll
die1_3 = random.randint(die_min,die_max)
print("This is the value of Die 1, the third roll: ",die1_3,"\n")
die2_3 = random.randint(die_min,die_max)
print("This is the value of Die 2, the third roll: ",die2_3,"\n")
die3_3 = random.randint(die_min,die_max)
print("This is the value of Die 3, the third roll: ",die3_3,"\n")
print("----------------------------")
input("Press the Enter key to continue!")

# Let's find our statistics
# Sum of first roll
sum_1 = die1_1 + die2_1 + die3_1
print("----------------------------")
print("Here is the first set of stats!\n")
print("The sum of the first roll is: ",sum_1)

# Sum of second roll
sum_2 = die1_2 + die2_2 + die3_2
print("----------------------------")
print("The sum of the second roll is: ",sum_2)

# Sum of third roll
sum_3 = die1_3 + die2_3 + die3_3
print("----------------------------")
print("The sum of the third roll is: ",sum_3)
print("----------------------------")

# Print the greatest roll sum
if sum_1 > sum_2 and sum_1 > sum_3:
    print("The first roll was the largest with: ", sum_1,"\n")
elif sum_2 > sum_1 and sum_2 > sum_3:
    print("The second roll was the largest with: ", sum_2,"\n")
elif sum_3 > sum_1 and sum_3 > sum_2:
    print("The third roll was the largest with: ", sum_3,"\n")
input("This is the first set, press the Enter key to continue!\n")
print("----------------------------")

# Acting on the second roll for the second set of statistics
# Take the max of the list
print("Here is the second set of stats!\n")
list_second_roll = [die1_2, die2_2, die3_2]

# Here is the max value of the second roll

print("The max value of the second dice roll is: ",max(list_second_roll),"\n")
print("----------------------------")
# How many times did the max number occur?
# Define a function to count the second roll
def count_list2(list_second_roll,i):
    count = 0
    for element in list_second_roll:
        if (element == i):
            count = count + 1
    return count

# Driver Code for the count
i = max(list_second_roll)
print('{} has occurred {} times in the second roll!'.format(i,count_list2(list_second_roll, i)),"\n")
input("This is the second set, press the Enter key to continue!\n")
print("----------------------------")

# Acting on the third roll for the third set of statistics
# Take the min of the list
print("Here is the third set of stats!\n")
list_third_roll = [die1_3, die2_3, die3_3]

# Here is the min value of the third roll

print("The min value of the third dice roll is: ",min(list_third_roll),"\n")
print("----------------------------")
# How many times did the max number occur?
# Define a function to count the second roll
def count_list3(list_third_roll,i):
    count = 0
    for element in list_third_roll:
        if (element == i):
            count = count + 1
    return count

# Driver Code for the count
i = min(list_third_roll)
print('{} has occurred {} times in the third roll!'.format(i,count_list3(list_third_roll, i)),"\n")
input("This is the third set, press the Enter key to continue!\n")
print("----------------------------")

# List all rolls
print("Here is the final set of stats!\n")
list_all_rolls = [die1_1, die1_2, die1_3, die2_1, die2_2, die2_3, die3_1, die3_2, die3_3]

# Define a function to count all rolls
# Take the max and min values
def count_list_all(list_all_rolls,i):
    count = 0
    for element in list_all_rolls:
        if (element == i):
            count = count + 1
    return count

# Driver Code for the count
i = max(list_all_rolls)

# Print the maximum
print("The max value of all the rolls is: ",max(list_all_rolls),"\n")
print('{} has occurred {} times out of all the rolls!'.format(i,count_list_all(list_all_rolls, i)),"\n")
# Driver Code for the count
i = min(list_all_rolls)

# Print the minimum
print("The min value of all the rolls is: ",min(list_all_rolls),"\n")
print('{} has occurred {} times out of all the rolls!'.format(i,count_list_all(list_all_rolls, i)),"\n")
input("This is the fourth set, press the Enter key to end the program, and thanks for playing!\n")
print("----------------------------")
