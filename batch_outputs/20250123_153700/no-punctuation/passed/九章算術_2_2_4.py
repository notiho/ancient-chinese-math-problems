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
粟 = (粟斗 * 10) + 粟升

# 以粟求鑿米，十二之
鑿米 = 12 * 粟

# 二十五而一
鑿米 = Fraction(鑿米, 25)

# Convert back to 斗 (1 斗 = 10 升)
a斗 = 鑿米 // 10  # Whole dou
a升 = 鑿米 % 10   # Remaining sheng

a = Fraction(a斗) + Fraction(a升, 10)  # Final result in dou

"""
"""
