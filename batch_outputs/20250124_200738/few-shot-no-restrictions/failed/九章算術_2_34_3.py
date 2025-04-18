"""
今有出錢七百二十，買縑一匹二丈一尺。欲丈率之，問︰丈幾何？
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一丈， a錢
"""

#----- content starts here -----
"""
Suppose 720 qian is spent to buy 1 bolt of silk, which is 2 zhang and 1 chi in length.
It is desired to calculate the price per zhang.
Question: how much qian per zhang?

The procedure says: Multiply the desired rate (1 zhang) by the total money spent to obtain the dividend.
Use the total length of the silk as the divisor.
Divide the dividend by the divisor to obtain the price per zhang.

Answer: 1 zhang costs *a* qian.
"""

from fractions import Fraction

# 出錢七百二十
錢數 = 720

# 買縑一匹二丈一尺
總長度 = 2 + Fraction(1, 10)  # 2丈1尺 = 2 + 1/10丈

# 所求率 (1丈)
所求率 = 1

# 以所求率乘錢數為實
實 = 所求率 * 錢數

# 以所買率為法
法 = 總長度

# 實如法得一
a = Fraction(實, 法)

# Output the result
a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 7200/61, Actual: 2400/7"""
