"""
今有共買牛，七家共出一百九十，不足三百三十；九家共出二百七十，盈三十。問︰家數、牛價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a家 ，牛價 b 。
"""

#----- content starts here -----
"""
Suppose there is a group buying a cow. 
Seven households together contribute 190, which is 330 short. 
Nine households together contribute 270, which is 30 in excess. 
Question: how many households are there, and what is the price of the cow?

The procedure for surplus and deficit says: Place the contribution rates, with the surplus and deficit below each. 
Multiply the contribution rates by their respective surplus or deficit, and sum them to form the dividend. 
Add the surplus and deficit to form the divisor. 
Divide the dividend by the divisor to find one unit. 
If there is a fraction, simplify it. 
For those sharing the same purchased item, place the contribution rates, subtract the smaller from the larger, and simplify the divisor and dividend. 
The dividend becomes the price of the item, and the divisor becomes the number of households.

Answer: *a* households, and the cow costs *b*.
"""

from fractions import Fraction

# 七家共出一百九十，不足三百三十
七家 = 7
七家出 = 190
七家不足 = 330 - 七家出

# 九家共出二百七十，盈三十
九家 = 9
九家出 = 270
九家盈 = 九家出 - 300

# 置所出率，盈、不足各居其下
所出率_七家 = 七家
所出率_九家 = 九家
不足 = 七家不足
盈 = 九家盈

# 令維乘所出率，并以為實
實 = (所出率_七家 * 不足) + (所出率_九家 * 盈)

# 并盈、不足為法
法 = 不足 + 盈

# 實如法而一
一 = Fraction(實, 法)

# 盈不足相與同其買物者，置所出率，以少減多
所出率差 = abs(所出率_九家 - 所出率_七家)

# 餘，以約法、實
物價 = Fraction(實, 所出率差)
人數 = Fraction(法, 所出率差)

# 答案
a = int(人數)  # 家數
b = int(物價)  # 牛價#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 126, Actual: 55
Variable 'b' has wrong value. Expected: 3750, Actual: 355"""
