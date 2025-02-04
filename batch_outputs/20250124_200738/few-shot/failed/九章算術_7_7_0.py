"""
今有共買犬，人出五，不足九十；人出五十，適足。問︰人數、犬價各幾何？
盈、適足，不足、適足術曰：以盈及不足之數為實。置所出率，以少減多，餘為法。實如法得一人。其求物價者，以適足乘人數得物價。
荅曰： a人 ，犬價 b 。
"""

#----- content starts here -----
"""
Suppose people collectively buy a dog. If each person contributes 5, the total is 90 short. 
If each person contributes 50, the total is exactly enough.
Question: how many people are there, and what is the price of the dog?

The procedure for "excess and exact, deficit and exact" says: Take the numbers of excess and deficit as the dividend.
Place the contribution rates, subtract the smaller from the larger, and the remainder is the divisor.
Divide the dividend by the divisor to get the number of people.
To find the price of the dog, multiply the exact contribution by the number of people to get the price.

Answer: *a* people, and the price of the dog is *b*.
"""

# 人出五，不足九十
不足 = 90
少出 = 5

# 人出五十，適足
適足 = 50

# 盈及不足之數為實
實 = 不足 + 適足

# 置所出率，以少減多，餘為法
法 = 適足 - 少出

# 實如法得一人
a = Fraction(實, 法)

# 以適足乘人數得物價
b = 適足 * a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2, Actual: 28/9
Variable 'b' has wrong value. Expected: 100, Actual: 1400/9"""
