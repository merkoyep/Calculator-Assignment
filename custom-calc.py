# Homework: Your job is to make a custom calculator. 
# Your calculator should accept at least three values. 

# For example height, width, length

# It should print a prompt that makes it clear what 
# is being calculated. 

# For example: 
# Enter height, width, and length to calculate the area of a cube
# Height: 3
# Width: 4
# Length: 2

# After accepting input the calculator should perform 
# an accurate calculation and display the results in 
# a clear and well formatted message. 

# For example: A cube with a height of 3, width of 4, and length of 2 has an area of 24

# You can accept string input that becomes part of the descirption. 
# For example: Input units: inches

# Be sure to convert your numeric values to numbers before performing math operations!


print("""
      Welcome to Marco Airlines!
      Marco Airlines offers 3 complementary checked bags on each flight, totalling up to 100lbs.
      This tool will help you calculate your total baggage.
      """)

bag_1 = int(input("Please enter the weight in lbs of your first bag."))
bag_2 = int(input("Please enter the weight in lbs of your second bag."))
bag_3 = int(input("Please enter the weight in lbs of your final bag."))
sum_of_bags = bag_1 + bag_2 + bag_3


if sum_of_bags <= 100:
      print(f"Your bags weigh {sum_of_bags}lbs. You're all set to fly! We hope you enjoy your flight!")
else:
      print(f"Your bags weigh {sum_of_bags}lbs. Please pay for additional bags or adjust your bags acccordingly. We hope you enjoy your flight!")
