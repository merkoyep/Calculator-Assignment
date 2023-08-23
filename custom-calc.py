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
      Marco Airlines offers 3 complementary checked bags on each flight, totalling up to 100lbs].
      We charge an additional $2.00CAD per lbs over 100.
      This tool will help you calculate your total baggage fees.
      """)

intro_msg = "Please enter the weight to the nearest lb of your "
bag_1 = int(input(f"{intro_msg}first bag."))
bag_2 = int(input(f"{intro_msg}second bag."))
bag_3 = int(input(f"{intro_msg}final bag."))

# end of User Input

def bag_total(bag_1, bag_2, bag_3):
      solution = bag_1 + bag_2 + bag_3
      return solution

sum_of_bags = bag_total(bag_1, bag_2, bag_3)
total_overweight = sum_of_bags - 100
bag_total_msg=f"Your bags weigh {bag_1}lb, {bag_2}lb, and {bag_3}lb. This adds to a total of {sum_of_bags}lbs."

def bag_fee(sum_of_bags):
      fee = (sum_of_bags - 100) * 2
      return fee

if total_overweight <= 0:
      print(f"""
          {bag_total_msg} 
            You're all set to fly! We hope you enjoy your flight!""")
else:
      print(f"""
            {bag_total_msg} 
            This is {total_overweight}lb overweight.
            Marco Airlines charges $2.00CAD for each lb over 100lb. Your total fee due today is ${bag_fee(sum_of_bags)}.00CAD.
            Please pay this fee online before check-in. Paying during or after check-in will incurr an additional $10.00CAD customer service fee.""")
