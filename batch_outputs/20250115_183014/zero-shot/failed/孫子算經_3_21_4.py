"""
今有六萬口，上口三萬人，日食九升；中口二萬人，日食七升；下口一萬人，日食五升。問：上、中、下口，共食幾何？
術曰：各置口數，以日食之數乘之，所得并之，即得。
答曰： a斛 。
"""

"""
To solve this problem, we calculate the total food consumption for each group (上口, 中口, 下口) by multiplying the number of people in each group by their daily food consumption. Then, we sum up the results to get the total food consumption.

Here is the Python code:


"""


from fractions import Fraction

# Number of people in each group
upper_people = 30000  # 上口
middle_people = 20000  # 中口
lower_people = 10000  # 下口

# Daily food consumption per person in each group (in 升)
upper_food_per_person = 9  # 上口
middle_food_per_person = 7  # 中口
lower_food_per_person = 5  # 下口

# Total food consumption for each group
upper_total_food = upper_people * upper_food_per_person
middle_total_food = middle_people * middle_food_per_person
lower_total_food = lower_people * lower_food_per_person

# Total food consumption for all groups
a = upper_total_food + middle_total_food + lower_total_food  # in 升

# Convert to 斛 (1 斛 = 10 升)
a = Fraction(a, 10)  # in 斛

# Result
a


"""


The variable `a` will contain the total food consumption in 斛.
"""


"""
Variable 'a' has wrong value. Expected: 4600, Actual: 46000"""
