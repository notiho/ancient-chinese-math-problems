"""
今有共買金，人出四百，盈三千四百；人出三百，盈一百。問︰人數、金價各幾何？
兩盈、兩不足術曰：置所出率，盈、不足各居其下。令維乘所出率，以少減多，餘為實。兩盈、兩不足以少減多，餘為法。實如法而一。有分者通之。
荅曰： a(=33)人 。金價 b(=9800) 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys gold. 
If each person contributes 400, there is a surplus of 3400.
If each person contributes 300, there is a surplus of 100.
Question: how many people are there, and what is the price of the gold?

The procedure for two surpluses or two deficits says: 
Place the contribution rates, with the surpluses or deficits below them respectively.
Multiply the contribution rates crosswise, and subtract the smaller from the larger, leaving the remainder as the dividend.
For the two surpluses or two deficits, subtract the smaller from the larger, leaving the remainder as the divisor.
Divide the dividend by the divisor to obtain one unit.
If there is a fraction, simplify it.

Answer: *a*(=33) people, and the price of the gold is *b*(=9800).
"""

# 人出四百，盈三千四百
出率1 = 400
盈1 = 3400

# 人出三百，盈一百
出率2 = 300
盈2 = 100

# 令維乘所出率，以少減多，餘為實
實 = abs((出率1 * 盈2) - (出率2 * 盈1))

# 兩盈、兩不足以少減多，餘為法
法 = abs((出率1 - 出率2))

# 實如法而一
人數 = Fraction(實, 法)

# 金價 = 人數 * 出率1 - 盈1
金價 = 人數 * 出率1 - 盈1

a = 人數  # 33
b = 金價  # 9800#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 33, Actual: 9800
Variable 'b' has wrong value. Expected: 9800, Actual: 3916600"""
