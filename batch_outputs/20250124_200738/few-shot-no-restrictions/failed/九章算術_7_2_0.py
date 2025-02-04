"""
今有共買璡，人出半，盈四；人出少半，不足三。問︰人數、璡價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，璡價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys a jade item. 
If each person contributes half a unit of money, there is an excess of 4 units.
If each person contributes less than half (a quarter), there is a shortfall of 3 units.
Question: how many people are there, and what is the price of the jade item?

The procedure for "excess and shortfall" says:
1. Place the contribution rates, with the excess and shortfall amounts below them.
2. Multiply the contribution rates by their respective amounts, then add them together to form the dividend (實).
3. Add the excess and shortfall amounts together to form the divisor (法).
4. Divide the dividend by the divisor to find the result. If there is a fraction, simplify it.
5. For items jointly purchased with both excess and shortfall:
   - Place the contribution rates, subtract the smaller rate from the larger rate, and simplify the divisor and dividend.
   - The dividend represents the price of the item, and the divisor represents the number of people.

Answer: *a* people, and the jade item costs *b*.
"""

from fractions import Fraction

# Contribution rates
rate_excess = Fraction(1, 2)  # Half a unit of money
rate_shortfall = Fraction(1, 4)  # Quarter of a unit of money

# Excess and shortfall amounts
excess = 4
shortfall = 3

# Step 1: Multiply contribution rates by their respective amounts
实 = (rate_excess * shortfall) + (rate_shortfall * excess)

# Step 2: Add excess and shortfall amounts together to form the divisor
法 = excess + shortfall

# Step 3: Divide 实 by 法 to find the number of people
a = Fraction(实, 法)

# Step 4: Calculate the price of the jade item
b = a * rate_excess + excess

# Final result
a_people = a
b_price = b

a_people, b_price#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 42, Actual: 5/14
Variable 'b' has wrong value. Expected: 17, Actual: 117/28"""
