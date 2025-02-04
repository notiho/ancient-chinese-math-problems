"""
今有共買金，人出四百，盈三千四百；人出三百，盈一百。問︰人數、金價各幾何？
兩盈、兩不足術曰：置所出率，盈、不足各居其下。令維乘所出率，以少減多，餘為實。兩盈、兩不足以少減多，餘為法。實如法而一。有分者通之。
荅曰： a人 。金價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys gold. 
If each person contributes 400, there is an excess of 3400.
If each person contributes 300, there is an excess of 100.
Question: how many people are there, and what is the price of the gold?

The procedure says: Place the contribution rates, with the excess or deficit below each.
Multiply the contribution rates by the corresponding excess or deficit. Subtract the smaller product from the larger product, and the remainder is the dividend.
Subtract the smaller excess or deficit from the larger one, and the remainder is the divisor.
Divide the dividend by the divisor to find the number of people.
If there is a remainder, adjust accordingly.

The answer says: *a* people, and the price of the gold is *b*.
"""

from fractions import Fraction

# Inputs
rate1 = 400  # Contribution rate for the first case
excess1 = 3400  # Excess for the first case
rate2 = 300  # Contribution rate for the second case
excess2 = 100  # Excess for the second case

# Procedure
# Multiply the contribution rates by the corresponding excess
product1 = rate1 * excess1
product2 = rate2 * excess2

# Subtract the smaller product from the larger product (dividend)
dividend = product1 - product2

# Subtract the smaller excess from the larger excess (divisor)
divisor = excess1 - excess2

# Number of people
a = Fraction(dividend, divisor)

# Gold price
b = rate1 * a - excess1

# Outputs
a_people = a
b_gold_price = b

a_people, b_gold_price#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 33, Actual: 13300/33
Variable 'b' has wrong value. Expected: 9800, Actual: 5207800/33"""
