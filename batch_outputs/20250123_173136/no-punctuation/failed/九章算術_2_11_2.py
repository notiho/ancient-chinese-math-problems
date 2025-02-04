"""
今有粟四斗一升太半升欲為答問得幾何
術曰以粟求菽答麻麥皆九之十而一
荅曰為答 a斗 
"""

"""
Suppose there are 4 dou, 1 sheng, and 0.5 sheng of millet. It is desired to convert it into da (a type of grain).
Question: how much da is obtained?

The procedure says: When seeking da, beans, hemp, or wheat from millet, multiply by 9 and divide by 10.

The answer says: it makes *a* dou of da.
"""

# 粟四斗一升太半升
粟 = 4 * 10 + 1 + Fraction(1, 2)  # Convert everything to sheng (1 dou = 10 sheng)

# 以粟求答，九之
答 = 9 * 粟

# 十而一
答 = Fraction(答, 10)

# Convert back to dou
a = Fraction(答, 10)  # Convert sheng to dou (1 dou = 10 sheng)
"""
Variable 'a' has wrong value. Expected: 15/4, Actual: 747/200"""
