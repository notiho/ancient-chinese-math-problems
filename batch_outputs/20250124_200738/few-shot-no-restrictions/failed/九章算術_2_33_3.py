"""
今有出錢五千七百八十五，買漆一斛六斗七升、太半升。欲斗率之，問︰斗幾何。
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一斗， a錢
"""

#----- content starts here -----
"""
Suppose there is 5785 qian spent to buy 1 hu, 6 dou, 7 sheng, and half a sheng of lacquer.
It is desired to calculate the price per dou.
Question: how much is one dou?

The procedure says: Multiply the quantity sought (1 dou) by the total amount of money spent to obtain the dividend.
Use the total quantity purchased as the divisor.
Divide the dividend by the divisor to obtain the price per dou.

Answer: one dou costs *a* qian.
"""

from fractions import Fraction

# 出錢五千七百八十五
錢數 = 5785

# 買漆一斛六斗七升、太半升
# 1 斛 = 10 斗, 1 斗 = 10 升
所買率 = 1 * 10 + 6 + Fraction(7, 10) + Fraction(1, 20)  # Convert to dou

# 以所求率乘錢數為實
實 = 1 * 錢數  # 所求率 is 1 dou

# 實如法得一
a = Fraction(實, 所買率)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 173550/503, Actual: 23140/67"""
