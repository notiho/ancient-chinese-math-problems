"""
今有共買物，人出八，盈三；人出七，不足四。問︰人數、物價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，物價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys an item. If each person contributes 8, there is an excess of 3. If each person contributes 7, there is a shortage of 4.
Question: how many people are there, and what is the price of the item?

The procedure for the "Excess and Deficit Method" says:
1. Place the contribution rates (8 and 7), with the excess (3) and deficit (4) below them respectively.
2. Multiply each contribution rate by its corresponding excess or deficit, and sum these products to form the dividend (實).
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

# Step 1: Multiply each rate by its corresponding excess/deficit
product1 = rate1 * deficit
product2 = rate2 * excess

# Step 2: Sum the products to form the dividend (實)
實 = product1 + product2

# Step 3: Add the excess and deficit to form the divisor (法)
法 = excess + deficit

# Step 4: Divide the dividend by the divisor to find the number of people (人數)
a = Fraction(實, 法)  # Number of people

# Step 5: To find the price of the item (物價)
difference = rate1 - rate2  # Difference between the two rates
adjusted_dividend = 实 * difference
adjusted_divisor = 法 * difference
b = Fraction(adjusted_dividend, adjusted_divisor)  # Price of the item

a, b#----- content ends here -----

"""
Code error: name '实' is not defined"""
