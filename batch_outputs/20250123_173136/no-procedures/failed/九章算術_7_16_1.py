"""
今有善田一畝，價三百；惡田七畝，價五百。今并買一頃，價錢一萬。問︰善、惡田各幾何？
荅曰：善田 a畝 ，惡田 b畝 。
"""

"""
Suppose there is good farmland (善田) where 1 mu costs 300 coins, and poor farmland (惡田) where 7 mu costs 500 coins.
Now, a total of 1 qing (100 mu) is purchased for 10,000 coins.
Question: how many mu of good farmland and poor farmland are purchased?

Answer: *a* mu of good farmland, and *b* mu of poor farmland.
"""

# Define the total area and total cost
total_area = 100  # 1 qing = 100 mu
total_cost = 10000  # in coins

# Define the cost per mu for good and poor farmland
good_cost_per_mu = 300  # coins per mu
poor_cost_per_mu = Fraction(500, 7)  # coins per mu (500 coins for 7 mu)

# Let the area of good farmland be a, and the area of poor farmland be b
# a + b = total_area
# 300a + (500/7)b = total_cost

# Solve the system of equations
from fractions import Fraction

# Equation 1: a + b = total_area
# Equation 2: 300a + (500/7)b = total_cost

# Express b in terms of a from Equation 1
b = total_area - a

# Substitute b into Equation 2
# 300a + (500/7)(total_area - a) = total_cost
# 300a + (500/7)total_area - (500/7)a = total_cost
# (300 - 500/7)a = total_cost - (500/7)total_area

a = Fraction(total_cost - (Fraction(500, 7) * total_area), 300 - Fraction(500, 7))
b = total_area - a

# Results
善田 = a
惡田 = b

善田, 惡田
"""
Code error: name 'a' is not defined"""
