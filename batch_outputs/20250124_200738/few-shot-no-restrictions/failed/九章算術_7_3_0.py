"""
今有共買牛，七家共出一百九十，不足三百三十；九家共出二百七十，盈三十。問︰家數、牛價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a家 ，牛價 b 。
"""

#----- content starts here -----
"""
Suppose there is a group buying a cow. 
- Seven families together contribute 190, which is 330 short.
- Nine families together contribute 270, which is 30 extra.

Question: how many families are there, and what is the price of the cow?

The procedure for surplus and deficit says:
1. Place the contribution rates, with the surplus and deficit below them respectively.
2. Multiply the contribution rates by their respective surplus or deficit, and sum these to obtain the dividend.
3. Add the surplus and deficit to obtain the divisor.
4. Divide the dividend by the divisor to obtain 1 unit. If there is a remainder, simplify it.
5. For the surplus and deficit cases involving the same item being purchased:
   - Place the contribution rates.
   - Subtract the smaller rate from the larger rate, and simplify the divisor and dividend.
   - The dividend is the price of the item, and the divisor is the number of families.

Answer: *a* families, and the price of the cow is *b*.
"""

from fractions import Fraction

# Known values
rate_7 = 190  # Contribution rate for 7 families
rate_9 = 270  # Contribution rate for 9 families
deficit = 330  # Amount short for 7 families
surplus = 30   # Amount extra for 9 families

# Step 1: Multiply contribution rates by their respective surplus/deficit
product_7 = rate_7 * surplus
product_9 = rate_9 * deficit

# Step 2: Sum the products to obtain the dividend
dividend = product_7 + product_9

# Step 3: Add surplus and deficit to obtain the divisor
divisor = deficit + surplus

# Step 4: Divide dividend by divisor to find 1 unit (price of the cow)
price_per_cow = Fraction(dividend, divisor)

# Step 5: Determine the number of families
# Subtract smaller rate from larger rate
rate_difference = rate_9 - rate_7

# Simplify divisor and dividend
num_families = Fraction(price_per_cow, rate_difference)

# Final results
a = num_families
b = price_per_cow

a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 126, Actual: 79/24
Variable 'b' has wrong value. Expected: 3750, Actual: 790/3"""
