"""
今有共買金，人出四百，盈三千四百；人出三百，盈一百。問︰人數、金價各幾何？
兩盈、兩不足術曰：置所出率，盈、不足各居其下。令維乘所出率，以少減多，餘為實。兩盈、兩不足以少減多，餘為法。實如法而一。有分者通之。
荅曰： a人 。金價 b 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""

#----- content starts here -----

from fractions import Fraction

# Given data
rate1 = 400  # Rate of contribution per person in the first case
profit1 = 3400  # Profit in the first case
rate2 = 300  # Rate of contribution per person in the second case
profit2 = 100  # Profit in the second case

# Calculations based on the method described
# 实 = (rate1 * profit2 - rate2 * profit1)
实 = rate1 * profit2 - rate2 * profit1

# 法 = (profit2 - profit1)
法 = profit2 - profit1

# 人数 a = 实 / 法
a = 实 / 法

# 金价 b = rate1 * a - profit1
b = rate1 * a - profit1

# Convert to Fraction for exact representation
a = Fraction(a)
b = Fraction(b)

# Results
a  # Number of people
b  # Price of gold
#----- content ends here -----


"""


This code calculates the number of people (`a`) and the price of gold (`b`) using the method described in the problem. The results are stored in the variables `a` and `b`.
"""


"""
Variable 'a' has wrong value. Expected: 33, Actual: 326521634915297/1099511627776
Variable 'b' has wrong value. Expected: 9800, Actual: 7929394651980025/68719476736"""
