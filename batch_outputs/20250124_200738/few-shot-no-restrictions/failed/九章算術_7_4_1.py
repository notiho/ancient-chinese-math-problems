"""
今有共買金，人出四百，盈三千四百；人出三百，盈一百。問︰人數、金價各幾何？
兩盈、兩不足術曰：置所出率，盈、不足各居其下。令維乘所出率，以少減多，餘為實。兩盈、兩不足以少減多，餘為法。實如法而一。有分者通之。
荅曰： a人 。金價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys gold. 
When each person contributes 400, there is an excess of 3400. 
When each person contributes 300, there is an excess of 100. 
Question: what is the number of people and the price of the gold?

The procedure says: Place the contribution rates, with the excess or deficit amounts below them. 
Multiply the contribution rates by the corresponding excess or deficit amounts. 
Subtract the smaller product from the larger product to obtain the dividend. 
Subtract the smaller excess or deficit from the larger excess or deficit to obtain the divisor. 
Divide the dividend by the divisor to obtain the number of people. 
If there are fractions, simplify them.

Answer: *a* people, and the price of the gold is *b*.
"""

from fractions import Fraction

# Given data
rate1 = 400  # Contribution rate when each person contributes 400
excess1 = 3400  # Excess amount when each person contributes 400
rate2 = 300  # Contribution rate when each person contributes 300
excess2 = 100  # Excess amount when each person contributes 300

# Procedure
# Multiply the contribution rates by the corresponding excess amounts
product1 = rate1 * excess1
product2 = rate2 * excess2

# Subtract the smaller product from the larger product to obtain the dividend
dividend = product1 - product2

# Subtract the smaller excess from the larger excess to obtain the divisor
divisor = excess1 - excess2

# Divide the dividend by the divisor to obtain the number of people
a = Fraction(dividend, divisor)

# Calculate the price of the gold
# Using the formula: 金價 = 人數 * 每人出資 - 盈餘
b = a * rate1 - excess1

# Results
a_people = a
b_gold_price = b

a_people, b_gold_price#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 33, Actual: 13300/33
Variable 'b' has wrong value. Expected: 9800, Actual: 5207800/33"""
