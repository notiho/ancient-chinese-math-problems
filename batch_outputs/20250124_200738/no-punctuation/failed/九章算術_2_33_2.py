"""
今有出錢五千七百八十五買漆一斛六斗七升太半升欲斗率之問斗幾何
經術術曰以所求率乘錢數為實以所買率為法實如法得一
荅曰一斗 a錢
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 5785 qian to buy 1 hu, 6 dou, 7 sheng, and half a sheng of lacquer.
It is desired to calculate the price per dou.
Question: how much is one dou worth?

The procedure says: Multiply the desired rate (1 dou) by the total money spent to obtain the dividend.
Take the total amount purchased as the divisor.
Divide the dividend by the divisor to obtain the price per dou.

Answer: one dou is worth *a* qian.
"""

from fractions import Fraction

# 出錢五千七百八十五
錢數 = 5785

# 買漆一斛六斗七升太半升
# Convert the total amount purchased to dou
# 1 hu = 10 dou, 1 dou = 10 sheng
所買率 = 10 + 6 + Fraction(7, 10) + Fraction(1, 20)  # 1 hu + 6 dou + 7 sheng + 0.5 sheng

# 所求率為 1 斗
所求率 = 1

# 以所求率乘錢數為實
實 = 所求率 * 錢數

# 以所買率為法
法 = 所買率

# 實如法得一
a = Fraction(實, 法)  # Price per dou in qian#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 173550/503, Actual: 23140/67"""
