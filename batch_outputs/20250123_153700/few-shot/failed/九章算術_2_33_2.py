"""
今有出錢五千七百八十五，買漆一斛六斗七升、太半升。欲斗率之，問︰斗幾何。
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一斗， a錢
"""

"""
Suppose there is an expenditure of 5785 qian to purchase 1 hu, 6 dou, 7 sheng, and half a sheng of lacquer.
It is desired to determine the cost per dou. 
Question: how much qian per dou?

The procedure says: Multiply the quantity sought (1 dou) by the total expenditure to obtain the dividend.
Use the total quantity purchased as the divisor.
Divide the dividend by the divisor to obtain the cost per dou.

Answer: 1 dou costs *a* qian.
"""

# 出錢五千七百八十五
錢數 = 5785

# 買漆一斛六斗七升、太半升
# Convert the total quantity to dou (1 hu = 10 dou, 1 dou = 10 sheng)
漆量 = 1 * 10 + 6 + 7 / 10 + 1 / 20  # 1 hu + 6 dou + 7 sheng + half a sheng

# 以所求率乘錢數為實
實 = 1 * 錢數  # The rate sought is 1 dou

# 以所買率為法
法 = 漆量

# 實如法得一
a = Fraction(實, 法)  # Cost per dou in qian
"""
Code error: both arguments should be Rational instances"""
