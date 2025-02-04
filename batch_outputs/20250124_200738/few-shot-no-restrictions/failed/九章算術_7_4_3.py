"""
今有共買金，人出四百，盈三千四百；人出三百，盈一百。問︰人數、金價各幾何？
兩盈、兩不足術曰：置所出率，盈、不足各居其下。令維乘所出率，以少減多，餘為實。兩盈、兩不足以少減多，餘為法。實如法而一。有分者通之。
荅曰： a人 。金價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys gold. 
If each person contributes 400, there is a surplus of 3400. 
If each person contributes 300, there is a surplus of 100. 
Question: how many people are in the group, and what is the price of the gold?

The procedure says: Place the contribution rates, with the surplus or deficit below each. 
Multiply the contribution rates by their respective surpluses or deficits. Subtract the smaller product from the larger product, and the remainder is the dividend.
Subtract the smaller surplus or deficit from the larger one, and the remainder is the divisor.
Divide the dividend by the divisor to find the number of people. 
If there is a remainder, adjust accordingly.

Answer: there are *a* people, and the price of the gold is *b*.
"""

from fractions import Fraction

# Given data
rate1 = 400  # Contribution rate when surplus is 3400
surplus1 = 3400
rate2 = 300  # Contribution rate when surplus is 100
surplus2 = 100

# Step 1: Multiply contribution rates by their respective surpluses
product1 = rate1 * surplus1
product2 = rate2 * surplus2

# Step 2: Subtract the smaller product from the larger product to get the dividend
dividend = product1 - product2

# Step 3: Subtract the smaller surplus from the larger surplus to get the divisor
divisor = surplus1 - surplus2

# Step 4: Divide the dividend by the divisor to find the number of people
a = Fraction(dividend, divisor)

# Step 5: Calculate the price of the gold
# Using the equation: price = number_of_people * contribution_rate - surplus
b = a * rate1 - surplus1

# Final result
a_people = a
b_price = b

a_people, b_price#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 33, Actual: 13300/33
Variable 'b' has wrong value. Expected: 9800, Actual: 5207800/33"""
