"""
今有共買羊，人出五，不足四十五；人出七，不足三。問︰人數、羊價各幾何？
兩盈、兩不足術曰：置所出率，盈、不足各居其下。令維乘所出率，以少減多，餘為實。兩盈、兩不足以少減多，餘為法。實如法而一。有分者通之。
荅曰： a人 ，羊價 b 。
"""

"""
Suppose a group of people jointly buys sheep. If each person contributes 5, they are short by 45. If each person contributes 7, they are short by 3.
Question: how many people are there, and what is the price of the sheep?

The procedure for "two excesses and two deficits" says: Place the contribution rates, with the excess or deficit amounts below each.
Multiply the contribution rates by their respective amounts, then subtract the smaller from the larger. The remainder is the dividend.
Subtract the smaller excess or deficit from the larger. The remainder is the divisor.
Divide the dividend by the divisor to obtain the number of people. If there is a remainder, simplify it.

Answer: *a* people, and the price of the sheep is *b*.
"""
#ERR: misunderstood procedure (inference required)
# 置所出率，盈、不足各居其下
率1 = 5  # 每人出5
不足1 = 45  # 不足45

率2 = 7  # 每人出7
不足2 = 3  # 不足3

# 令維乘所出率，以少減多，餘為實
實 = (率2 * 不足1) - (率1 * 不足2)

# 兩盈、兩不足以少減多，餘為法
法 = 不足1 - 不足2

# 實如法而一
人數 = Fraction(實, 法)

# 羊價 = 每人出率 * 人數 + 不足
羊價 = 率1 * 人數 + 不足1

a = 人數
b = 羊價
"""
Variable 'a' has wrong value. Expected: 21, Actual: 50/7
Variable 'b' has wrong value. Expected: 150, Actual: 565/7"""
