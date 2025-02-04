"""
今有出錢一萬三千五百，買竹二千三百五十箇。問︰箇幾何？
經率術曰：以所買率為法，所出錢數為實，實如法得一錢。
荅曰：一箇， a錢
"""

#----- content starts here -----
"""
Suppose there is an expenditure of 13,500 qian to buy 2,350 bamboo pieces.
Question: how much does each bamboo piece cost?

The procedure says: Take the number of bamboo pieces purchased as the divisor (法), and the amount of money spent as the dividend (實). 
Divide the dividend by the divisor to obtain the cost of one bamboo piece.

Answer: one bamboo piece costs *a* qian.
"""

# 所出錢數
所出錢數 = 13500

# 所買竹數
所買竹數 = 2350

# 算出一箇的價格
a = Fraction(所出錢數, 所買竹數)

# Answer
a  # This represents the cost of one bamboo piece in qian.#----- content ends here -----

"""
"""
