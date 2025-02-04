"""
今有出錢一萬三千五百，買竹二千三百五十箇。問︰箇幾何？
荅曰：一箇， a錢
"""

"""
Suppose there is a total of 13,500 qian spent to buy 2,350 bamboo pieces.
Question: how much does one bamboo piece cost?

Answer: one bamboo piece costs *a* qian.
"""

# 出錢一萬三千五百
總錢 = 13500

# 買竹二千三百五十箇
竹數 = 2350

# Calculate the cost per bamboo piece
a = Fraction(總錢, 竹數)

# Result
a
"""
"""
