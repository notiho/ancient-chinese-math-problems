"""
今有六萬口，上口三萬人，日食九升；中口二萬人，日食七升；下口一萬人，日食五升。問：上、中、下口，共食幾何？
術曰：各置口數，以日食之數乘之，所得并之，即得。
答曰： a斛 。
"""

"""
To solve this problem, we need to calculate the total amount of food consumed by the three groups (上口, 中口, 下口) in one day. Here's the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Number of people in each group
upper_people = 30000
middle_people = 20000
lower_people = 10000

# Daily food consumption per person in each group (in 升)
upper_food_per_person = 9
middle_food_per_person = 7
lower_food_per_person = 5

# Total food consumption for each group
upper_total_food = upper_people * upper_food_per_person
middle_total_food = middle_people * middle_food_per_person
lower_total_food = lower_people * lower_food_per_person

# Total food consumption for all groups
a = Fraction(upper_total_food + middle_total_food + lower_total_food, 10)  # Convert to 斛 (1 斛 = 10 升)

# The answer is stored in variable 'a'
#----- content ends here -----


"""


### Explanation:
1. Each group has a specific number of people and a daily food consumption rate (in 升 per person).
2. Multiply the number of people in each group by their respective daily food consumption rate to get the total food consumption for that group (in 升).
3. Add the total food consumption of all groups together.
4. Convert the total from 升 to 斛 by dividing by 10 (since 1 斛 = 10 升).
5. The result is stored in the variable `a`, which represents the total food consumption in 斛.
"""


"""
Variable 'a' has wrong value. Expected: 4600, Actual: 46000"""
