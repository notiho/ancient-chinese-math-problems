"""
今有共買犬，人出五，不足九十；人出五十，適足。問︰人數、犬價各幾何？
盈、適足，不足、適足術曰：以盈及不足之數為實。置所出率，以少減多，餘為法。實如法得一人。其求物價者，以適足乘人數得物價。
荅曰： a人 ，犬價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people jointly buys a dog. 
If each person contributes 5 units of money, the total is 90 units short.
If each person contributes 50 units of money, the total is exactly sufficient.
Question: how many people are there, and what is the price of the dog?

The procedure says: Take the amounts of excess and deficit as the dividend.
Place the contribution rates, subtract the smaller from the larger, and the remainder is the divisor.
Divide the dividend by the divisor to obtain the number of people.
To find the price of the dog, multiply the exact contribution by the number of people.

Answer: *a* people, and the price of the dog is *b*.
"""

# 人出五，不足九十
不足 = 90
少出 = 5

# 人出五十，適足
適足 = 50

# 盈及不足之數為實
實 = 適足 - 少出 + 不足

# 置所出率，以少減多，餘為法
法 = 適足 - 少出

# 實如法得一人
a = Fraction(實, 法)

# 其求物價者，以適足乘人數得物價
b = 適足 * a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2, Actual: 3
Variable 'b' has wrong value. Expected: 100, Actual: 150"""
