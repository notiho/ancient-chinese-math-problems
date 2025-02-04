"""
今有出錢一萬三千五百買竹二千三百五十箇問箇幾何
經率術曰以所買率為法所出錢數為實實如法得一錢
荅曰一箇 a錢
"""

"""
Suppose there is an expenditure of 13,500 qian to buy 2,350 bamboo pieces.
Question: how much does each piece cost?

The procedure for the rate says: Take the quantity of bamboo bought as the divisor (法).
Take the amount of money spent as the dividend (實).
Divide the dividend by the divisor to obtain the cost of one piece.

The answer says: one piece costs *a* qian.
"""

# 所出錢數
所出錢數 = 13500

# 所買率
所買率 = 2350

# 實如法得一錢
a = Fraction(所出錢數, 所買率)
"""
"""
