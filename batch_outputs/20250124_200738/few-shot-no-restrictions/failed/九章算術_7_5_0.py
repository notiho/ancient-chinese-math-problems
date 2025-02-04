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
Multiply the contribution rates by their respective deficits, and subtract the smaller product from the larger product. The remainder is the dividend.
Subtract the smaller deficit from the larger deficit. The remainder is the divisor.
Divide the dividend by the divisor to find the number of people. If there is a remainder, simplify it.
The price of the sheep is then calculated.

Answer: there are *a* people, and the price of the sheep is *b*.
"""

from fractions import Fraction

# Inputs
rate1 = 5  # Each person contributes 5
deficit1 = 45  # Short by 45

rate2 = 7  # Each person contributes 7
deficit2 = 3  # Short by 3

# Step 1: Multiply the rates by their respective deficits
product1 = rate1 * deficit1
product2 = rate2 * deficit2

# Step 2: Subtract the smaller product from the larger product to get the dividend
dividend = abs(product2 - product1)

# Step 3: Subtract the smaller deficit from the larger deficit to get the divisor
divisor = abs(deficit2 - deficit1)

# Step 4: Divide the dividend by the divisor to find the number of people
people = Fraction(dividend, divisor)

# Step 5: Calculate the price of the sheep
# If each person contributes rate1, the total contribution is rate1 * people, and the price of the sheep is this total plus the deficit
sheep_price = rate1 * people + deficit1

# Results
a = people
b = sheep_price

a, b#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 21, Actual: 34/7
Variable 'b' has wrong value. Expected: 150, Actual: 485/7"""
