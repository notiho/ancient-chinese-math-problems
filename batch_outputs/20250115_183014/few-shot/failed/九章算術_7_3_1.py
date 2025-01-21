"""
今有共買牛，七家共出一百九十，不足三百三十；九家共出二百七十，盈三十。問︰家數、牛價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a家 ，牛價 b 。
"""

"""
Suppose there is a group buying a cow. 
Seven families together contribute 190, which is 330 short.
Nine families together contribute 270, which is 30 in excess.
Question: how many families are there, and what is the price of the cow?

The procedure for surplus and deficit says:
Place the contribution rates, with the surplus and deficit below each.
Multiply the contribution rates by their respective surplus or deficit, and sum them to obtain the dividend.
Sum the surplus and deficit to obtain the divisor.
Divide the dividend by the divisor to obtain 1 unit.
If there are fractions, simplify them.
For those who share the same purchase item (the cow), place the contribution rates.
Subtract the smaller rate from the larger rate, and use the remainder to simplify the divisor and dividend.
The dividend becomes the price of the item, and the divisor becomes the number of people.

Answer: *a* families, and the price of the cow is *b*.
"""

from fractions import Fraction

# 置所出率
率1 = 190
率2 = 270

# 盈、不足各居其下
不足 = 330
盈 = 30

# 令維乘所出率，并以為實
實 = (率1 * 盈) + (率2 * 不足)

# 并盈、不足為法
法 = 盈 + 不足

# 實如法而一
一 = Fraction(實, 法)

# 有分者，通之 (simplify fractions)
一 = 一  # Already simplified by Fraction

# 盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實
餘 = abs(率2 - 率1)

# 約法、實
法 = Fraction(法, 餘)
實 = Fraction(實, 餘)

# 實為物價，法為人數
b = 實  # 牛價
a = 法  # 家數
"""
Variable 'a' has wrong value. Expected: 126, Actual: 9/2
Variable 'b' has wrong value. Expected: 3750, Actual: 1185"""
