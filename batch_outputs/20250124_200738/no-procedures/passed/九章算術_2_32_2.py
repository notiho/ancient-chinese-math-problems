"""
今有出錢一萬三千五百，買竹二千三百五十箇。問︰箇幾何？
荅曰：一箇， a錢
"""

#----- content starts here -----
"""
Suppose there is a total of 13,500 qian (ancient Chinese currency) used to buy 2,350 bamboo poles.
Question: how much does each bamboo pole cost?

Answer: each bamboo pole costs *a* qian.
"""

# 出錢一萬三千五百
總錢數 = 13500

# 買竹二千三百五十箇
竹數 = 2350

# Calculate the cost per bamboo pole
a = Fraction(總錢數, 竹數)

# Result: a is the cost per bamboo pole in qian.#----- content ends here -----

"""
"""
