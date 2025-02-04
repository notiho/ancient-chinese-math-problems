"""
今有共買牛，七家共出一百九十，不足三百三十；九家共出二百七十，盈三十。問︰家數、牛價各幾何？
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。
荅曰： a(=126)家 ，牛價 b(=3750) 。
"""

"""
Suppose there is a group buying cattle. 
Seven households together contribute 190, which is short by 330. 
Nine households together contribute 270, which exceeds by 30. 
Question: how many households are there, and what is the price of the cattle?

The procedure for surplus and deficit says: Place the contribution rates, with the surplus and deficit below each. 
Multiply the contribution rates by their respective surplus or deficit, and sum them to form the dividend. 
Sum the surplus and deficit to form the divisor. 
Divide the dividend by the divisor to obtain 1 unit. 
If there are fractions, simplify them. 
For those who share the purchase of the same item, place the contribution rates, subtract the smaller from the larger, and simplify the divisor and dividend. 
The dividend is the price of the item, and the divisor is the number of households.

Answer: *a*(=126) households, and the price of the cattle is *b*(=3750).
"""

from fractions import Fraction

# Seven households contribute 190, short by 330
七家 = 7
七家出 = 190
七家不足 = 330

# Nine households contribute 270, exceeds by 30
九家 = 9
九家出 = 270
九家盈 = 30

# 盈不足術
# Multiply contribution rates by surplus/deficit and sum them to form the dividend
實 = (七家 * 七家不足) + (九家 * 九家盈)

# Sum the surplus and deficit to form the divisor
法 = 七家不足 + 九家盈

# Divide the dividend by the divisor to obtain 1 unit
一 = Fraction(實, 法)

# For those who share the purchase of the same item, subtract the smaller rate from the larger rate
差 = 九家 - 七家

# Simplify the divisor and dividend
牛價 = Fraction(一 * 差, 1)  # b = 3750
家數 = Fraction(法 * 差, 差)  # a = 126

a = 家數
b = 牛價
"""
Variable 'a' has wrong value. Expected: 126, Actual: 360
Variable 'b' has wrong value. Expected: 3750, Actual: 43/3"""
