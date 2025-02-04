"""
今有出錢七百二十，買縑一匹二丈一尺。欲丈率之，問︰丈幾何？
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一丈， a錢
"""

#----- content starts here -----
"""
Suppose 720 qian is spent to buy 1 pi of silk, which is 2 zhang and 1 chi in length.
It is desired to calculate the price per zhang.
Question: how much is the price per zhang?

The procedure says: Multiply the desired rate (1 zhang) by the total money spent to obtain the dividend.
Take the total length of silk purchased as the divisor.
Divide the dividend by the divisor to obtain the price per zhang.

Answer: 1 zhang costs *a* qian.
"""

from fractions import Fraction

# 出錢七百二十
錢數 = 720

# 買縑一匹二丈一尺
# Convert 2丈1尺 to 尺 (1丈 = 10尺)
所買率 = 2 * 10 + 1  # Total length in chi

# 所求率 (1丈 = 10尺)
所求率 = 10  # Desired rate in chi (1 zhang)

# 以所求率乘錢數為實
實 = 所求率 * 錢數

# 以所買率為法
法 = 所買率

# 實如法得一 (price per zhang)
a = Fraction(實, 法)

# Output the result
a  # Price per zhang in qian#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 7200/61, Actual: 2400/7"""
