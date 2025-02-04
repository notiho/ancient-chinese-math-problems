"""
今有共買豕人出一百盈一百人出九十適足問人數豕價各幾何
盈適足不足適足術曰以盈及不足之數為實置所出率以少減多餘為法實如法得一人其求物價者以適足乘人數得物價
荅曰 a人 豕價 b 
"""

#----- content starts here -----
"""
Suppose there is a group of people buying pigs. One group contributes 100 and has 100 surplus, while another group contributes 90 and has just enough.
Question: how many people are there, and what is the price of the pig?

The procedure for "surplus and just enough, deficit and just enough" says:
Take the numbers of surplus and deficit as the dividend.
Place the contribution rates, subtract the smaller from the larger, and the remainder is the divisor.
Divide the dividend by the divisor to obtain the number of people.
To find the price of the pig, multiply the just-enough contribution by the number of people.

Answer: *a* people, pig price *b*.
"""

# 盈及不足之數為實
盈 = 100
不足 = 0
實 = 盈 - 不足

# 置所出率
所出率_多 = 100
所出率_少 = 90

# 以少減多餘為法
法 = 所出率_多 - 所出率_少

# 實如法得一人
a = Fraction(實, 法)

# 其求物價者以適足乘人數得物價
適足 = 所出率_少
b = a * 適足#----- content ends here -----

"""
"""
