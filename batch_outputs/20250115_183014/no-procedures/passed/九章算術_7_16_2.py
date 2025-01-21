"""
今有善田一畝，價三百；惡田七畝，價五百。今并買一頃，價錢一萬。問︰善、惡田各幾何？
荅曰：善田 a畝 ，惡田 b畝 。
"""

"""
Suppose there is good farmland where 1 mu costs 300 coins, and poor farmland where 7 mu costs 500 coins.
Now, if 1 qing (100 mu) is purchased for 10,000 coins, how much of it is good farmland and how much is poor farmland?

Answer: *a* mu of good farmland, and *b* mu of poor farmland.
"""

# Prices and total area
善田價 = 300  # coins per mu
惡田價 = Fraction(500, 7)  # coins per mu
總價 = 10000  # total price in coins
總畝 = 100  # total area in mu

# Let the area of good farmland be a mu, and the area of poor farmland be b mu.
# We know:
# 1. a + b = 總畝
# 2. 善田價 * a + 惡田價 * b = 總價

# Solve the system of equations:
# From equation 1: b = 總畝 - a
# Substitute into equation 2:
# 善田價 * a + 惡田價 * (總畝 - a) = 總價

from fractions import Fraction

a = Fraction(總價 - 惡田價 * 總畝, 善田價 - 惡田價)
b = 總畝 - a

# Results
a, b  # a is the area of good farmland, b is the area of poor farmland.
"""
"""
