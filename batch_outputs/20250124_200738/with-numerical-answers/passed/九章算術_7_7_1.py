"""
今有共買犬，人出五，不足九十；人出五十，適足。問︰人數、犬價各幾何？
盈、適足，不足、適足術曰：以盈及不足之數為實。置所出率，以少減多，餘為法。實如法得一人。其求物價者，以適足乘人數得物價。
荅曰： a(=2)人 ，犬價 b(=100) 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys a dog. If each person contributes 5, the total is 90 less than the price of the dog. If each person contributes 50, the total is exactly the price of the dog.
Question: how many people are there, and what is the price of the dog?

The procedure says: Take the numbers of the surplus (exactly sufficient) and the deficit (insufficient) as the dividend.
Place the contribution rates, subtract the smaller from the larger, and the remainder is the divisor.
Divide the dividend by the divisor to obtain the number of people.
To find the price of the dog, multiply the exact contribution by the number of people.

Answer: *a*(=2) people, and the price of the dog is *b*(=100).
"""

# 不足九十
不足 = 90

# 人出五
少出 = 5

# 人出五十
多出 = 50

# 盈及不足之數為實
實 = 不足

# 置所出率，以少減多，餘為法
法 = 多出 - 少出

# 實如法得一人
a = Fraction(實, 法) # 2

# 其求物價者，以適足乘人數得物價
b = 多出 * a # 100#----- content ends here -----

"""
"""
