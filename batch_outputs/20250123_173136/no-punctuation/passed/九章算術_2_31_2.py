"""
今有出錢一百六十買瓴甓十八枚問枚幾何
經率術曰以所買率為法所出錢數為實實如法得一錢
荅曰一枚 a錢
"""

"""
Suppose there is an expenditure of 160 qian to buy 18 bricks.
Question: how many qian per brick?

The procedure says: Take the rate of what is bought as the divisor, and the amount of money spent as the dividend.
Divide the dividend by the divisor to obtain the cost per brick.

Answer: one brick costs *a* qian.
"""

# 出錢一百六十
所出錢數 = 160

# 瓴甓十八枚
所買率 = 18

# 以所買率為法
法 = 所買率

# 所出錢數為實
實 = 所出錢數

# 實如法得一錢
a = Fraction(實, 法)
"""
"""
