"""
今有共買雞，人出九，盈十一；人出六，不足十六。問︰人數、雞價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，雞價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys chickens. 
If each person contributes 9, there is an excess of 11. 
If each person contributes 6, there is a shortfall of 16. 
Question: how many people are there, and what is the price of the chickens?

The procedure for the "excess and shortfall" method says:
1. Place the contribution rates (amounts contributed per person), with the excess and shortfall below them.
2. Multiply the contribution rates by their respective excess or shortfall, and sum these to obtain the dividend (實).
3. Add the excess and shortfall to obtain the divisor (法).
4. Divide the dividend by the divisor to find the result. If there is a remainder, simplify it.
5. If the excess and shortfall correspond to the same item being purchased, subtract the smaller contribution rate from the larger one. Use this difference to simplify the divisor and dividend.
6. The dividend gives the price of the item (chicken), and the divisor gives the number of people.

Answer: *a* people, chicken price *b*.
"""

from fractions import Fraction

# Step 1: Define the contribution rates and excess/shortfall
rate1 = 9  # Contribution rate when there is an excess
excess = 11  # Excess amount
rate2 = 6  # Contribution rate when there is a shortfall
shortfall = 16  # Shortfall amount

# Step 2: Multiply contribution rates by their respective excess/shortfall and sum them
實 = (rate1 * excess) + (rate2 * shortfall)

# Step 3: Add the excess and shortfall to obtain the divisor
法 = excess + shortfall

# Step 4: Divide the dividend by the divisor to find the chicken price
雞價 = Fraction(實, 法)

# Step 5: Subtract the smaller contribution rate from the larger one
rate_difference = rate1 - rate2

# Simplify the divisor and dividend using the rate difference
法_simplified = 法 // rate_difference
實_simplified = 實 // rate_difference

# Step 6: The simplified divisor gives the number of people
人數 = 法_simplified

# The simplified dividend gives the chicken price
雞價 = 實_simplified

# Final answer
a = 人數
b = 雞價

# Output the results
a, b#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 70, Actual: 65"""
