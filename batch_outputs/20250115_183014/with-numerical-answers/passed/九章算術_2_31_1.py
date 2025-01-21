"""
今有出錢一百六十，買瓴甓十八枚。問︰枚幾何？
經率術曰：以所買率為法，所出錢數為實，實如法得一錢。
荅曰：一枚， a(=80/9)錢
"""

"""
Suppose 160 qian is spent to buy 18 bricks.
Question: how much does each brick cost?

The procedure for proportional rates says: Take the number of items bought as the divisor (法), and the amount of money spent as the dividend (實).
Divide the dividend by the divisor to obtain the cost per item.

Answer: each brick costs *a*(=80/9) qian.
"""

# 出錢一百六十
所出錢數 = 160

# 買瓴甓十八枚
所買率 = 18

# 以所買率為法
法 = 所買率

# 所出錢數為實
實 = 所出錢數

# 實如法得一錢
a = Fraction(實, 法) # 80/9
"""
"""
