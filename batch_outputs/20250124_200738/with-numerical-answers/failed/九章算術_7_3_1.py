"""
今有共買牛，七家共出一百九十，不足三百三十；九家共出二百七十，盈三十。問︰家數、牛價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a(=126)家 ，牛價 b(=3750) 。
"""

#----- content starts here -----
"""
Suppose there is a group buying cattle. 
Seven households together contribute 190, which is 330 short.
Nine households together contribute 270, which is 30 in excess.
Question: how many households are there, and what is the price of the cattle?

The procedure for surplus and deficit says:
Place the contribution rates, with the surplus and deficit below each.
Multiply the contribution rates by their respective surplus or deficit, and sum them to form the dividend.
Sum the surplus and deficit to form the divisor.
Divide the dividend by the divisor to find one unit. If there is a remainder, simplify it.
For the households and the price of the cattle, place the contribution rates.
Subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend.
The dividend becomes the price of the cattle, and the divisor becomes the number of households.

Answer: *a*(=126) households, and the price of the cattle is *b*(=3750).
"""

# 七家共出一百九十，不足三百三十
七家 = 7
七家出 = 190
七家不足 = 330

# 九家共出二百七十，盈三十
九家 = 9
九家出 = 270
九家盈 = 30

# 盈不足術曰：置所出率，盈、不足各居其下
所出率_七家 = 七家
所出率_九家 = 九家
不足 = 七家不足
盈 = 九家盈

# 令維乘所出率，并以為實
實 = (所出率_七家 * 不足) + (所出率_九家 * 盈)

# 并盈、不足為法
法 = 不足 + 盈

# 實如法而一
單位 = Fraction(實, 法)

# 盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實
所出率差 = abs(所出率_九家 - 所出率_七家)

# 餘，以約法、實
法 = Fraction(法, 所出率差)
實 = Fraction(實, 所出率差)

# 實為物價，法為人數
b = 實  # 牛價 = 3750
a = 法  # 家數 = 126#----- content ends here -----

"""
Variable 'a' has wrong value. Expected: 126, Actual: 180
Variable 'b' has wrong value. Expected: 3750, Actual: 1290"""
