"""
今有出錢五千七百八十五，買漆一斛六斗七升、太半升。欲斗率之，問︰斗幾何。
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一斗， a錢
"""

"""

"""

#----- content starts here -----

# 出錢五千七百八十五
錢數 = 5785

# 買漆一斛六斗七升、太半升
# 1 斛 = 10 斗, 1 斗 = 10 升, 1 升 = 10 太半升
所買率 = 1 * 10 + 6 + 7 / 10 + 1 / 20  # Convert to total in terms of 斗

# 以所求率乘錢數為實
所求率 = 1  # 求每斗的錢數
實 = 所求率 * 錢數

# 以所買率為法
法 = 所買率

# 實如法得一
a = Fraction(實, 法)
#----- content ends here -----


"""

"""


"""
Code error: both arguments should be Rational instances"""
