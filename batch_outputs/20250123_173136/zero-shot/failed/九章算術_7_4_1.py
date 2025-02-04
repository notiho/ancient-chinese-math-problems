"""
今有共買金，人出四百，盈三千四百；人出三百，盈一百。問︰人數、金價各幾何？
兩盈、兩不足術曰：置所出率，盈、不足各居其下。令維乘所出率，以少減多，餘為實。兩盈、兩不足以少減多，餘為法。實如法而一。有分者通之。
荅曰： a人 。金價 b 。
"""

"""
To solve this problem, we will translate the ancient Chinese math problem into Python code. Here's the solution:


"""


from fractions import Fraction

# Given data
rate1 = 400  # First rate (人出四百)
profit1 = 3400  # First profit (盈三千四百)
rate2 = 300  # Second rate (人出三百)
profit2 = 100  # Second profit (盈一百)

# Calculate the difference in rates and profits
rate_diff = rate1 - rate2  # Difference in rates
profit_diff = profit1 - profit2  # Difference in profits

# Calculate the number of people (a)
a = Fraction(profit_diff, rate_diff)

# Calculate the price of gold (b)
b = Fraction(profit1, a) - rate1

# The answers
a  # Number of people
b  # Price of gold


"""


This code calculates the number of people (`a`) and the price of gold (`b`) using the method described in the problem. The results are stored in the variables `a` and `b`.
"""


"""
Variable 'b' has wrong value. Expected: 9800, Actual: -9800/33"""
