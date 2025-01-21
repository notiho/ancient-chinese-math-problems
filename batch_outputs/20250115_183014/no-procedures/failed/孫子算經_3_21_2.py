"""
今有六萬口，上口三萬人，日食九升；中口二萬人，日食七升；下口一萬人，日食五升。問：上、中、下口，共食幾何？
答曰： a斛 。
"""

"""
Suppose there are 60,000 people divided into three groups:
- The upper group (30,000 people) consumes 9 sheng per day per person.
- The middle group (20,000 people) consumes 7 sheng per day per person.
- The lower group (10,000 people) consumes 5 sheng per day per person.

Question: How much food do they consume in total per day?

Answer: *a* hu.
"""

# Define the number of people in each group
上口 = 30000
中口 = 20000
下口 = 10000

# Define the daily consumption per person in each group (in sheng)
上口日食 = 9
中口日食 = 7
下口日食 = 5

# Calculate total daily consumption for each group (in sheng)
上口總食 = 上口 * 上口日食
中口總食 = 中口 * 中口日食
下口總食 = 下口 * 下口日食

# Calculate total daily consumption for all groups (in sheng)
總食 = 上口總食 + 中口總食 + 下口總食

# Convert total consumption from sheng to hu (1 hu = 10 sheng)
a = Fraction(總食, 10)

# The total daily consumption in hu
a
"""
Variable 'a' has wrong value. Expected: 4600, Actual: 46000"""
