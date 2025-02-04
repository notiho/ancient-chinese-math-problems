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

The procedure for "two surpluses and two deficits" says: 
Place the contribution rates, with the surpluses or deficits below each. 
Multiply the contribution rates crosswise, and subtract the smaller from the larger, leaving the remainder as the dividend. 
Subtract the smaller surplus or deficit from the larger, leaving the remainder as the divisor. 
Divide the dividend by the divisor to obtain 1. If there is a fraction, simplify it.

Answer: there are *a* people, and the price of the gold is *b*.
"""

# 置所出率，盈、不足各居其下
出率1 = 400  # 每人出400
盈1 = 3400   # 盈餘3400
出率2 = 300  # 每人出300
盈2 = 100    # 盈餘100

# 令維乘所出率，以少減多，餘為實
實 = abs((出率1 * 盈2) - (出率2 * 盈1))

# 兩盈、兩不足以少減多，餘為法
法 = abs(盈1 - 盈2)

# 實如法而一
人數 = Fraction(實, 法)

# 金價 = 每人出率 * 人數 - 盈餘
金價 = 出率1 * 人數 - 盈1

a = 人數
b = 金價
"""
Variable 'a' has wrong value. Expected: 33, Actual: 9800/33
Variable 'b' has wrong value. Expected: 9800, Actual: 3807800/33"""
