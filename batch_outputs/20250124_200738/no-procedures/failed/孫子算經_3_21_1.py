"""
今有六萬口，上口三萬人，日食九升；中口二萬人，日食七升；下口一萬人，日食五升。問：上、中、下口，共食幾何？
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 60,000 people divided into three groups:
- The upper group has 30,000 people, and each person consumes 9 sheng per day.
- The middle group has 20,000 people, and each person consumes 7 sheng per day.
- The lower group has 10,000 people, and each person consumes 5 sheng per day.

Question: How much food do the upper, middle, and lower groups consume in total per day?

Answer: *a* hu.
"""

# Define the number of people and daily consumption per person for each group
上口_人數 = 30000
上口_日食 = 9  # sheng per person

中口_人數 = 20000
中口_日食 = 7  # sheng per person

下口_人數 = 10000
下口_日食 = 5  # sheng per person

# Calculate total consumption for each group in sheng
上口_總食 = 上口_人數 * 上口_日食
中口_總食 = 中口_人數 * 中口_日食
下口_總食 = 下口_人數 * 下口_日食

# Total consumption in sheng
總食_升 = 上口_總食 + 中口_總食 + 下口_總食

# Convert sheng to hu (1 hu = 10 sheng)
a = Fraction(總食_升, 10)  # Total consumption in hu

a  # Output the total consumption in hu#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4600, Actual: 46000"""
