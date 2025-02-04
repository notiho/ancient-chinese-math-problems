"""
今有共買豕，人出一百，盈一百；人出九十，適足。問︰人數、豕價各幾何？
盈、適足，不足、適足術曰：以盈及不足之數為實。置所出率，以少減多，餘為法。實如法得一人。其求物價者，以適足乘人數得物價。
荅曰： a人 ，豕價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys a pig. If each person contributes 100, there is an excess of 100. If each person contributes 90, the amount is exactly sufficient.
Question: how many people are there, and what is the price of the pig?

The procedure says: Take the excess (盈) and the shortfall (不足) as the dividend.
Place the contribution rates (所出率), subtract the smaller from the larger, and the remainder is the divisor.
Divide the dividend by the divisor to find the number of people.
To find the price of the pig, multiply the exact contribution rate (適足) by the number of people.

Answer: *a* people, and the price of the pig is *b*.
"""

# Given data
盈 = 100  # Excess amount when each person contributes 100
不足 = 0  # Shortfall amount when each person contributes 90 (exactly sufficient)
多出率 = 100  # Contribution rate when there is an excess
少出率 = 90  # Contribution rate when it is exactly sufficient

# Procedure
# 盈及不足之數為實
實 = 盈 - 不足

# 置所出率，以少減多，餘為法
法 = 多出率 - 少出率

# 實如法得一人
人數 = Fraction(實, 法)

# 以適足乘人數得物價
豕價 = 少出率 * 人數

# Final answer
a = 人數
b = 豕價#----- content ends here -----

"""
"""
