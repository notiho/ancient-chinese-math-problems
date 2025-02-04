"""
今有出錢一百六十買瓴甓十八枚問枚幾何
經率術曰以所買率為法所出錢數為實實如法得一錢
荅曰一枚 a錢
"""

"""
Suppose 160 qian is spent to buy 18 bricks.
Question: how much does each brick cost?

The procedure says: Take the rate of the purchase as the divisor, and the amount of money spent as the dividend.
Divide the dividend by the divisor to obtain the cost of one brick.

Answer: one brick costs *a* qian.
"""

# 所出錢數
所出錢數 = 160

# 所買率
所買率 = 18

# 以所買率為法，所出錢數為實
法 = 所買率
實 = 所出錢數

# 實如法得一錢
a = Fraction(實, 法)
"""
"""
