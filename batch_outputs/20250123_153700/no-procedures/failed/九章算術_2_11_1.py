"""
今有粟四斗一升、太半升，欲為答。問︰得幾何？
荅曰：為答 a斗 。
"""

"""
Suppose there is 4 dou, 1 sheng, and half a sheng of millet. It is desired to turn it into "da" (a processed form of millet).
Question: how much "da" does one obtain?

The answer says: it makes *a* dou of "da".
"""

# 粟四斗一升、太半升
粟 = 4 + Fraction(1, 10) + Fraction(1, 20)  # 1 dou = 10 sheng, so 1 sheng = 1/10 dou, and half a sheng = 1/20 dou

# Conversion rate: 3/5 of millet becomes "da"
a = Fraction(3, 5) * 粟

# Result
a
"""
Variable 'a' has wrong value. Expected: 15/4, Actual: 249/100"""
