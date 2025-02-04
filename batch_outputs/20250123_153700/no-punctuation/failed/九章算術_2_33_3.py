"""
今有出錢五千七百八十五買漆一斛六斗七升太半升欲斗率之問斗幾何
經術術曰以所求率乘錢數為實以所買率為法實如法得一
荅曰一斗 a錢
"""

"""
Suppose there is an expenditure of 5785 qian to buy 1 hu, 6 dou, 7 sheng, and 0.5 sheng of lacquer.
It is desired to calculate the cost per dou.
Question: how much is one dou?

The procedure says: Multiply the rate being sought by the amount of money spent to obtain the dividend.
Use the rate of what was purchased as the divisor.
Divide the dividend by the divisor to obtain the result.

Answer: one dou costs *a* qian.
"""

# 出錢五千七百八十五
錢數 = 5785

# 買漆一斛六斗七升太半升
# Convert the total amount to dou (1 hu = 10 dou, 1 dou = 10 sheng)
所買率 = 10 + 6 + Fraction(7.5, 10)  # 1 hu + 6 dou + 7.5 sheng

# 以所求率乘錢數為實
所求率 = 1  # We are calculating the cost per 1 dou
實 = 所求率 * 錢數

# 以所買率為法
法 = 所買率

# 實如法得一
a = Fraction(實, 法)  # Cost per dou in qian
"""
Code error: both arguments should be Rational instances"""
