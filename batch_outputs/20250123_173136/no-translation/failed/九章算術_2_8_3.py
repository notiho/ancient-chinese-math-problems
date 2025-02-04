"""
今有粟八斗六升，欲為鑿飯。問︰得幾何？
術曰：以粟求鑿飯，二十四之，二十五而一。
荅曰：為鑿飯 a斗 。
"""


# 粟八斗六升
粟_斗 = 8
粟_升 = 6

# Convert 粟 to 升 (1斗 = 10升)
粟 = 10 * 粟_斗 + 粟_升

# 以粟求鑿飯，二十四之
鑿飯 = 24 * 粟

# 二十五而一
a = Fraction(鑿飯, 25)

# Convert result back to 斗
a_斗 = a // 10  # Whole 斗
a_升 = a % 10   # Remaining 升
a = f"{a_斗}斗 {a_升}升"
"""
Variable 'a' has wrong value. Expected: 1032/125, Actual: 8斗 64/25升"""
