"""
今有人持錢之蜀，賈利十三。初返歸一萬四千，次返歸一萬三千，次返歸一萬二千，次返歸一萬一千，後返歸一萬。凡五返歸錢，本利俱盡。問︰本持錢及利各幾何？
術曰：假令本錢三萬，不足一千七百三十八錢半。令之四萬，多三萬五千三百九十錢八分。
盈不足術曰：置所出率，盈、不足各居其下。令維乘所出率，并以為實。并盈、不足為法。實如法而一。有分者，通之。盈不足相與同其買物者，置所出率，以少減多，餘，以約法、實。實為物價，法為人數。荅曰：本 a錢 。利 b錢 。
"""

"""
Suppose someone holds money in Shu (a currency unit) and trades with a profit rate of 13%. 
The first return is 14,000, the second return is 13,000, the third return is 12,000, the fourth return is 11,000, and the final return is 10,000. 
In total, there are five returns, and the principal and profit are completely exhausted.
Question: how much was the principal and how much was the profit?

The procedure says: Suppose the principal is 30,000, it falls short by 1,738.5. 
Suppose it is 40,000, it exceeds by 35,390.8. 
The "Excess and Deficiency" method says: Place the given profit rate, and the excess and deficiency below it. 
Multiply the assumed principal by the profit rate, and combine them to form the dividend. 
Combine the excess and deficiency to form the divisor. 
Divide the dividend by the divisor to find the principal. 
If there is a remainder, convert it. 
For the excess and deficiency, if they are related to the same transaction, place the profit rate, subtract the smaller from the larger, and use the remainder to simplify the divisor and dividend. 
The dividend represents the price of the goods, and the divisor represents the number of people.

Answer: the principal is *a* Shu, and the profit is *b* Shu.
"""

from fractions import Fraction

# 利率
利率 = Fraction(13, 100)

# 假設本金 30,000，不足 1,738.5
假設本金1 = 30000
不足 = Fraction(17385, 10)

# 假設本金 40,000，多 35,390.8
假設本金2 = 40000
多 = Fraction(353908, 10)

# 盈不足術
# 置所出率，盈、不足各居其下
盈不足差 = 多 - 不足

# 令維乘所出率，并以為實
實 = (假設本金2 * 不足) + (假設本金1 * 多)

# 并盈、不足為法
法 = 盈不足差

# 實如法而一
本金 = Fraction(實, 法)

# 利 = 本金 * 利率
利 = 本金 * 利率

a = 本金
b = 利
"""
Variable 'a' has wrong value. Expected: 11312640000/371293, Actual: 11312640000/336523
Variable 'b' has wrong value. Expected: 10964940000/371293, Actual: 1470643200/336523"""
