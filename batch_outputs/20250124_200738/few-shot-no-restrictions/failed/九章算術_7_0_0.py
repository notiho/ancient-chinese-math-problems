"""
今有共買物，人出八，盈三；人出七，不足四。問︰人數、物價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，物價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys an item. If each person contributes 8, there is an excess of 3. If each person contributes 7, there is a shortfall of 4.
Question: what are the number of people and the price of the item?

The procedure for the "excess and shortfall method" says:
1. Place the contribution rates (8 and 7), with the excess (3) and shortfall (4) below them, respectively.
2. Multiply each contribution rate by its corresponding excess or shortfall, and sum these to form the dividend (實).
3. Add the excess and shortfall to form the divisor (法).
4. Divide the dividend by the divisor to find the number of people.
5. If there is a remainder, simplify it.
6. To find the price of the item, subtract the smaller contribution rate from the larger one, and simplify the divisor and dividend accordingly.

Answer: *a* people, and the price of the item is *b*.
"""

from fractions import Fraction

# 所出率
rate1 = 8  # 每人出8，盈3
rate2 = 7  # 每人出7，不足4

# 盈、不足
excess = 3
shortfall = 4

# Step 1: Multiply each rate by its corresponding excess/shortfall
實 = (rate1 * excess) + (rate2 * shortfall)

# Step 2: Add the excess and shortfall to form the divisor
法 = excess + shortfall

# Step 3: Calculate the number of people
a = Fraction(實, 法)

# Step 4: Calculate the price of the item
# Subtract the smaller rate from the larger rate
rate_difference = rate1 - rate2

# Simplify the divisor and dividend
物價_dividend = rate_difference * a
物價_divisor = 1  # Simplified divisor is 1

b = 物價_dividend  # Since divisor is 1, the price is just the dividend

# Final answer
a_people = a
b_price = b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 7, Actual: 52/7
Variable 'b' has wrong value. Expected: 53, Actual: 52/7"""
