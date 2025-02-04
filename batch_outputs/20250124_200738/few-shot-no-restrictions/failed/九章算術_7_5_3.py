"""
今有共買羊，人出五，不足四十五；人出七，不足三。問︰人數、羊價各幾何？
兩盈、兩不足術曰：置所出率，盈、不足各居其下。令維乘所出率，以少減多，餘為實。兩盈、兩不足以少減多，餘為法。實如法而一。有分者通之。
荅曰： a人 ，羊價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys sheep. If each person contributes 5, they are short by 45. If each person contributes 7, they are short by 3.
Question: how many people are there, and what is the price of the sheep?

The procedure for "two excesses or two deficits" says: Place the contribution rates, with the deficits below each.
Multiply the contribution rates by their respective deficits, and subtract the smaller product from the larger product to obtain the dividend.
Subtract the smaller deficit from the larger deficit to obtain the divisor.
Divide the dividend by the divisor to find the number of people. If there is a remainder, simplify it.

Answer: *a* people, and the price of the sheep is *b*.
"""

from fractions import Fraction

# 所出率
rate1 = 5  # 每人出5
rate2 = 7  # 每人出7

# 盈、不足
deficit1 = 45  # 不足45
deficit2 = 3   # 不足3

# 令維乘所出率，以少減多，餘為實
實 = rate2 * deficit1 - rate1 * deficit2

# 兩盈、兩不足以少減多，餘為法
法 = deficit1 - deficit2

# 實如法而一
人數 = Fraction(實, 法)

# 羊價
羊價 = rate1 * 人數 + deficit1

# 答案
a = 人數
b = 羊價

a, b  # Output the number of people and the price of the sheep#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 21, Actual: 50/7
Variable 'b' has wrong value. Expected: 150, Actual: 565/7"""
