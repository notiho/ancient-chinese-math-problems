"""
今有出錢一萬三千五百買竹二千三百五十箇問箇幾何
經率術曰以所買率為法所出錢數為實實如法得一錢
荅曰一箇 a錢
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 13,500 qian to buy 2,350 bamboo items.
Question: how much does each bamboo item cost?

The procedure for the price rate says: Take the number of items bought as the divisor.
Take the amount of money spent as the dividend.
Divide the dividend by the divisor to obtain the cost of one item.

Answer: one item costs *a* qian.
"""

# 所出錢數
所出錢數 = 13500

# 所買率
所買率 = 2350

# 以所買率為法，所出錢數為實
法 = 所買率
實 = 所出錢數

# 實如法得一錢
a = Fraction(實, 法)#----- content ends here -----

"""
"""
