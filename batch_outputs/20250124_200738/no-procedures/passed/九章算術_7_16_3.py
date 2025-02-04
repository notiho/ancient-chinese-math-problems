"""
今有善田一畝，價三百；惡田七畝，價五百。今并買一頃，價錢一萬。問︰善、惡田各幾何？
荅曰：善田 a畝 ，惡田 b畝 。
"""

#----- content starts here -----
"""
Suppose there is good farmland (善田) where 1 mu costs 300 coins, and poor farmland (惡田) where 7 mu cost 500 coins.
Now, a total of 1 qing (100 mu) is purchased for 10,000 coins.
Question: how many mu of good farmland and poor farmland are purchased?

Answer: *a* mu of good farmland, and *b* mu of poor farmland.
"""

# Define the given values
善田價 = 300  # price per mu of good farmland
惡田價 = Fraction(500, 7)  # price per mu of poor farmland
總田地 = 100  # total land in mu (1 qing = 100 mu)
總價錢 = 10000  # total price in coins

# Let the amount of good farmland be a mu, and poor farmland be b mu
# We know:
# a + b = 100  (total land)
# 300a + (500/7)b = 10000  (total cost)

# Solve the system of equations
# From the first equation: b = 100 - a
# Substitute into the second equation:
# 300a + (500/7)(100 - a) = 10000

from fractions import Fraction

a = Fraction(10000 * 7 - 500 * 100, 300 * 7 - 500)  # Solve for a
b = 100 - a  # Solve for b

# Results
a, b  # a is the amount of good farmland, b is the amount of poor farmland#----- content ends here -----

"""
"""
