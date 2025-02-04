"""
今有共買牛七家共出一百九十不足三百三十九家共出二百七十盈三十問家數牛價各幾何
盈不足術曰置所出率盈不足各居其下令維乘所出率并以為實并盈不足為法實如法而一有分者通之盈不足相與同其買物者置所出率以少減多餘以約法實實為物價法為人數
荅曰 a家 牛價 b 
"""

#----- content starts here -----
"""
Suppose there are 7 families who together contribute 190, which is 3 less than the required amount.
Separately, 39 families contribute 270, which is 30 more than the required amount.
Question: how many families are there, and what is the price of the cow?

The procedure for surplus and deficit says:
Place the contribution rates, with the surplus and deficit below each.
Multiply the contribution rates and add them together to form the dividend.
Add the surplus and deficit to form the divisor.
Divide the dividend by the divisor to find the price of the item.
If there is a remainder, adjust it.
For the surplus and deficit, if they are the same for the item being purchased, place the contribution rates.
Subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend.
The dividend gives the price of the item, and the divisor gives the number of families.

Answer: *a* families, and the price of the cow is *b*.
"""

# 置所出率
率1 = 190
率2 = 270

# 盈不足各居其下
不足 = 3
盈 = 30

# 令維乘所出率，并以為實
實 = (率1 * 盈) + (率2 * 不足)

# 并盈不足為法
法 = 盈 + 不足

# 實如法而一
牛價 = Fraction(實, 法)

# 盈不足相與同其買物者，置所出率
# 以少減多餘以約法實
餘 = abs(率2 - 率1)
法 = abs(盈 - 不足)

# 約分
牛價 = Fraction(實, 法)

# 實為物價，法為人數
a = Fraction(餘, 法)
b = 牛價#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 126, Actual: 80/27
Variable 'b' has wrong value. Expected: 3750, Actual: 2170/9"""
