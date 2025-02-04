"""
今有共買雞，人出九，盈十一；人出六，不足十六。問︰人數、雞價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，雞價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys chickens. 
If each person contributes 9 units of money, there is an excess of 11 units. 
If each person contributes 6 units of money, there is a shortfall of 16 units. 
Question: how many people are there, and what is the price of the chickens?

The procedure for the "excess and shortfall" method says:
1. Place the contribution rates (amounts contributed per person), with the excess and shortfall below them respectively.
2. Multiply the contribution rates by their respective excess or shortfall, and sum these products to obtain the dividend (實).
3. Add the excess and shortfall to obtain the divisor (法).
4. Divide the dividend by the divisor to find the result. If there is a remainder, simplify it.
5. If the excess and shortfall correspond to the same purchase, subtract the smaller contribution rate from the larger one. Use the remainder to simplify the divisor and dividend.
6. The dividend represents the price of the chickens, and the divisor represents the number of people.

Answer: *a* people, and the price of the chickens is *b*.
"""

from fractions import Fraction

# Given data
rate1 = 9  # Contribution rate when there is an excess
excess = 11  # Excess amount
rate2 = 6  # Contribution rate when there is a shortfall
shortfall = 16  # Shortfall amount

# Step 1: Multiply the contribution rates by their respective excess/shortfall
實 = (rate1 * excess) + (rate2 * shortfall)

# Step 2: Add the excess and shortfall to obtain the divisor
法 = excess + shortfall

# Step 3: Divide the dividend by the divisor to find the price of the chickens
雞價 = Fraction(實, 法)

# Step 4: Subtract the smaller contribution rate from the larger one
rate_difference = rate1 - rate2

# Step 5: Simplify the divisor and dividend using the rate difference
法 = 法 // rate_difference
實 = 實 // rate_difference

# Step 6: The divisor represents the number of people, and the dividend represents the price of the chickens
人數 = 法
雞價 = 實

# Final answers
a = 人數
b = 雞價

a, b  # Output the results#----- content ends here -----

"""
Variable 'b' has wrong value. Expected: 70, Actual: 65"""
