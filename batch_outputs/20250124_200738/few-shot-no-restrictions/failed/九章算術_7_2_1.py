"""
今有共買璡，人出半，盈四；人出少半，不足三。問︰人數、璡價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，璡價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys a jade item. If each person contributes half a unit, there is a surplus of 4 units. 
If each person contributes less than half a unit, there is a shortfall of 3 units.
Question: how many people are there, and what is the price of the jade item?

The procedure for surplus and shortfall says:
1. Place the contribution rates, with the surplus and shortfall below them.
2. Multiply the contribution rates by their respective surplus or shortfall, and sum them to form the dividend.
3. Add the surplus and shortfall to form the divisor.
4. Divide the dividend by the divisor to find the base unit.
5. If there are fractions, simplify them.
6. For items jointly purchased with the same surplus and shortfall:
   - Place the contribution rates.
   - Subtract the smaller rate from the larger rate to find the difference.
   - Use this difference to simplify the divisor and dividend.
   - The dividend gives the price of the item, and the divisor gives the number of people.

Answer: *a* people, jade price *b*.
"""

from fractions import Fraction

# Given data
rate_more = Fraction(1, 2)  # Contribution rate when there is a surplus
rate_less = Fraction(1, 2) - Fraction(1, 2)  # Contribution rate when there is a shortfall
surplus = 4  # Surplus amount
shortfall = 3  # Shortfall amount

# Step 1: Multiply the rates by their respective surplus/shortfall and sum them
dividend = (rate_more * surplus) + (rate_less * shortfall)

# Step 2: Add the surplus and shortfall to form the divisor
divisor = surplus + shortfall

# Step 3: Divide the dividend by the divisor to find the base unit
base_unit = dividend / divisor

# Step 4: Simplify the result if necessary
base_unit = Fraction(base_unit).limit_denominator()

# Step 5: The divisor gives the number of people, and the dividend gives the price of the jade
a = divisor  # Number of people
b = dividend  # Price of the jade

# Final answer
a = divisor
b = dividend#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 42, Actual: 7
Variable 'b' has wrong value. Expected: 17, Actual: 2"""
