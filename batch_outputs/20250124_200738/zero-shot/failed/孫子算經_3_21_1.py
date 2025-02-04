"""
今有六萬口，上口三萬人，日食九升；中口二萬人，日食七升；下口一萬人，日食五升。問：上、中、下口，共食幾何？
術曰：各置口數，以日食之數乘之，所得并之，即得。
答曰： a斛 。
"""

"""
To solve this problem, we will compute the total amount of food consumed by the three groups (上口, 中口, 下口) in one day. Each group's daily consumption is calculated by multiplying the number of people in the group by the amount of food consumed per person per day. Then, we sum these values to get the total daily consumption.

Here is the Python code:


"""

#----- content starts here -----

from fractions import Fraction

# Number of people in each group
upper_people = 30000  # 上口
middle_people = 20000  # 中口
lower_people = 10000  # 下口

# Daily food consumption per person in each group (in 升)
upper_food_per_person = 9  # 上口
middle_food_per_person = 7  # 中口
lower_food_per_person = 5  # 下口

# Total daily food consumption for each group
upper_total_food = upper_people * upper_food_per_person
middle_total_food = middle_people * middle_food_per_person
lower_total_food = lower_people * lower_food_per_person

# Total daily food consumption for all groups (in 升)
total_food_in_sheng = upper_total_food + middle_total_food + lower_total_food

# Convert the total food consumption to 斛 (1 斛 = 10 升)
a = Fraction(total_food_in_sheng, 10)

# The answer is stored in variable 'a' (in 斛)
#----- content ends here -----


"""


The solution is stored in the variable `a` as a `Fraction` representing the total daily food consumption in 斛.
"""


"""
Variable 'a' has wrong value. Expected: 4600, Actual: 46000"""
