"""
今有共買牛七家共出一百九十不足三百三十九家共出二百七十盈三十問家數牛價各幾何
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰 a家 牛價 b 
"""

"""
Suppose there are 7 families who together contribute 190, which is 3 less than the required amount.
Separately, 39 families together contribute 270, which is 30 more than the required amount.
Question: how many families are there, and what is the price of the cow?

The procedure for surplus and deficit says:
Place the contribution rates, with the surplus and deficit amounts below them.
Multiply the contribution rates by their respective surplus or deficit, and sum them to obtain the dividend.
Sum the surplus and deficit amounts to obtain the divisor.
Divide the dividend by the divisor to obtain the unit price of the item (the cow).
If there is a remainder, simplify it.
To find the number of families, place the contribution rates, subtract the smaller from the larger, and simplify the divisor and dividend.
The dividend gives the price of the item, and the divisor gives the number of families.

Answer: *a* families, cow price *b*.
"""

# 置所出率
率_不足 = 190
率_盈 = 270

# 盈不足各居其下
不足 = 3
盈 = 30

# 令維乘所出率并以為實
實 = (率_不足 * 盈) + (率_盈 * 不足)

# 并盈不足為法
法 = 盈 + 不足

# 實如法而一
牛價 = Fraction(實, 法)

# 置所出率以少減多
差 = 率_盈 - 率_不足

# 餘以約法實
家數 = Fraction(法, 差)

# 答案
a = 家數
b = 牛價
"""
Variable 'a' has wrong value. Expected: 126, Actual: 33/80
Variable 'b' has wrong value. Expected: 3750, Actual: 2170/11"""
