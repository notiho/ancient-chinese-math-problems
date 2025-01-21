"""
今有出錢一萬三千五百，買竹二千三百五十箇。問︰箇幾何？
經率術曰：以所買率為法，所出錢數為實，實如法得一錢。
荅曰：一箇， a錢
"""

"""
Suppose there is an expenditure of 13,500 qian to buy 2,350 bamboo pieces.
Question: how much does each piece cost?

The procedure for proportional rates says: Take the number of items bought as the divisor (法), and the amount of money spent as the dividend (實). 
Divide the dividend by the divisor to obtain the cost of one piece.

Answer: one piece costs *a* qian.
"""

# 出錢一萬三千五百
出錢 = 13500

# 買竹二千三百五十箇
竹數 = 2350

# 以所買率為法
法 = 竹數

# 所出錢數為實
實 = 出錢

# 實如法得一錢
a = Fraction(實, 法)
"""
"""
