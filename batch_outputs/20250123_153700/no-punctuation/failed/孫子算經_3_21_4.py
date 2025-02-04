"""
今有六萬口上口三萬人日食九升中口二萬人日食七升下口一萬人日食五升問上中下口共食幾何
術曰各置口數以日食之數乘之所得并之即得
答曰 a斛 
"""

"""
Suppose there are 60,000 people:
- 30,000 upper-class people, each consuming 9 sheng of grain per day.
- 20,000 middle-class people, each consuming 7 sheng of grain per day.
- 10,000 lower-class people, each consuming 5 sheng of grain per day.
Question: how much grain do they consume in total?

The procedure says: Place the number of people for each class.
Multiply it by the daily consumption for that class.
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
上口總食 = 上口人數 * 上口日食
中口總食 = 中口人數 * 中口日食
下口總食 = 下口人數 * 下口日食

# 所得并之，即得
總食升 = 上口總食 + 中口總食 + 下口總食

# Convert 升 to 斛 (1 斛 = 10 升)
a = Fraction(總食升, 10)  # Total in hu
"""
Variable 'a' has wrong value. Expected: 4600, Actual: 46000"""
