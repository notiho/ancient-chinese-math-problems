"""
今有共買豕，人出一百，盈一百；人出九十，適足。問︰人數、豕價各幾何？
盈、適足，不足、適足術曰：以盈及不足之數為實。置所出率，以少減多，餘為法。實如法得一人。其求物價者，以適足乘人數得物價。
荅曰： a(=10)人 ，豕價 b(=900) 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys a pig. If each person contributes 100, there is an excess of 100. If each person contributes 90, the amount is exactly sufficient.
Question: how many people are there, and what is the price of the pig?

The procedure for "excess and sufficient, insufficient and sufficient" says: Take the numbers of excess and insufficient as the dividend.
Place the contribution rates, subtract the smaller from the larger, and the remainder becomes the divisor.
Divide the dividend by the divisor to obtain the number of people.
To find the price of the pig, multiply the sufficient contribution by the number of people.

Answer: *a*(=10) people, and the price of the pig is *b*(=900).
"""

# 盈一百
盈 = 100

# 人出一百
出率多 = 100

# 人出九十
出率少 = 90

# 適足
適足 = 出率少

# 以盈及不足之數為實
實 = 盈

# 置所出率，以少減多，餘為法
法 = 出率多 - 出率少

# 實如法得一人
a = Fraction(實, 法) # 10

# 其求物價者，以適足乘人數得物價
b = 適足 * a # 900#----- content ends here -----

"""
"""
