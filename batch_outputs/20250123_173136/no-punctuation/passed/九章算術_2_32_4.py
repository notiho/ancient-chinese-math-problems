"""
今有出錢一萬三千五百買竹二千三百五十箇問箇幾何
經率術曰以所買率為法所出錢數為實實如法得一錢
荅曰一箇 a錢
"""

"""
Suppose there is an expenditure of 13,500 qian to purchase 2,350 bamboo pieces.
Question: how much does each piece cost?

The procedure for the unit rate says: Take the quantity purchased as the divisor (法).
Take the amount of money spent as the dividend (實).
Divide the dividend by the divisor to obtain the cost per piece.

Answer: each piece costs *a* qian.
"""

# 出錢一萬三千五百
所出錢數 = 13500

# 買竹二千三百五十箇
所買率 = 2350

# 以所買率為法
法 = 所買率

# 所出錢數為實
實 = 所出錢數

# 實如法得一錢
a = Fraction(實, 法)
"""
"""
