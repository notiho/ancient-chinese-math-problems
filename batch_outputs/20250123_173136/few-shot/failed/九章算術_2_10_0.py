"""
今有粟三斗少半升，欲為菽。問︰得幾何？
術曰：以粟求菽、答、麻、麥，皆九之，十而一。
荅曰：為菽 a斗 。
"""

"""
Suppose there are 3 dou and half a sheng of millet. It is desired to convert it into beans.
Question: how much does one obtain?

The procedure says: When seeking beans, da, hemp, or wheat from millet, multiply by 9 and divide by 10.

The answer says: it makes *a* dou of beans.
"""

# 粟三斗少半升
粟 = 3 + Fraction(1, 20)  # 1 dou = 10 sheng, so half a sheng = 1/20 dou

# 以粟求菽，九之
菽 = 9 * 粟

# 十而一
a = Fraction(菽, 10)
"""
Variable 'a' has wrong value. Expected: 273/100, Actual: 549/200"""
