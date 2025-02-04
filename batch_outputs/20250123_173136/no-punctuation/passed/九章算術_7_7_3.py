"""
今有共買犬人出五不足九十人出五十適足問人數犬價各幾何
盈適足不足適足術曰以盈及不足之數為實置所出率以少減多餘為法實如法得一人其求物價者以適足乘人數得物價
荅曰 a人 犬價 b 
"""

"""
Suppose a group of people jointly buys a dog. 
When each person contributes 5, they are short by 90. 
When each person contributes 50, the amount is exactly sufficient.
Question: how many people are there, and what is the price of the dog?

The procedure for "excess and sufficient, deficit and sufficient" says:
Take the numbers of excess and deficit as the dividend.
Place the contribution rates, subtracting the smaller from the larger, and the remainder becomes the divisor.
Divide the dividend by the divisor to obtain the number of people.
To find the price of the dog, multiply the sufficient contribution by the number of people.

Answer: *a* people, and the price of the dog is *b*.
"""

# 盈及不足之數為實
盈 = 0  # There is no excess, so 盈 = 0
不足 = 90  # Short by 90
實 = 盈 + 不足

# 置所出率
少出率 = 5
多出率 = 50

# 以少減多餘為法
法 = 多出率 - 少出率

# 實如法得一人
a = Fraction(實, 法)

# 以適足乘人數得物價
適足 = 多出率
b = 適足 * a
"""
"""
