"""
今有出錢七百二十，買縑一匹二丈一尺。欲丈率之，問︰丈幾何？
經術術曰：以所求率乘錢數為實，以所買率為法，實如法得一。
荅曰：一丈， a(=7200/61)錢
"""

"""
Suppose 720 qian is spent to buy one bolt of silk, which is 2 zhang and 1 chi in length.
It is desired to determine the price per zhang.
Question: how much qian per zhang?

The procedure says: Multiply the rate being sought by the amount of money spent, obtaining the dividend.
Use the rate of what was purchased as the divisor.
Divide the dividend by the divisor to obtain the price per zhang.

Answer: 1 zhang costs *a*(=7200/61) qian.
"""

# 出錢七百二十
錢數 = 720

# 買縑一匹二丈一尺
所買率 = 2 * 10 + 1  # Convert 2丈1尺 to total chi (1丈 = 10尺)

# 所求率 (1丈 = 10尺)
所求率 = 10

# 以所求率乘錢數為實
實 = 所求率 * 錢數

# 以所買率為法
法 = 所買率

# 實如法得一
a = Fraction(實, 法)  # 7200/61 qian per zhang
"""
Variable 'a' has wrong value. Expected: 7200/61, Actual: 2400/7"""
