"""
今有六萬口，上口三萬人，日食九升；中口二萬人，日食七升；下口一萬人，日食五升。問：上、中、下口，共食幾何？
術曰：各置口數，以日食之數乘之，所得并之，即得。
答曰： a斛 。
"""

"""
Suppose there are 60,000 people in total. 
Among them, 30,000 are upper-class people, each consuming 9 sheng of food per day; 
20,000 are middle-class people, each consuming 7 sheng of food per day; 
and 10,000 are lower-class people, each consuming 5 sheng of food per day.
Question: how much food do the upper, middle, and lower classes consume in total?

The procedure says: Place the number of people in each class, and multiply it by the amount of food consumed per day for that class. 
Add the results together, and the total is obtained.

Answer: *a* hu.
"""

# 上口三萬人，日食九升
上口人數 = 30000
上口日食 = 9

# 中口二萬人，日食七升
中口人數 = 20000
中口日食 = 7

# 下口一萬人，日食五升
下口人數 = 10000
下口日食 = 5

# 各置口數，以日食之數乘之
上口食量 = 上口人數 * 上口日食
中口食量 = 中口人數 * 中口日食
下口食量 = 下口人數 * 下口日食

# 所得并之，即得
總食量升 = 上口食量 + 中口食量 + 下口食量

# Convert sheng to hu (10 sheng = 1 hu)
#ERR: unit conversion
#a = Fraction(總食量升, 10)  # Total food in hu
a = Fraction(總食量升, 100)  # Total food in hu
"""
Variable 'a' has wrong value. Expected: 4600, Actual: 46000"""
