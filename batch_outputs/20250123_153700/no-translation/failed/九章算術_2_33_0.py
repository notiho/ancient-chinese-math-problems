"""
今有出錢五千七百八十五，買漆一斛六斗七升、太半升。欲斗率之，問︰斗幾何。
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一斗， a錢
"""

"""

"""


from fractions import Fraction

# 出錢五千七百八十五
錢數 = 5785

# 買漆一斛六斗七升、太半升
# 1 斛 = 10 斗, 1 斗 = 10 升
所買率 = 1 * 10 + 6 + 7 + Fraction(1, 2)  # Convert to total 升

# 所求率 (1 斗 = 10 升)
所求率 = 10

# 以所求率乘錢數為實
實 = 所求率 * 錢數

# 以所買率為法
法 = 所買率

# 實如法得一
a = Fraction(實, 法)


"""
 

`a` represents the cost of one 斗 in 錢.
"""


"""
Variable 'a' has wrong value. Expected: 173550/503, Actual: 115700/47"""
