"""
今有共買雞，人出九，盈十一；人出六，不足十六。問︰人數、雞價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a人 ，雞價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people collectively buys chickens. 
If each person contributes 9, there is a surplus of 11. 
If each person contributes 6, there is a shortage of 16. 
Question: how many people are there, and what is the price of the chickens?

The procedure for the surplus and shortage method says:
Place the contribution rates, with the surplus and shortage below them respectively. 
Multiply the contribution rates by their respective surplus or shortage, and sum them to form the dividend. 
Add the surplus and shortage to form the divisor. 
Divide the dividend by the divisor to find the result. 
If there is a remainder, simplify it. 
If the surplus and shortage correspond to the same item being purchased, subtract the smaller contribution rate from the larger one. 
Use the remainder to simplify the divisor and dividend. 
The dividend represents the price of the item, and the divisor represents the number of people.

Answer: *a* people, and the price of the chickens is *b*.
"""

from fractions import Fraction

# Inputs
rate1 = 9  # Contribution rate when surplus
surplus = 11  # Surplus amount
rate2 = 6  # Contribution rate when shortage
shortage = 16  # Shortage amount

# 盈不足術
# Multiply contribution rates by their respective surplus/shortage
dividend = (rate1 * surplus) + (rate2 * shortage)

# Add surplus and shortage to form the divisor
divisor = surplus + shortage

# Calculate the number of people and the price of the chickens
price_of_chickens = Fraction(dividend, divisor)
number_of_people = Fraction(price_of_chickens, rate1 - rate2)

# Results
a = number_of_people
b = price_of_chickens

# Output
a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 9, Actual: 65/27
Variable 'b' has wrong value. Expected: 70, Actual: 65/9"""
