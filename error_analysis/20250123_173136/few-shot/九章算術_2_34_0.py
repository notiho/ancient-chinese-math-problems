"""
今有出錢七百二十，買縑一匹二丈一尺。欲丈率之，問︰丈幾何？
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一丈， a錢
"""

"""
Suppose 720 qian is spent to buy 1 pi of silk, which is 2 zhang and 1 chi in length.
It is desired to calculate the cost per zhang.
Question: how much qian per zhang?

The procedure says: Multiply the rate being sought by the amount of money, obtaining the dividend.
Take the rate of what was bought as the divisor.
Divide the dividend by the divisor to obtain the result.

Answer: for 1 zhang, it is *a* qian.
"""

# 出錢七百二十
錢數 = 720

# 買縑一匹二丈一尺
#ERR: misunderstood expression
#縑一匹二丈一尺 -> 1 pi of silk, which is 2 zhang and 1 chi in length
#所買率 = 2 + Fraction(1, 10)  # 2丈1尺 = 2 + 1/10丈
所買率 = 4 *1 + 2 + Fraction(1, 10)

# 以所求率乘錢數為實
所求率 = 1  # 求每丈的費用
實 = 所求率 * 錢數

# 以所買率為法
法 = 所買率

# 實如法得一
a = Fraction(實, 法)
"""
Variable 'a' has wrong value. Expected: 7200/61, Actual: 2400/7"""
