"""
今有六萬口，上口三萬人，日食九升；中口二萬人，日食七升；下口一萬人，日食五升。問：上、中、下口，共食幾何？
術曰：各置口數，以日食之數乘之，所得并之，即得。
答曰： a(=4600)斛 。
"""

#----- content starts here -----
"""
Suppose there are 60,000 people in total. 
The upper group has 30,000 people, and each person eats 9 sheng per day.
The middle group has 20,000 people, and each person eats 7 sheng per day.
The lower group has 10,000 people, and each person eats 5 sheng per day.
Question: how much do the upper, middle, and lower groups eat in total?

The procedure says: Place the number of people in each group, multiply it by the amount each person eats per day, and sum the results. This gives the total.

Answer: *a*(=4600) hu.
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
上口總食 = 上口人數 * 上口日食
中口總食 = 中口人數 * 中口日食
下口總食 = 下口人數 * 下口日食

# 所得并之，即得
總食升 = 上口總食 + 中口總食 + 下口總食

# Convert 升 to 斛 (1 斛 = 10 升)
a = Fraction(總食升, 10) # 4600 斛#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4600, Actual: 46000"""
