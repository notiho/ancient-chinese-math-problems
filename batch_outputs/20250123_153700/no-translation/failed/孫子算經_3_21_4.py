"""
今有六萬口，上口三萬人，日食九升；中口二萬人，日食七升；下口一萬人，日食五升。問：上、中、下口，共食幾何？
術曰：各置口數，以日食之數乘之，所得并之，即得。
答曰： a斛 。
"""

"""

"""


# 上口三萬人，日食九升
上口數 = 30000
上口日食 = 9

# 中口二萬人，日食七升
中口數 = 20000
中口日食 = 7

# 下口一萬人，日食五升
下口數 = 10000
下口日食 = 5

# 各置口數，以日食之數乘之
上口食 = 上口數 * 上口日食
中口食 = 中口數 * 中口日食
下口食 = 下口數 * 下口日食

# 所得并之，即得
總日食升 = 上口食 + 中口食 + 下口食

# Convert 升 to 斛 (10 升 = 1 斛)
a = Fraction(總日食升, 10)


"""

"""


"""
Variable 'a' has wrong value. Expected: 4600, Actual: 46000"""
