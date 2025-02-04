"""
今有共買犬人出五不足九十人出五十適足問人數犬價各幾何
盈適足不足適足術曰以盈及不足之數為實置所出率以少減多餘為法實如法得一人其求物價者以適足乘人數得物價
荅曰 a人 犬價 b 
"""

#----- content starts here -----
"""
Suppose there is a group buying a dog. When each person contributes 5, they are short by 90. When each person contributes 50, it is exactly enough.
Question: how many people are there, and what is the price of the dog?

The procedure for "excess and exact, deficit and exact" says: Take the numbers of excess and deficit as the dividend.
Place the contribution rates, subtract the smaller from the larger, and the remainder is the divisor.
Divide the dividend by the divisor to obtain the number of people.
To find the price of the item, multiply the exact contribution by the number of people to obtain the price.

Answer: *a* people, and the price of the dog is *b*.
"""

# 盈及不足之數為實
盈數 = 0  # No excess
不足數 = 90
實 = 盈數 + 不足數

# 置所出率
少率 = 5
多率 = 50

# 以少減多餘為法
法 = 多率 - 少率

# 實如法得一人
a = Fraction(實, 法)

# 以適足乘人數得物價
適足 = 50
b = 適足 * a#----- content ends here -----

"""
"""
