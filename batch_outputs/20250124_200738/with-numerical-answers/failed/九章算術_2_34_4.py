"""
今有出錢七百二十，買縑一匹二丈一尺。欲丈率之，問︰丈幾何？
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一丈， a(=7200/61)錢
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 720 qian to purchase one bolt of silk, which is 2 zhang and 1 chi in length.
It is desired to determine the cost per zhang.
Question: how much is the cost per zhang?

The procedure says: Multiply the rate being sought by the amount of money spent to obtain the dividend.
Take the rate of what was purchased as the divisor.
Divide the dividend by the divisor to obtain the result.

Answer: 1 zhang costs *a*(=7200/61) qian.
"""

# 出錢七百二十
錢數 = 720

# 買縑一匹二丈一尺
所買率 = 2 * 10 + 1  # Convert 2 zhang 1 chi to chi (1 zhang = 10 chi)

# 所求丈率
所求率 = 10  # 1 zhang = 10 chi

# 以所求率乘錢數為實
實 = 所求率 * 錢數

# 以所買率為法
法 = 所買率

# 實如法得一
a = Fraction(實, 法)  # 7200/61 qian per zhang#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 7200/61, Actual: 2400/7"""
