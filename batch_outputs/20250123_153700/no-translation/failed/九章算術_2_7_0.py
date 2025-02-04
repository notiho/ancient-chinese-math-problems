"""
今有粟三斗六升，欲為粺飯。問︰得幾何？
術曰：以粟求粺飯，二十七之，二十五而一。
荅曰：為粺飯 a斗 。
"""

"""

"""


# 粟三斗六升
粟斗 = 3
粟升 = 6

# Convert 粟 to 升 (1斗 = 10升)
粟 = 10 * 粟斗 + 粟升

# 以粟求粺飯，二十七之
粺飯 = 27 * 粟

# 二十五而一
a = Fraction(粺飯, 25)

# Convert result back to 斗 (if needed)
粺飯斗 = a // 10  # Whole 斗
粺飯升 = a % 10   # Remaining 升


"""

"""


"""
Variable 'a' has wrong value. Expected: 486/125, Actual: 972/25"""
