"""
今有共買物，人出八，盈三；人出七，不足四。問︰人數、物價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，物價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys an item. 
If each person contributes 8, there is an excess of 3. 
If each person contributes 7, there is a shortage of 4. 
Question: how many people are there, and what is the price of the item?

The procedure for the "Excess and Deficit" method says:
1. Place the contribution rates, with the excess and deficit below each rate.
2. Multiply each contribution rate by its corresponding excess or deficit, and sum these to form the dividend (實).
3. Add the excess and deficit to form the divisor (法).
4. Divide the dividend by the divisor to find the result. If there is a remainder, simplify it.
5. To find the price of the item, subtract the smaller contribution rate from the larger one, and use the remainder to simplify the divisor and dividend.
6. The dividend gives the price of the item, and the divisor gives the number of people.

Answer: *a* people, and the price of the item is *b*.
"""

from fractions import Fraction

# Inputs
rate1 = 8  # Contribution rate when there is an excess
excess = 3  # Excess amount
rate2 = 7  # Contribution rate when there is a deficit
deficit = 4  # Deficit amount

# Step 1: Multiply each rate by its corresponding excess/deficit
實 = (rate1 * deficit) + (rate2 * excess)

# Step 2: Add the excess and deficit to form the divisor
法 = excess + deficit

# Step 3: Calculate the number of people
人數 = Fraction(實, 法)

# Step 4: Calculate the price of the item
price_difference = rate1 - rate2
物價 = Fraction(實, 法) * price_difference

# Outputs
a = 人數
b = 物價

a, b  # Number of people and price of the item#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 7, Actual: 53/7
Variable 'b' has wrong value. Expected: 53, Actual: 53/7"""
