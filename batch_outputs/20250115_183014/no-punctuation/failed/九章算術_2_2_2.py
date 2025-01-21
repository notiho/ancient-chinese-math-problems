"""
今有粟四斗五升欲為鑿米問得幾何
術曰以粟求鑿米十二之二十五而一
荅曰為鑿米 a斗 
"""

"""
Suppose there are 4 dou and 5 sheng of unhusked millet. It is desired to turn it into polished millet.
Question: how much polished millet does one obtain?

The procedure says: when seeking polished millet from unhusked millet, multiply by 12 and divide by 25.

The answer says: it makes *a* dou of polished millet.
"""

# 粟四斗五升
粟斗 = 4
粟升 = 5

# Convert everything to 升 (1 斗 = 10 升)
粟 = 10 * 粟斗 + 粟升

# 以粟求鑿米，十二之
鑿米 = 12 * 粟

# 二十五而一
a = Fraction(鑿米, 25)

# Convert back to 斗 if needed
a斗 = a // 10  # Whole dou
a升 = a % 10   # Remaining sheng
a = f"{a斗}斗 {a升}升" if a升 != 0 else f"{a斗}斗"
"""
Variable 'a' has wrong value. Expected: 54/25, Actual: 2斗 8/5升"""
