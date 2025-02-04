"""
今有出錢五千七百八十五，買漆一斛六斗七升、太半升。欲斗率之，問︰斗幾何。
荅曰：一斗， a錢
"""

#----- content starts here -----
"""
Suppose there is 5785 qian spent to buy 1 hu, 6 dou, 7 sheng, and half a sheng of lacquer.
Question: what is the cost per dou?

Answer: 1 dou costs *a* qian.
"""

from fractions import Fraction

# 出錢五千七百八十五
total_money = 5785

# 買漆一斛六斗七升、太半升
# 1 斛 = 10 斗, 1 斗 = 10 升
total_volume_in_sheng = (1 * 10 * 10) + (6 * 10) + 7 + Fraction(1, 2)

# Convert total volume to dou
total_volume_in_dou = total_volume_in_sheng / 10

# Calculate cost per dou
a = Fraction(total_money, total_volume_in_dou)

a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 173550/503, Actual: 23140/67"""
