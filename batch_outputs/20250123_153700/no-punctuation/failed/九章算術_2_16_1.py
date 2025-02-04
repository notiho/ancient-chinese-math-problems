"""
今有粟五斗五升欲為飧問得幾何
術曰以粟求飧九之五而一
荅曰為飧 a斗 
"""

"""
Suppose there are 5 dou and 5 sheng of millet. It is desired to turn it into cooked millet (food).
Question: how much cooked millet does it make?

The procedure says: when seeking cooked millet using millet, multiply by 9 and divide by 5.

The answer says: it makes *a* dou of cooked millet.
"""

# 粟五斗五升
粟斗 = 5
粟升 = 5

# Convert to sheng (1 dou = 10 sheng)
粟 = (粟斗 * 10) + 粟升

# 以粟求飧，九之
飧 = 9 * 粟

# 五而一
a = Fraction(飧, 5)

# Convert back to dou and sheng if needed
a斗 = a // 10  # Whole dou
a升 = a % 10   # Remaining sheng

a = f"{a斗}斗 {a升}升"  # Final result in dou and sheng
"""
Variable 'a' has wrong value. Expected: 99/10, Actual: 9斗 9升"""
