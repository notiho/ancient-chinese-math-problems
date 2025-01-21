"""
今有共買牛七家共出一百九十不足三百三十九家共出二百七十盈三十問家數牛價各幾何
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰 a家 牛價 b 
"""

"""
Suppose there are 7 families collectively buying a cow, contributing 190, which is 3 less than sufficient.
Suppose there are 39 families collectively buying a cow, contributing 270, which is 30 more than sufficient.
Question: how many families are there, and what is the price of the cow?

The procedure for surplus and deficit says: Place the contribution rates, with the surplus and deficit values below them.
Multiply the contribution rates by the surplus or deficit, and add them together to form the dividend.
Add the surplus and deficit together to form the divisor.
Divide the dividend by the divisor to get the price of the item.
If there is a remainder, simplify it.
To find the number of families, place the contribution rates, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend.
The dividend becomes the price of the item, and the divisor becomes the number of families.

Answer: there are *a* families, and the price of the cow is *b*.
"""

# 置所出率
率少 = 190  # 7家共出
率多 = 270  # 39家共出

# 盈不足各居其下
不足 = 3
盈 = 30

# 令維乘所出率并以為實
實 = (率少 * 盈) + (率多 * 不足)

# 并盈不足為法
法 = 盈 + 不足

# 實如法而一，有分者通之
牛價 = Fraction(實, 法)

# 盈不足相與同其買物者，置所出率，以少減多餘以約法實
餘 = 率多 - 率少

# 餘以約法實，實為物價，法為人數
a = Fraction(法, 餘)
b = 牛價
"""
Variable 'a' has wrong value. Expected: 126, Actual: 33/80
Variable 'b' has wrong value. Expected: 3750, Actual: 2170/11"""
