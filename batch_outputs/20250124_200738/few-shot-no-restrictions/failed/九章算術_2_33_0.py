"""
今有出錢五千七百八十五，買漆一斛六斗七升、太半升。欲斗率之，問︰斗幾何。
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一斗， a錢
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 5785 qian to buy 1 hu, 6 dou, 7 sheng, and half a sheng of lacquer.
It is desired to calculate the price per dou.
Question: how much is one dou?

The procedure says: Multiply the quantity sought (1 dou) by the total money spent to obtain the dividend.
Use the total quantity purchased as the divisor.
Divide the dividend by the divisor to obtain the price per dou.

Answer: one dou costs *a* qian.
"""

from fractions import Fraction

# 出錢五千七百八十五
錢數 = 5785

# 買漆一斛六斗七升、太半升
# 1 斛 = 10 斗, 1 斗 = 10 升
所買率 = 1 * 10 + 6 + 7 / 10 + Fraction(1, 2) / 10  # Convert to dou

# 以所求率 (1斗) 乘錢數為實
所求率 = 1  # 1 dou
實 = 所求率 * 錢數

# 以所買率為法
法 = 所買率

# 實如法得一
a = Fraction(實, 法)

# Output the result
a#----- content ends here -----

"""
Code error: both arguments should be Rational instances"""
