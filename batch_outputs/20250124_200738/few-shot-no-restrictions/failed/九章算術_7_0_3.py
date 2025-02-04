"""
今有共買物，人出八，盈三；人出七，不足四。問︰人數、物價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，物價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buy an item. If each person contributes 8, there is an excess of 3. 
If each person contributes 7, there is a deficit of 4. 
Question: how many people are there, and what is the price of the item?

The procedure for "excess and deficit" says:
1. Place the contribution rates (8 and 7), with the excess (3) and deficit (4) below them, respectively.
2. Multiply each contribution rate by its corresponding excess or deficit, and sum these products to form the dividend.
3. Add the excess and deficit to form the divisor.
4. Divide the dividend by the divisor to find the number of people. If there is a remainder, simplify it.
5. To find the price of the item, subtract the smaller contribution rate from the larger one, and use the remainder to simplify both the divisor and dividend.

Answer: *a* people, and the price of the item is *b*.
"""

from fractions import Fraction

# Step 1: Place the contribution rates and the excess/deficit
rate1 = 8  # Contribution rate when there is an excess
excess = 3  # Excess amount
rate2 = 7  # Contribution rate when there is a deficit
deficit = 4  # Deficit amount

# Step 2: Multiply each rate by its corresponding excess/deficit and sum them
dividend = (rate1 * deficit) + (rate2 * excess)

# Step 3: Add the excess and deficit to form the divisor
divisor = excess + deficit

# Step 4: Divide the dividend by the divisor to find the number of people
num_people = Fraction(dividend, divisor)

# Step 5: To find the price of the item, subtract the smaller rate from the larger rate
rate_difference = rate1 - rate2

# Simplify the divisor and dividend using the rate difference
simplified_divisor = divisor // rate_difference
simplified_dividend = dividend // rate_difference

# The price of the item is the simplified dividend
item_price = simplified_dividend

# Final results
a = num_people
b = item_price

a, b  # Output the number of people and the price of the item#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 7, Actual: 53/7"""
