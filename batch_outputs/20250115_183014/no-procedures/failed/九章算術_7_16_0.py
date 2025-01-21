"""
今有善田一畝，價三百；惡田七畝，價五百。今并買一頃，價錢一萬。問︰善、惡田各幾何？
荅曰：善田 a畝 ，惡田 b畝 。
"""

"""
Suppose there is good farmland (善田) where 1 mu costs 300 coins, and poor farmland (惡田) where 7 mu cost 500 coins.
Now, a total of 1 qing (100 mu) is purchased for 10,000 coins.
Question: how many mu of good farmland and poor farmland are there?

Answer: there are *a* mu of good farmland and *b* mu of poor farmland.
"""

# Define the variables
total_area = 100  # 1 qing = 100 mu
total_price = 10000  # total price in coins
good_price_per_mu = 300  # price of 1 mu of good farmland
poor_price_per_7_mu = 500  # price of 7 mu of poor farmland
poor_price_per_mu = Fraction(poor_price_per_7_mu, 7)  # price of 1 mu of poor farmland

# Let the area of good farmland be x (in mu)
# Let the area of poor farmland be y (in mu)
# We know:
# x + y = total_area
# 300x + (500/7)y = total_price

# Solve for x and y
from fractions import Fraction

# Equation 1: x + y = total_area
# Equation 2: 300x + (500/7)y = total_price

# Express y in terms of x from Equation 1
# y = total_area - x
y = total_area - Fraction(1)

# Substitute y into Equation 2
# 300x + (500/7)(total_area - x) = total_price
# Solve for x
x = Fraction(total_price - (500 / 7) * total_area, 300 - (500 / 7))

# Solve for y
y = total_area - x

# Results
a = x  # good farmland (善田)
b = y  # poor farmland (惡田)

# Output the results
a, b
"""
Code error: both arguments should be Rational instances"""
