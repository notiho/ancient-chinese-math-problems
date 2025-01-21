"""
今有共買豕，人出一百，盈一百；人出九十，適足。問︰人數、豕價各幾何？
盈、適足，不足、適足術曰：以盈及不足之數為實。置所出率，以少減多，餘為法。實如法得一人。其求物價者，以適足乘人數得物價。
荅曰： a人 ，豕價 b 。
"""

"""
Suppose a group of people jointly buys a pig. If each person contributes 100, there is an excess of 100. 
If each person contributes 90, the amount is exactly sufficient.
Question: how many people are there, and what is the price of the pig?

The procedure for "excess and sufficient" or "deficient and sufficient" says: 
Take the amounts of excess and deficiency as the dividend.
Place the contribution rates, subtract the smaller from the larger, and the remainder is the divisor.
Divide the dividend by the divisor to get the number of people.
To find the price of the pig, multiply the sufficient contribution rate by the number of people.

Answer: *a* people, and the price of the pig is *b*.
"""

# 盈一百
盈 = 100

# 人出一百
高出率 = 100

# 人出九十
低出率 = 90

# 適足
不足 = 0

# 以盈及不足之數為實
實 = 盈 - 不足

# 置所出率，以少減多，餘為法
法 = 高出率 - 低出率

# 實如法得一人
a = Fraction(實, 法)

# 以適足乘人數得物價
b = 低出率 * a
"""
"""
