"""
今有出錢一百六十，買瓴甓十八枚。問︰枚幾何？
經率術曰：以所買率為法，所出錢數為實，實如法得一錢。
荅曰：一枚， a錢
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 160 qian to buy 18 bricks.
Question: how much does one brick cost?

The procedure says: Take the number of items purchased as the divisor (法), and the amount of money spent as the dividend (實).
Divide the dividend by the divisor to obtain the cost of one brick.

Answer: one brick costs *a* qian.
"""

# 出錢一百六十
所出錢數 = 160

# 買瓴甓十八枚
所買率 = 18

# 以所買率為法，所出錢數為實
法 = 所買率
實 = 所出錢數

# 實如法得一錢
a = Fraction(實, 法)

# Output the result
a#----- content ends here -----

"""
"""
