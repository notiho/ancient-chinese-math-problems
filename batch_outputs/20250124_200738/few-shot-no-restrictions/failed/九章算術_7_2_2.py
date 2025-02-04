"""
今有共買璡，人出半，盈四；人出少半，不足三。問︰人數、璡價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，璡價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys a jade item. 
If each person contributes half a unit, there is an excess of 4 units.
If each person contributes less than half a unit, there is a shortfall of 3 units.
Question: how many people are there, and what is the price of the jade?

The procedure for "excess and shortfall" says:
1. Place the contribution rates, with the excess and shortfall below them respectively.
2. Multiply the contribution rates by their respective excess or shortfall, and add them together to form the dividend (實).
3. Add the excess and shortfall together to form the divisor (法).
4. Divide the dividend by the divisor to find the result. If there are fractions, simplify them.
5. For items jointly purchased with both excess and shortfall:
   - Place the contribution rates.
   - Subtract the smaller rate from the larger rate, and use the remainder to simplify the divisor and dividend.
   - The dividend gives the price of the item, and the divisor gives the number of people.

Answer: *a* people, and the jade costs *b*.
"""

from fractions import Fraction

# Step 1: Define the given data
rate_high = Fraction(1, 2)  # Each person contributes half a unit
excess = 4  # Excess of 4 units
rate_low = Fraction(1, 2) - Fraction(1, 2)  # Each person contributes less than half
shortfall = 3  # Shortfall of 3 units

# Step 2: Calculate the dividend (實)
實 = (rate_high * excess) + (rate_low * shortfall)

# Step 3: Calculate the divisor (法)
法 = excess + shortfall

# Step 4: Simplify the result
璡價 = Fraction(實, 法)  # The price of the jade
人數 = 法  # The number of people

# Final answer
a = 人數
b = 璡價

#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 42, Actual: 7
Variable 'b' has wrong value. Expected: 17, Actual: 2/7"""
