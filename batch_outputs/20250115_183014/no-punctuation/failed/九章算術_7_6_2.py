"""
今有共買豕人出一百盈一百人出九十適足問人數豕價各幾何
盈適足不足適足術曰以盈及不足之數為實置所出率以少減多餘為法實如法得一人其求物價者以適足乘人數得物價
荅曰 a人 豕價 b 
"""

"""
Suppose a group of people jointly buy a pig. Some people contribute 100, leaving an excess of 100. Others contribute 90, which is just enough.
Question: how many people are there, and what is the price of the pig?

The procedure for "excess and just enough, deficit and just enough" says:
Take the numbers of excess and deficit as the dividend.
Place the contribution rates, subtract the smaller from the larger, and the remainder becomes the divisor.
Divide the dividend by the divisor to obtain the number of people.
To find the price of the pig, multiply the number of people by the just-enough contribution rate.

Answer: *a* people, and the pig's price is *b*.
"""

# 盈一百
盈 = 100

# 不足一百
不足 = 100

# 人出一百
多出率 = 100

# 人出九十
少出率 = 90

# 以盈及不足之數為實
實 = 盈 + 不足

# 置所出率，以少減多，餘為法
法 = 多出率 - 少出率

# 實如法得一人
a = Fraction(實, 法)

# 以適足乘人數，得物價
b = a * 少出率
"""
Variable 'a' has wrong value. Expected: 10, Actual: 20
Variable 'b' has wrong value. Expected: 900, Actual: 1800"""
