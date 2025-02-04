"""
今有六萬口，上口三萬人，日食九升；中口二萬人，日食七升；下口一萬人，日食五升。問：上、中、下口，共食幾何？
術曰：各置口數，以日食之數乘之，所得并之，即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 60,000 people in total. Among them:
- 30,000 are upper-class people, and each consumes 9 sheng of food daily.
- 20,000 are middle-class people, and each consumes 7 sheng of food daily.
- 10,000 are lower-class people, and each consumes 5 sheng of food daily.

Question: How much food do the upper, middle, and lower classes consume in total?

The procedure says: For each group, multiply the number of people by their daily food consumption. Add the results together to obtain the total.

Answer: *a* hu.
"""

# Define the number of people in each class
上口 = 30000
中口 = 20000
下口 = 10000

# Define the daily food consumption for each class (in sheng)
上口日食 = 9
中口日食 = 7
下口日食 = 5

# Calculate the total food consumption for each class
上口總食 = 上口 * 上口日食
中口總食 = 中口 * 中口日食
下口總食 = 下口 * 下口日食

# Add the total food consumption for all classes
總食 = 上口總食 + 中口總食 + 下口總食

# Convert sheng to hu (1 hu = 10 sheng)
a = Fraction(總食, 10)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4600, Actual: 46000"""
