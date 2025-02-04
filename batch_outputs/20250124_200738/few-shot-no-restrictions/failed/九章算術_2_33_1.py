"""
今有出錢五千七百八十五，買漆一斛六斗七升、太半升。欲斗率之，問︰斗幾何。
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一斗， a錢
"""

#----- content starts here -----
"""
Suppose 5785 qian (units of money) are spent to buy 1 hu, 6 dou, 7 sheng, and half a sheng of lacquer.
It is desired to calculate the price per dou (unit of volume).
Question: how much money per dou?

The procedure says: Multiply the desired rate (dou) by the total money spent to obtain the dividend.
Use the total volume purchased as the divisor.
Perform the division to obtain the price per dou.

Answer: 1 dou costs *a* qian.
"""

from fractions import Fraction

# 出錢五千七百八十五
錢數 = 5785

# 買漆一斛六斗七升、太半升
# 1 斛 = 10 斗, 1 斗 = 10 升
所買率 = 1 * 10 + 6 + 7 + Fraction(1, 2)  # Convert to total dou

# 以所求率乘錢數為實
實 = 錢數

# 以所買率為法
法 = 所買率

# 實如法得一
a = Fraction(實, 法)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 173550/503, Actual: 11570/47"""
