"""
今有六萬口，上口三萬人，日食九升；中口二萬人，日食七升；下口一萬人，日食五升。問：上、中、下口，共食幾何？
術曰：各置口數，以日食之數乘之，所得并之，即得。
答曰： a斛 。
"""

"""
To solve this problem, we will calculate the total amount of food consumed by the three groups (上口, 中口, 下口) in one day. Each group's daily consumption is determined by multiplying the number of people in the group by their respective daily consumption rate. The total consumption is the sum of these values.

Here is the Python code:


"""


from fractions import Fraction

# Number of people in each group
upper_people = 30000  # 上口
middle_people = 20000  # 中口
lower_people = 10000  # 下口

# Daily consumption per person in each group (in 升)
upper_consumption = 9  # 上口日食
middle_consumption = 7  # 中口日食
lower_consumption = 5  # 下口日食

# Calculate total consumption for each group
upper_total = upper_people * upper_consumption
middle_total = middle_people * middle_consumption
lower_total = lower_people * lower_consumption

# Calculate the total consumption for all groups
total_consumption = upper_total + middle_total + lower_total

# Convert to 斛 (1 斛 = 10 升)
a = Fraction(total_consumption, 10)

# The answer is stored in variable 'a'


"""


The solution is stored in the variable `a`, which represents the total daily consumption in 斛.
"""


"""
Variable 'a' has wrong value. Expected: 4600, Actual: 46000"""
