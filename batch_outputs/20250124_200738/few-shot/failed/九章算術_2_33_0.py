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

The procedure says: Multiply the amount of money by the unit being sought (dou), obtaining the dividend.
Take the total amount purchased as the divisor.
Divide the dividend by the divisor to obtain the price per dou.

Answer: one dou costs *a* qian.
"""

# 出錢五千七百八十五
錢數 = 5785

# 買漆一斛六斗七升、太半升
# Convert the total amount purchased into dou
# 1 hu = 10 dou, 1 dou = 10 sheng
所買率 = 10 + 6 + Fraction(7, 10) + Fraction(1, 20)  # 1 hu + 6 dou + 7 sheng + half a sheng

# 以所求率乘錢數為實
實 = 錢數

# 以所買率為法
法 = 所買率

# 實如法得一
a = Fraction(實, 法)  # Price per dou in qian#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 173550/503, Actual: 23140/67"""
