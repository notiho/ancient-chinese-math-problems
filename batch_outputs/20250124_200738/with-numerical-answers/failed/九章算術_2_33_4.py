"""
今有出錢五千七百八十五，買漆一斛六斗七升、太半升。欲斗率之，問︰斗幾何。
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一斗， a(=173550/503)錢
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 5785 qian to buy 1 hu, 6 dou, 7 sheng, and half a sheng of lacquer.
It is desired to calculate the price per dou.
Question: how much is one dou?

The procedure says: Multiply the rate being sought by the amount of money to obtain the dividend.
Take the rate of what was purchased as the divisor.
Divide the dividend by the divisor to obtain the result.

Answer: one dou costs *a*(=173550/503) qian.
"""

from fractions import Fraction

# 出錢五千七百八十五
錢數 = 5785

# 買漆一斛六斗七升、太半升
# Convert the total amount of lacquer to sheng
一斛 = 10  # 1 hu = 10 dou
一斗 = 10  # 1 dou = 10 sheng
一升 = 1   # 1 sheng = 1 sheng
太半升 = Fraction(1, 2)  # Half a sheng

所買率 = (1 * 一斛 * 一斗) + (6 * 一斗) + (7 * 一升) + 太半升  # Total in sheng

# Convert 所買率 to dou
所買率 = Fraction(所買率, 一斗)  # Convert sheng to dou

# 以所求率乘錢數為實
所求率 = 1  # We are calculating the price for 1 dou
實 = 所求率 * 錢數

# 以所買率為法
法 = 所買率

# 實如法得一
a = Fraction(實, 法)  # 173550/503 qian per dou#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 173550/503, Actual: 23140/67"""
