"""
今有共買豕，人出一百，盈一百；人出九十，適足。問︰人數、豕價各幾何？
盈、適足，不足、適足術曰：以盈及不足之數為實。置所出率，以少減多，餘為法。實如法得一人。其求物價者，以適足乘人數得物價。
荅曰： a人 ，豕價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys a pig. If each person contributes 100, there is a surplus of 100. If each person contributes 90, the amount is just sufficient.
Question: how many people are there, and what is the price of the pig?

The procedure says: Take the surplus and the deficit as the dividend. Place the contribution rates, subtract the smaller rate from the larger rate, and the remainder is the divisor. Divide the dividend by the divisor to find the number of people. To find the price of the pig, multiply the sufficient contribution rate by the number of people.

Answer: *a* people, and the pig's price is *b*.
"""

# Given values
盈 = 100  # Surplus when each contributes 100
不足 = 0  # Deficit when each contributes 90 (just sufficient, so deficit is 0)
多出率 = 100  # Contribution rate when there is a surplus
少出率 = 90  # Contribution rate when it is just sufficient

# Procedure
# 盈及不足之數為實
實 = 盈 - 不足

# 置所出率，以少減多，餘為法
法 = 多出率 - 少出率

# 實如法得一人
a = Fraction(實, 法)  # Number of people

# 其求物價者，以適足乘人數得物價
b = 少出率 * a  # Price of the pig

a, b  # Output the number of people and the pig's price#----- content ends here -----

"""
"""
