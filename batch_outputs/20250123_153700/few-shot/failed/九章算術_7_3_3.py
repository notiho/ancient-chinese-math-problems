"""
今有共買牛，七家共出一百九十，不足三百三十；九家共出二百七十，盈三十。問︰家數、牛價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a家 ，牛價 b 。
"""

"""
Suppose there is a group buying a cow. 
Seven families together contribute 190, which is 330 short.
Nine families together contribute 270, which is 30 in excess.
Question: how many families are there, and what is the price of the cow?

The procedure for surplus and deficit says:
Place the contribution rates, with the surplus and deficit below each.
Multiply the contribution rates by their respective values, and sum them to obtain the dividend.
Sum the surplus and deficit to obtain the divisor.
Divide the dividend by the divisor to obtain 1 unit.
If there are fractions, simplify them.
For the surplus and deficit cases involving the same purchased item:
Place the contribution rates, subtract the smaller from the larger, and take the remainder.
Simplify the divisor and dividend.
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: *a* families, and the price of the cow is *b*.
"""

from fractions import Fraction

# Seven families contribute 190, which is 330 short
家數1 = 7
出率1 = 190
不足 = 330

# Nine families contribute 270, which is 30 in excess
家數2 = 9
出率2 = 270
盈 = 30

# Multiply contribution rates by their respective surplus/deficit and sum them
實 = (家數1 * 盈) + (家數2 * 不足)

# Sum the surplus and deficit to obtain the divisor
法 = 盈 + 不足

# Divide the dividend by the divisor to get 1 unit
單位 = Fraction(實, 法)

# Subtract the smaller contribution rate from the larger
餘 = abs(出率2 - 出率1)

# Simplify the divisor and dividend
物價 = Fraction(單位 * 餘, 1)
人數 = Fraction(物價, 餘)

# Final answers
a = int(人數)
b = int(物價)
"""
Variable 'a' has wrong value. Expected: 126, Actual: 8
Variable 'b' has wrong value. Expected: 3750, Actual: 706"""
