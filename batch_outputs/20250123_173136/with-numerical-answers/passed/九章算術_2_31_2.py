"""
今有出錢一百六十，買瓴甓十八枚。問︰枚幾何？
經率術曰：以所買率為法，所出錢數為實，實如法得一錢。
荅曰：一枚， a(=80/9)錢
"""

"""
Suppose there is an expenditure of 160 qian to buy 18 bricks.
Question: how much does each brick cost?

The procedure for proportional rates says: Take the number of items bought as the divisor, and the amount of money spent as the dividend. 
Perform the division to obtain the cost per item.

Answer: Each brick costs *a*(=80/9) qian.
"""

# 出錢一百六十
出錢 = 160

# 買瓴甓十八枚
瓴甓數 = 18

# 以所買率為法
法 = 瓴甓數

# 所出錢數為實
實 = 出錢

# 實如法得一錢
a = Fraction(實, 法) # 80/9

"""
"""
