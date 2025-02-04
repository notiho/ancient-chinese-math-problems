"""
今有出錢七百二十，買縑一匹二丈一尺。欲丈率之，問︰丈幾何？
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一丈， a錢
"""

#----- content starts here -----
"""
Suppose 720 qian is spent to buy 1 pi of silk, which is 2 zhang and 1 chi in length.
It is desired to calculate the price per zhang.
Question: how many qian per zhang?

The procedure says: Multiply the desired rate (1 zhang) by the amount of money spent, obtaining the dividend.
Take the rate of what was bought (2 zhang and 1 chi) as the divisor.
Divide the dividend by the divisor to obtain the price per zhang.

Answer: for 1 zhang, *a* qian.
"""

# 出錢七百二十
錢數 = 720

# 買縑一匹二丈一尺
所買率 = 2 + Fraction(1, 10)  # 2丈1尺 = 2 + 1/10丈

# 所求率 (1丈)
所求率 = 1

# 以所求率乘錢數為實
實 = 所求率 * 錢數

# 以所買率為法
法 = 所買率

# 實如法得一
a = Fraction(實, 法)#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 7200/61, Actual: 2400/7"""
