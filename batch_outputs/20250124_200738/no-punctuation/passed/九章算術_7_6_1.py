"""
今有共買豕人出一百盈一百人出九十適足問人數豕價各幾何
盈適足不足適足術曰以盈及不足之數為實置所出率以少減多餘為法實如法得一人其求物價者以適足乘人數得物價
荅曰 a人 豕價 b 
"""

#----- content starts here -----
"""
Suppose there is a group of people buying pigs together. One group of people contributes 100 each, and there is an excess of 100. Another group contributes 90 each, and it is just enough.
Question: how many people are there, and what is the price of the pig(s)?

The procedure for "excess and just enough, and deficit and just enough" says: Take the numbers of excess and deficit as the dividend.
Place the contribution rates, subtract the smaller from the larger, and the remainder is the divisor.
Divide the dividend by the divisor to get the number of people.
To find the price of the pig(s), multiply the "just enough" rate by the number of people to get the price.

Answer: *a* people, and the price of the pig(s) is *b*.
"""

# 盈一百
盈 = 100

# 人出一百
率_盈 = 100

# 人出九十
率_足 = 90

# 適足
不足 = 0

# 以盈及不足之數為實
實 = 盈 - 不足

# 置所出率，以少減多，餘為法
法 = 率_盈 - 率_足

# 實如法得一人
a = Fraction(實, 法)

# 其求物價者，以適足乘人數，得物價
b = 率_足 * a#----- content ends here -----

"""
"""
