"""
今有六萬口，上口三萬人，日食九升；中口二萬人，日食七升；下口一萬人，日食五升。問：上、中、下口，共食幾何？
術曰：各置口數，以日食之數乘之，所得并之，即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 60,000 people in total. 
Among them, 30,000 are upper-class people, each consuming 9 sheng of food per day.
20,000 are middle-class people, each consuming 7 sheng of food per day.
10,000 are lower-class people, each consuming 5 sheng of food per day.
Question: How much food do the upper, middle, and lower classes consume in total?

The procedure says: Place the number of people in each class, multiply it by the daily consumption for that class, and sum the results to obtain the total.

Answer: *a* hu.
"""

# 上口三萬人，日食九升
上口人數 = 30000
上口日食 = 9  # 升

# 中口二萬人，日食七升
中口人數 = 20000
中口日食 = 7  # 升

# 下口一萬人，日食五升
下口人數 = 10000
下口日食 = 5  # 升

# 計算各類人口的總消耗
上口總消耗 = 上口人數 * 上口日食
中口總消耗 = 中口人數 * 中口日食
下口總消耗 = 下口人數 * 下口日食

# 總消耗（升）
總消耗升 = 上口總消耗 + 中口總消耗 + 下口總消耗

# 1 斛 = 10 升，將總消耗轉換為斛
a = Fraction(總消耗升, 10)  # 斛

a  # 答案以斛為單位#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4600, Actual: 46000"""
