"""
今有共買犬，人出五，不足九十；人出五十，適足。問︰人數、犬價各幾何？
盈、適足，不足、適足術曰：以盈及不足之數為實。置所出率，以少減多，餘為法。實如法得一人。其求物價者，以適足乘人數得物價。
荅曰： a人 ，犬價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people collectively buys a dog. If each person contributes 5, the total is 90 short. 
If each person contributes 50, the total is exactly sufficient.
Question: how many people are there, and what is the price of the dog?

The procedure for "excess and sufficient, insufficient and sufficient" says:
Take the numbers of excess and insufficient as the dividend.
Place the contribution rates, subtract the smaller from the larger, and the remainder is the divisor.
Divide the dividend by the divisor to find the number of people.
To find the price of the dog, multiply the sufficient contribution by the number of people.

Answer: *a* people, and the price of the dog is *b*.
"""

# 人出五，不足九十
不足 = 90
少出率 = 5

# 人出五十，適足
適足率 = 50

# 盈及不足之數為實
實 = 不足

# 置所出率，以少減多，餘為法
法 = 適足率 - 少出率

# 實如法得一人
a = Fraction(實, 法)

# 以適足乘人數得物價
b = 適足率 * a#----- content ends here -----

"""
"""
