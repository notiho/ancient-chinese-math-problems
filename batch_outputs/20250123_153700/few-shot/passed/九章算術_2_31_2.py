"""
今有出錢一百六十，買瓴甓十八枚。問︰枚幾何？
經率術曰：以所買率為法，所出錢數為實，實如法得一錢。
荅曰：一枚， a錢
"""

"""
Suppose there is an expenditure of 160 qian to buy 18 bricks.
Question: how much does each brick cost?

The procedure for calculating the rate says: Take the number of items bought as the divisor (法), and the amount of money spent as the dividend (實). 
Divide the dividend by the divisor to obtain the cost of one item.

Answer: one brick costs *a* qian.
"""

# 所出錢數
所出錢數 = 160

# 所買率 (枚數)
所買率 = 18

# 實如法得一錢
a = Fraction(所出錢數, 所買率)
"""
"""
