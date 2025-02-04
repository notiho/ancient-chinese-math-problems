"""
今有粟五斗太半升欲為麻問得幾何
術曰以粟求菽答麻麥皆九之十而一
荅曰為麻 a斗 
"""

"""
Suppose there are 5 dou and half a sheng of millet. It is desired to convert it into hemp.
Question: how much hemp does it make?

The procedure says: When seeking beans, hemp, or wheat from millet, multiply by 9 and divide by 10.

The answer says: it makes *a* dou of hemp.
"""

# 粟五斗太半升
粟 = 5 + Fraction(1, 20)  # 1 dou = 10 sheng, so half a sheng = 1/20 dou

# 以粟求麻，九之
麻 = 9 * 粟

# 十而一
a = Fraction(麻, 10)
"""
Variable 'a' has wrong value. Expected: 114/25, Actual: 909/200"""
