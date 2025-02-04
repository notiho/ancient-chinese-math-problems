"""
今有六萬口，上口三萬人，日食九升；中口二萬人，日食七升；下口一萬人，日食五升。問：上、中、下口，共食幾何？
術曰：各置口數，以日食之數乘之，所得并之，即得。
答曰： a斛 。
"""

#----- content starts here -----
"""
Suppose there are 60,000 people in total. 
Among them, 30,000 are upper-class people, and they consume 9 sheng of food per day.
20,000 are middle-class people, and they consume 7 sheng of food per day.
10,000 are lower-class people, and they consume 5 sheng of food per day.
Question: how much food do they consume in total?

The procedure says: Place the number of people in each class, and multiply it by the amount of food consumed per day for that class.
Add the results together, and the total is obtained.

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

# 各置口數，以日食之數乘之
上口總食 = 上口人數 * 上口日食
中口總食 = 中口人數 * 中口日食
下口總食 = 下口人數 * 下口日食

# 所得并之，即得
總食升 = 上口總食 + 中口總食 + 下口總食

# Convert 升 to 斛 (1 斛 = 10 升)
a = Fraction(總食升, 10)  # 斛

a  # Output the total food consumption in hu.#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 4600, Actual: 46000"""
