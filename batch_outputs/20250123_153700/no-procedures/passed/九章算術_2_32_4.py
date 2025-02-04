"""
今有出錢一萬三千五百，買竹二千三百五十箇。問︰箇幾何？
荅曰：一箇， a錢
"""

"""
Suppose there is 13,500 qian (ancient Chinese currency) used to buy 2,350 bamboo pieces.
Question: how much does each bamboo piece cost?

Answer: one bamboo piece costs *a* qian.
"""

# 出錢一萬三千五百
total_money = 13500

# 買竹二千三百五十箇
total_bamboo = 2350

# Calculate the cost per bamboo piece
a = Fraction(total_money, total_bamboo)

# Output the result
a
"""
"""
