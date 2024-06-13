
"""
When you physically exercise to strengthen your heart, you
should maintain your heart rate within a range for at least 20
minutes. To find that range, subtract your age from 220. This
difference is your maximum heart rate per minute. Your heart
simply will not beat faster than this maximum (220 - age).
When exercising to strengthen your heart, you should keep your
heart rate between 65% and 85% of your heart’s maximum rate.
"""

""" Write a Python program named heart_rate.py that asks for a person’s age and computes and outputs the slowest and fastest rates necessary to strengthen his heart. To start your program, copy and paste the following code into your program and use it as an outline as you write code. Note that in a Python program, a triple quoted string at the top of the file acts as a comment for the entire program. """

#TODO
#*1python program heart_rate.py DONE
#*2ask the person's age DONE
#*3 computes and outputs the slowest and fastes rates DONE

age = int(input("What is your age? "))

max_heart_rate = 220 - age
low_heart_rate = (max_heart_rate * 0.65)
high_heart_rate = (max_heart_rate *0.85)

print(f"When you exercise to strengthen your heart,\nyou should keep your heart rate between {int(low_heart_rate)} and {int(high_heart_rate)} beats per minute.")
