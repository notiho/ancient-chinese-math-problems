"""
今有共買金，人出四百，盈三千四百；人出三百，盈一百。問︰人數、金價各幾何？
兩盈、兩不足術曰：置所出率，盈、不足各居其下。令維乘所出率，以少減多，餘為實。兩盈、兩不足以少減多，餘為法。實如法而一。有分者通之。
荅曰： a人 。金價 b 。
"""

"""
Suppose a group of people jointly buys gold. 
If each person contributes 400, there is a surplus of 3400.
If each person contributes 300, there is a surplus of 100.
Question: how many people are there, and what is the price of the gold?

The procedure for two surpluses or two deficits says: Place the contribution rates, with the surplus or deficit below each.
Multiply the contribution rates crosswise, subtracting the smaller from the larger, and the remainder is the dividend.
For the two surpluses or two deficits, subtract the smaller from the larger, and the remainder is the divisor.
Divide the dividend by the divisor to obtain 1 [unit, i.e., the number of people].
If there is a remainder, simplify it.

Answer: there are *a* people, and the price of the gold is *b*.
"""

from fractions import Fraction

# 人出四百，盈三千四百
出率1 = 400
盈1 = 3400

# 人出三百，盈一百
出率2 = 300
盈2 = 100

# 令維乘所出率，以少減多，餘為實
實 = abs((出率1 * 盈2) - (出率2 * 盈1))

# 兩盈以少減多，餘為法
法 = abs(盈1 - 盈2)

# 實如法而一
人數 = Fraction(實, 法)

# 金價 = 出率1 * 人數 - 盈1
金價 = 出率1 * 人數 - 盈1

a = 人數
b = 金價
"""
Variable 'a' has wrong value. Expected: 33, Actual: 9800/33
Variable 'b' has wrong value. Expected: 9800, Actual: 3807800/33"""
