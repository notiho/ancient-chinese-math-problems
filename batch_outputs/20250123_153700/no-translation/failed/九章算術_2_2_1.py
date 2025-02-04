"""
今有粟四斗五升，欲為鑿米。問︰得幾何？
術曰：以粟求鑿米，十二之，二十五而一。
荅曰：為鑿米 a斗 。
"""

"""

"""


from fractions import Fraction

# 粟四斗五升
粟_斗 = 4
粟_升 = 5
# Convert 粟 to 升 (1斗 = 10升)
粟 = 粟_斗 * 10 + 粟_升

# 以粟求鑿米，十二之
鑿米 = 12 * 粟

# 二十五而一
a = Fraction(鑿米, 25)

# Convert result back to 斗 (1斗 = 10升)
a_斗 = a // 10  # Whole number of 斗
a_升 = a % 10   # Remaining 升


"""
 

`a_斗` represents the number of 斗, and `a_升` represents the remaining 升.
"""


"""
Variable 'a' has wrong value. Expected: 54/25, Actual: 108/5"""
