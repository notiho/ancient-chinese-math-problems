"""
今有出錢一萬三千五百，買竹二千三百五十箇。問︰箇幾何？
經率術曰：以所買率為法，所出錢數為實，實如法得一錢。
荅曰：一箇， a(=270/47)錢
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 13,500 qian to buy 2,350 bamboo pieces.
Question: how much does each piece cost?

The procedure for proportional rates says: Take the quantity of items bought as the divisor (法), and the amount of money spent as the dividend (實). 
Divide the dividend by the divisor to obtain the cost per piece.

Answer: Each piece costs *a*(=270/47) qian.
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
a = Fraction(實, 法) # 270/47#----- content ends here -----

"""
"""
