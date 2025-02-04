"""
今有共買犬，人出五，不足九十；人出五十，適足。問︰人數、犬價各幾何？
盈、適足，不足、適足術曰：以盈及不足之數為實。置所出率，以少減多，餘為法。實如法得一人。其求物價者，以適足乘人數得物價。
荅曰： a人 ，犬價 b 。
"""

#----- content starts here -----
"""
Suppose a group of people collectively buys a dog. 
If each person contributes 5, the total is 90 short. 
If each person contributes 50, the total is just enough.
Question: how many people are there, and what is the price of the dog?

The procedure for "excess and just enough, shortfall and just enough" says:
Take the numbers of excess and shortfall as the dividend.
Place the contribution rates, subtract the smaller from the larger, and the remainder is the divisor.
Divide the dividend by the divisor to obtain the number of people.
To find the price of the dog, multiply the just-enough contribution by the number of people.

Answer: *a* people, and the price of the dog is *b*.
"""

# 不足九十
不足 = 90

# 適足
適足 = 50

# 人出五
少出 = 5

# 人出五十
多出 = 50

# 以盈及不足之數為實
實 = 不足 + 適足

# 置所出率，以少減多，餘為法
法 = 多出 - 少出

# 實如法得一人
a = Fraction(實, 法)

# 其求物價者，以適足乘人數得物價
b = 適足 * a#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 2, Actual: 28/9
Variable 'b' has wrong value. Expected: 100, Actual: 1400/9"""
