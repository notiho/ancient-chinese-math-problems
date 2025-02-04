"""
今有出錢五千七百八十五，買漆一斛六斗七升、太半升。欲斗率之，問︰斗幾何。
荅曰：一斗， a錢
"""

#----- content starts here -----
"""
Suppose there is 5785 qian spent to buy 1 hu, 6 dou, 7 sheng, and half a sheng of lacquer.
Question: how much does 1 dou cost?

Answer: 1 dou costs *a* qian.
"""

from fractions import Fraction

# Total money spent
total_money = 5785

# Total lacquer purchased in dou
# 1 hu = 10 dou, 6 dou = 6 dou, 7 sheng = 7/10 dou, half a sheng = 1/20 dou
total_lacquer_in_dou = 10 + 6 + Fraction(7, 10) + Fraction(1, 20)

# Cost per dou
a = Fraction(total_money, total_lacquer_in_dou)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 173550/503, Actual: 23140/67"""
