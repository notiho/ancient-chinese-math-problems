"""
今有出錢七百二十買縑一匹二丈一尺欲丈率之問丈幾何
經術術曰以所求率乘錢數為實以所買率為法實如法得一
荅曰一丈 a錢
"""

#----- content starts here -----
"""
Suppose 720 qian is spent to buy one bolt of silk, which is 2 zhang and 1 chi in length.
It is desired to find the price per zhang.
Question: how many qian per zhang?

The procedure says: Multiply the desired rate (1 zhang) by the amount of money spent, obtaining the dividend.
Take the rate of what was bought (2 zhang and 1 chi) as the divisor.
Divide the dividend by the divisor to obtain the price per zhang.

Answer: 1 zhang costs *a* qian.
"""

# 出錢七百二十
錢數 = 720

# 所買率為二丈一尺 (convert to chi: 1 zhang = 10 chi)
所買率 = 2 * 10 + 1  # 2 zhang and 1 chi = 21 chi

# 所求率為一丈 (convert to chi: 1 zhang = 10 chi)
所求率 = 10  # 1 zhang = 10 chi

# 以所求率乘錢數，為實
實 = 所求率 * 錢數

# 以所買率為法
法 = 所買率

# 實如法得一
a = Fraction(實, 法)  # Price per zhang in qian#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 7200/61, Actual: 2400/7"""
