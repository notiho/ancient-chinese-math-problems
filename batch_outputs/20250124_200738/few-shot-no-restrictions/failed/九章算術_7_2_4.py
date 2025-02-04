"""
今有共買璡，人出半，盈四；人出少半，不足三。問︰人數、璡價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，璡價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buy a piece of jade. 
If each person contributes half a unit, there is an excess of 4 units.
If each person contributes less than half a unit, there is a shortfall of 3 units.
Question: how many people are there, and what is the price of the jade?

The procedure for "excess and shortfall" says:
Place the contribution rates, with the excess and shortfall values below them.
Multiply the contribution rates by their respective values, and sum them to form the dividend.
Sum the excess and shortfall values to form the divisor.
Divide the dividend by the divisor to find the result. If there is a fraction, simplify it.
For cases where the excess and shortfall are related to the same item being purchased, subtract the smaller contribution rate from the larger one.
Use the remainder to simplify the divisor and dividend.
The dividend represents the price of the item, and the divisor represents the number of people.

Answer: *a* people, and the price of the jade is *b*.
"""

from fractions import Fraction

# Given data
rate_more = Fraction(1, 2)  # Contribution rate when there is an excess
rate_less = Fraction(1, 2) - Fraction(1, 2)  # Contribution rate when there is a shortfall
excess = 4  # Excess amount
shortfall = 3  # Shortfall amount

# Step 1: Multiply contribution rates by their respective excess/shortfall values
numerator = (rate_more * excess) + (rate_less * shortfall)

# Step 2: Sum the excess and shortfall values to form the divisor
denominator = excess + shortfall

# Step 3: Divide to find the number of people
people = Fraction(numerator, denominator)

# Step 4: Find the price of the jade
price = Fraction(excess * shortfall)

# Final answer
a = people
b = price#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 42, Actual: 2/7
Variable 'b' has wrong value. Expected: 17, Actual: 12"""
