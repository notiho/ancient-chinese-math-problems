"""
今有共買羊，人出五，不足四十五；人出七，不足三。問︰人數、羊價各幾何？
兩盈、兩不足術曰：置所出率，盈、不足各居其下。令維乘所出率，以少減多，餘為實。兩盈、兩不足以少減多，餘為法。實如法而一。有分者通之。
荅曰： a人 ，羊價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys sheep. If each person contributes 5, they are short by 45. If each person contributes 7, they are short by 3.
Question: how many people are there, and what is the price of the sheep?

The procedure for "two excesses or two deficits" says:
Place the contribution rates, with the deficits below each rate.
Multiply the contribution rates by their respective deficits, then subtract the smaller product from the larger product. The remainder is the dividend.
Subtract the smaller deficit from the larger deficit. The remainder is the divisor.
Divide the dividend by the divisor to get the number of people. If there is a remainder, simplify it.
The price of the sheep can then be calculated.

Answer: *a* people, and the price of the sheep is *b*.
"""

from fractions import Fraction

# Given data
rate1 = 5  # Contribution rate when short by 45
deficit1 = 45  # Shortfall when contributing 5
rate2 = 7  # Contribution rate when short by 3
deficit2 = 3  # Shortfall when contributing 7

# Calculate the dividend (實)
實 = (rate2 * deficit1) - (rate1 * deficit2)

# Calculate the divisor (法)
法 = deficit1 - deficit2

# Number of people (a)
a = Fraction(實, 法)

# Calculate the price of the sheep (b)
# Using the formula: 羊價 = 人數 * rate1 + deficit1
b = a * rate1 + deficit1

a_people = a
b_price = b

# Final answer
a_people, b_price#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 21, Actual: 50/7
Variable 'b' has wrong value. Expected: 150, Actual: 565/7"""
