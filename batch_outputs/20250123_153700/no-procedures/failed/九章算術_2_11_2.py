"""
今有粟四斗一升、太半升，欲為答。問︰得幾何？
荅曰：為答 a斗 。
"""

"""
Suppose there are 4 dou, 1 sheng, and half a sheng of millet. It is desired to convert it into da (a larger unit).
Question: how much da does it make?

Answer: it makes *a* dou.
"""

# 粟四斗一升、太半升
粟 = 4 + Fraction(1, 10) + Fraction(1, 20)  # 1 dou = 10 sheng, so 1 sheng = 1/10 dou, and half a sheng = 1/20 dou

# Convert to da (1 da = 10 dou)
a = Fraction(粟, 10)  # Divide the total millet by 10 to convert to da

a
"""
Variable 'a' has wrong value. Expected: 15/4, Actual: 83/200"""
