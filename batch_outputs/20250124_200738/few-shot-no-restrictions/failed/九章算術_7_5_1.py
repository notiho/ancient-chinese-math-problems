"""
今有共買羊，人出五，不足四十五；人出七，不足三。問︰人數、羊價各幾何？
兩盈、兩不足術曰：置所出率，盈、不足各居其下。令維乘所出率，以少減多，餘為實。兩盈、兩不足以少減多，餘為法。實如法而一。有分者通之。
荅曰： a人 ，羊價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people is buying sheep. If each person contributes 5, they are short by 45. If each person contributes 7, they are short by 3.
Question: how many people are there, and what is the price of the sheep?

The procedure for "two excesses and two deficits" says:
Place the contribution rates, with the deficits below each. 
Multiply the contribution rates by their respective deficits, and subtract the smaller product from the larger product to get the dividend.
Subtract the smaller deficit from the larger deficit to get the divisor.
Divide the dividend by the divisor to find the number of people. If there is a remainder, simplify it.

Answer: *a* people, and the price of the sheep is *b*.
"""

from fractions import Fraction

# Given data
rate1 = 5  # Contribution rate when each person contributes 5
deficit1 = 45  # Deficit when each person contributes 5
rate2 = 7  # Contribution rate when each person contributes 7
deficit2 = 3  # Deficit when each person contributes 7

# Procedure:
# Multiply the contribution rates by their respective deficits
product1 = rate1 * deficit1
product2 = rate2 * deficit2

# Subtract the smaller product from the larger product to get the dividend
dividend = product2 - product1

# Subtract the smaller deficit from the larger deficit to get the divisor
divisor = deficit1 - deficit2

# Divide the dividend by the divisor to find the number of people
a = Fraction(dividend, divisor)

# Calculate the price of the sheep
b = rate1 * a + deficit1

# Final answer
a_people = a
b_price = b

a_people, b_price#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 21, Actual: -34/7
Variable 'b' has wrong value. Expected: 150, Actual: 145/7"""
