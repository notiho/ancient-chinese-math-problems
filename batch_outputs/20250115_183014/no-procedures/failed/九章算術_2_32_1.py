"""
今有出錢一萬三千五百，買竹二千三百五十箇。問︰箇幾何？
荅曰：一箇， a錢
"""

"""
Suppose there is 13,500 qian (ancient Chinese currency) used to buy 2,350 bamboo pieces.
Question: how much does each bamboo piece cost?

Answer: each bamboo piece costs *a* qian.
"""

# 出錢一萬三千五百
總錢 = 13500

# 買竹二千三百五十箇
總竹 = 2350

# Calculate the cost per bamboo piece
a = Fraction(總錢, 総竹)
"""
Code error: name '総竹' is not defined"""
