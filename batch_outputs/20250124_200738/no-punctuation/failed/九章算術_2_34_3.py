"""
今有出錢七百二十買縑一匹二丈一尺欲丈率之問丈幾何
經術術曰以所求率乘錢數為實以所買率為法實如法得一
荅曰一丈 a錢
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 720 qian to buy 1 bolt of silk, which is 2 zhang and 1 chi in length.
It is desired to calculate the cost per zhang.
Question: how much qian per zhang?

The procedure says: Multiply the desired rate (1 zhang) by the amount of money spent, obtaining the dividend.
Take the rate of the purchased silk as the divisor.
Divide the dividend by the divisor to obtain the cost per zhang.

Answer: 1 zhang costs *a* qian.
"""

# 出錢七百二十
錢數 = 720

# 縑一匹二丈一尺
所買率 = 2 + Fraction(1, 10)  # 2丈1尺 = 2 + 1/10丈

# 所求率 (1丈)
所求率 = 1

# 以所求率乘錢數，為實
實 = 所求率 * 錢數

# 以所買率為法
法 = 所買率

# 實如法得一
a = Fraction(實, 法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 7200/61, Actual: 2400/7"""
