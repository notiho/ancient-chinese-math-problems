"""
今有共買物，人出八，盈三；人出七，不足四。問︰人數、物價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，物價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys an item. 
If each person contributes 8 units, there is an excess of 3 units.
If each person contributes 7 units, there is a shortfall of 4 units.
Question: What are the number of people and the price of the item?

The procedure for the "Excess and Deficit" method says:
1. Place the contribution rates (8 and 7), with the excess (3) and deficit (4) below them, respectively.
2. Multiply the contribution rates by their respective excess or deficit, and sum these products to form the dividend (實).
3. Add the excess and deficit to form the divisor (法).
4. Divide the dividend by the divisor to find the number of people (人數). If there is a remainder, simplify it.
5. To find the price of the item (物價), subtract the smaller contribution rate from the larger one, and use the remainder to adjust the divisor and dividend proportionally.

Answer: *a* people, and the price of the item is *b*.
"""

from fractions import Fraction

# Inputs
rate1 = 8  # Contribution rate when there is an excess
excess = 3  # Excess amount
rate2 = 7  # Contribution rate when there is a deficit
deficit = 4  # Deficit amount

# Step 1: Multiply contribution rates by their respective excess/deficit
實 = (rate1 * deficit) + (rate2 * excess)  # Dividend
法 = excess + deficit  # Divisor

# Step 2: Calculate the number of people
人數 = Fraction(實, 法)

# Step 3: Calculate the price of the item
price_difference = rate1 - rate2
adjusted_dividend = Fraction(實, price_difference)
adjusted_divisor = Fraction(法, price_difference)
物價 = adjusted_dividend / adjusted_divisor

# Final results
a = 人數
b = 物價

# Output
a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 7, Actual: 53/7
Variable 'b' has wrong value. Expected: 53, Actual: 53/7"""
