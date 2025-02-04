"""
今有出錢五千七百八十五，買漆一斛六斗七升、太半升。欲斗率之，問︰斗幾何。
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一斗， a錢
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 5785 qian to buy 1 hu, 6 dou, 7 sheng, and 0.5 sheng of lacquer.
It is desired to calculate the cost per dou.
Question: how much is the cost per dou?

The procedure says: Multiply the amount of money by the unit being sought (dou) to obtain the dividend.
Take the total amount purchased as the divisor.
Divide the dividend by the divisor to obtain the cost per dou.

Answer: 1 dou costs *a* qian.
"""

from fractions import Fraction

# 出錢五千七百八十五
錢數 = 5785

# 買漆一斛六斗七升、太半升
# Convert everything to dou (1 hu = 10 dou, 1 dou = 10 sheng)
所買率 = 1 * 10 + 6 + Fraction(7.5, 10)  # 1 hu + 6 dou + 7.5 sheng

# 以所求率乘錢數為實
實 = 錢數

# 以所買率為法
法 = 所買率

# 實如法得一
a = Fraction(實, 法)

# Output the result
a#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
