"""
今有共買璡，人出半，盈四；人出少半，不足三。問︰人數、璡價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，璡價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buy a jade item. 
If each person contributes half of the price, there is an excess of 4. 
If each person contributes less than half (a quarter of the price), there is a deficit of 3. 
Question: What is the number of people and the price of the jade?

The procedure for solving excess and deficit problems says:
1. Place the contribution rates, with the excess and deficit below them.
2. Multiply the contribution rates by their respective excess or deficit, and sum them to form the dividend (實).
3. Add the excess and deficit to form the divisor (法).
4. Divide the dividend by the divisor to find the result. If there is a fraction, simplify it.
5. For problems where the excess and deficit relate to the same item being purchased:
   - Subtract the smaller contribution rate from the larger one.
   - Use this difference to simplify the divisor and dividend.
   - The dividend gives the price of the item, and the divisor gives the number of people.

Answer: *a* people, jade price *b*.
"""

from fractions import Fraction

# Given data
rate1 = Fraction(1, 2)  # Contribution rate when there is an excess of 4
excess = 4              # Excess amount
rate2 = Fraction(1, 4)  # Contribution rate when there is a deficit of 3
deficit = -3            # Deficit amount

# Step 1: Multiply contribution rates by their respective excess/deficit
實 = (rate1 * excess) + (rate2 * deficit)

# Step 2: Add the excess and deficit to form the divisor
法 = excess - deficit  # Note: Subtract deficit because it's negative

# Step 3: Simplify the divisor and dividend
price = 實 / 法  # Price of the jade
people = price / rate1  # Number of people

# Final results
a = people
b = price

a, b  # Output the number of people and the jade price#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 42, Actual: 5/14
Variable 'b' has wrong value. Expected: 17, Actual: 5/28"""
