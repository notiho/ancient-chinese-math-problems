"""
今有共買豕人出一百盈一百人出九十適足問人數豕價各幾何
盈適足不足適足術曰以盈及不足之數為實置所出率以少減多餘為法實如法得一人其求物價者以適足乘人數得物價
荅曰 a人 豕價 b 
"""

#----- content starts here -----
"""
Suppose there is a group of people buying pigs. One person contributes 100, resulting in an excess of 100. Another person contributes 90, which is just enough.
Question: how many people are there, and what is the price of the pig?

The procedure for "excess equals sufficient, insufficient equals sufficient" says:
Take the numbers of excess and insufficient as the dividend.
Place the contribution rates, subtract the smaller from the larger, and the remainder becomes the divisor.
Divide the dividend by the divisor to obtain the number of people.
To find the price of the pig, multiply the sufficient amount by the number of people to get the price.

Answer: *a* people, pig price *b*.
"""

# 盈一百
盈 = 100

# 不足一百
不足 = 100

# 人出一百
出率多 = 100

# 人出九十
出率少 = 90

# 以盈及不足之數為實
實 = 盈 + 不足

# 置所出率，以少減多，餘為法
法 = 出率多 - 出率少

# 實如法得一人
a = Fraction(實, 法)

# 以適足乘人數，得物價
適足 = 出率少
b = 適足 * a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 10, Actual: 20
Variable 'b' has wrong value. Expected: 900, Actual: 1800"""
