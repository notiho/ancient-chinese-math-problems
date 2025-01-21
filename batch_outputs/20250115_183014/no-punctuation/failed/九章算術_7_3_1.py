"""
今有共買牛七家共出一百九十不足三百三十九家共出二百七十盈三十問家數牛價各幾何
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰 a家 牛價 b 
"""

"""
Suppose there are 7 families who together contribute 190, which is 3 less than the required amount.
Separately, there are 39 families who together contribute 270, which is 30 more than the required amount.
Question: how many families are there, and what is the price of the cow?

The procedure for "excess and deficiency" says:
Place the contribution rates, with the excess and deficiency below them.
Multiply the contribution rates, and sum them to form the dividend.
Add the excess and deficiency to form the divisor.
Divide the dividend by the divisor to find the result. If there is a remainder, simplify it.
For the families and the price of the cow:
Place the contribution rates, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend.
The dividend gives the price of the cow, and the divisor gives the number of families.

Answer: *a* families, cow price *b*.
"""

# 置所出率
所出率_不足 = 190
所出率_盈 = 270

# 盈不足各居其下
不足 = 3
盈 = 30

# 令維乘所出率并以為實
實 = (所出率_不足 * 盈) + (所出率_盈 * 不足)

# 并盈不足為法
法 = 盈 + 不足

# 實如法而一
家數 = Fraction(實, 法)

# 置所出率以少減多餘以約法實
餘 = 所出率_盈 - 所出率_不足
法 = Fraction(法, 餘)
實 = Fraction(實, 餘)

# 實為物價，法為人數
b = 實  # 牛價
a = 法  # 家數
"""
Variable 'a' has wrong value. Expected: 126, Actual: 33/80
Variable 'b' has wrong value. Expected: 3750, Actual: 651/8"""
